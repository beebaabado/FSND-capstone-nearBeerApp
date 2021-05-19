#!/usr/bin/env python3
""" Top beers in town """
from pprint import pprint
import os
import sys
import collections
from datetime import datetime, timedelta
import json
import requests
import bs4
import urllib3
import rest_client
urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

def main():
  """ Main """
  untappd = Untappd(os.path.dirname(__file__) + '/untappd.json', '/Volumes/untappd/keys.json')
  beers_venues = untappd.top_beers_near('boulder')
  print(json.dumps(beers_venues, indent=2))
  sys.exit()
  beers_venues = untappd.top_beers_near('granite_shoals')
  beers_venues = untappd.top_beers_near('goleta')
  beers_venues = untappd.top_beers_near('minneapolis')
  beers_venues = untappd.top_beers_near('granite_shoals')
  sys.exit()
  # full_cycle = untappd.venue.info('755706').GET()
  # pprint(full_cycle['response']['venue']['venue_slug'])


class Untappd():
  """All things Untappd"""
  def __init__(self, config_path, keys_path):
    self.config = self.read_config(config_path)
    api_keys = self.read_config(keys_path)
    self.api = Untappd_Rest(api_keys['untappd']['client_id'], api_keys['untappd']['client_secret'])
    self.scraper = Untappd_Scrape()
    self.checkin_days = 7  # default
    self.cache = {'venues': {}, 'beers': {}, 'menus': {}, 'checkins': {}}
    self.check_cache_dirs()

  def top_beers_near(self, location, styles=['all'], abv_range=[0, 100]):
    """main function to search out beers for a given location"""
    checkins = self.cached_get('checkins', location)
    if not checkins:
      return {}
    beers = []
    venues = {}
    for beer_id in checkins:   
      for venue_id in checkins[beer_id]['venues']:
        beer = {}
        beer_data = self.cached_get('beers', beer_id)
        beer_keys = ['bid', 'beer_name', 'beer_abv', 'beer_style', 'rating_score', 'beer_slug']
        beer = {k:beer_data[k] for k in beer_keys if k in beer_data}
        beer['brewery_slug'] = beer_data['brewery']['brewery_slug']
        beer['brewery_name'] = beer_data['brewery']['brewery_name']
        beer['major_style'] = self.major_style(beer['beer_style'])
        beer['untappd_url'] = "https://untappd.com/b" + "/" + beer['brewery_slug'] + beer['beer_slug'] + "/" + beer_id
        beer['venue_id'] = venue_id
        beer['last_seen'] = checkins[beer_id]['venues'][venue_id]['last_seen']
        if venue_id not in venues:
          venues[venue_id] = {}
          venue = self.cached_get('venues', venue_id)
          if venue:
            venue_keys = ['venue_name', 'venue_slug', 'location']
            venues[venue_id] = {k:venue[k] for k in venue_keys if k in venue}
            venues[venue_id]['total_user_count'] = venue['stats']['total_user_count']
          else:
            continue
        if venues[venue_id]['total_user_count'] < 50:
          continue
        beers.append(beer)
    beers = sorted(beers, key = lambda i: i['rating_score'], reverse=True)
    venues = {k:v for (k,v) in venues.items() if venues[k]['total_user_count'] > 50}
    return { 'beers': beers, 'venues': venues }

  def get_styles(self):
    return self.config['styles']

  def major_style(self, beer_style):
    for style_data in self.config['styles']:
      for pattern in style_data['patterns']:
        if pattern.lower() in beer_style.lower():
          return style_data['major']
    return 'Other'

  def beers_near(self, location):
    """old function using BeautifulSoup to search out beers for a given location"""
    beers = {}
    for venue_id in self.venue_list(location):
      venue = self.cached_get('venues', venue_id)
      if not venue:
        print('No venue:', venue_id, file=sys.stderr)
        continue
      menu = self.cached_get('menus', venue_id)
      if not menu:
        print('No menu:', venue_id, file=sys.stderr)
        continue
      for beer_id in menu.keys():
        if beer_id not in beers:
          beer = self.cached_get('beers', beer_id)
          if not beer:
            break
          beers[beer_id] = {}
          beers[beer_id] = beer
          # beers[beer_id] = self.cached_get('beers', beer_id)
          beers[beer_id]['venues'] = {}
        beers[beer_id]['venues'][venue_id] = {}
        beers[beer_id]['venues'][venue_id]['servings'] = menu[beer_id]
        beers[beer_id]['venues'][venue_id]['name'] = venue['venue_name']
    # return beers
    return collections.OrderedDict(sorted(
        beers.items(), key=lambda t: t[1]['rating_score'], reverse=True
    ))

  def the_pub(self, location, delta=timedelta(days=7), checkins={}, **kwargs):
    lat = self.config['locations'][location]['lat']
    lng = self.config['locations'][location]['lng']
    radius = self.config['locations'][location]['radius']
    if 'days' in self.config['locations'][location]:
      delta = timedelta(days=int(self.config['locations'][location]['days']))
    hit_cache = False
    checkin_time = datetime.today()  # default
    #print(kwargs)
    response = self.api.thepub.local.GET(lat=lat, lng=lng, radius=radius, **kwargs)
    if response.status_code == 429:
      print('Hit Status 429!!!')
      return checkins
    pub_checkins = response.json()
    #if 'max_id' in kwargs:
    #   sys.exit()
    for checkin in pub_checkins['response']['checkins']['items']:
      self.cache_store('checkins', checkin['checkin_id'], checkin)  # temporary
      if not self.valid_venue(checkin):  # Skip if venue is not in list of accepted types
        continue
      beer_id = str(checkin['beer']['bid'])
      if beer_id not in checkins:
        checkins[beer_id] = {'venues': {}, 'checkin_ids': []}
      checkin_time = datetime.strptime(checkin['created_at'], '%a, %d %b %Y %H:%M:%S +%f')
      if checkin['checkin_id'] in checkins[beer_id]['checkin_ids']:
        hit_cache = True
        break
      checkins[beer_id]['checkin_ids'].append(checkin['checkin_id'])
      venue_id = str(checkin['venue']['venue_id'])
      if venue_id in checkins[beer_id]['venues']:
        if checkins[beer_id]['venues'][venue_id]['last_seen']:
          if checkins[beer_id]['venues'][venue_id]['last_seen'] < checkin_time.isoformat():
            checkins[beer_id]['venues'][venue_id] = {'last_seen': checkin_time.isoformat()}
      else:
        checkins[beer_id]['venues'][venue_id] = {'last_seen': checkin_time.isoformat()}
      checkins[beer_id]['beer_style'] = checkin['beer']['beer_style']
      checkins[beer_id]['beer_abv'] = checkin['beer']['beer_abv']
    if checkin_time > (datetime.today() - delta) and not hit_cache:
      #max_id = response.json()['response']['pagination']['max_id']
      max_id = pub_checkins['response']['pagination']['max_id']
      print('max_id =', max_id)
      self.the_pub(location, delta=delta, checkins=checkins, max_id=max_id)
    checkins = self.checkins_delete_old(checkins, delta)
    return checkins

  def checkins_delete_old(self, checkins, delta):
    cutoff = (datetime.today() - delta)
    for checkin in list(checkins):
      for venue in list(checkins[checkin]['venues']):
        if ( datetime.fromisoformat(checkins[checkin]['venues'][venue]['last_seen']) < cutoff ):
          del checkins[checkin]['venues'][venue]
      if len(checkins[checkin]['venues']) == 0:
        del checkins[checkin]
    return checkins

  def valid_venue(self, checkin):
    if 'venue' in checkin:
      if 'categories' in checkin['venue']:
        if 'items' in checkin['venue']['categories']:
          for category in checkin['venue']['categories']['items']:
            if category['category_key'] in self.config['valid_venue_categories']:
              return True
            else:
              print('Invalid category:', checkin['venue']['categories']['items'], file=sys.stderr)
    return False

  def venue_beers(self, venue_id):
    if venue_id in self.cache['venues']:
      return self.cache['venues'][venue_id]
    self.venue.info(venue_id)

  def cached_get(self, c_type, c_id):
    if c_id in self.cache[c_type] and self.cache[c_type][c_id]:
      #print(c_type, c_id, 'from memory', file=sys.stderr)
      pass
    elif os.path.isfile(self.config['cache_root'] + '/' + c_type + '/' + str(c_id)):
      # retrieve from file cache
      #print(c_type, c_id, 'from file', file=sys.stderr)
      with open(self.config['cache_root'] + '/' + c_type + '/' + str(c_id)) as cache_fh:
        self.cache[c_type][c_id] = json.load(cache_fh)
      if c_type == 'checkins':  # Read from cache but still check for new ones and store
        c_data = self.the_pub(c_id, checkins=self.cache[c_type][c_id])
        self.cache_store(c_type, c_id, c_data)
    else:  # retrieve from API
      #print(c_type, c_id, 'from API', file=sys.stderr)
      if c_type == 'venues':
        c_data = self.venue_get(c_id)
      elif c_type == 'beers':
        c_data = self.beer_get(c_id)
      elif c_type == 'menus':
        c_data = self.menu_get(c_id)
      elif c_type == 'checkins':
        c_data = self.the_pub(c_id)
      else:
        print('Invalid type:', c_type, file=sys.stderr)
      if c_data:
        self.cache[c_type][c_id] = c_data
        self.cache_store(c_type, c_id, c_data)
      else:
        return False
    return self.cache[c_type][c_id]

  def venue_get(self, venue_id):
    try:
      venue = self.api.venue.info(venue_id).GET()
      venue.raise_for_status()
    except requests.exceptions.HTTPError as e:
      print(e.response, file=sys.stderr)
      return False
    return venue.json()['response']['venue']

  def beer_get(self, beer_id):
    try:
      beer = self.api.beer.info(beer_id).GET()
      beer.raise_for_status()
    except requests.exceptions.HTTPError as e:
      print(e.response, file=sys.stderr)
      return False
    return beer.json()['response']['beer']

  def menu_get(self, venue_id):
    venue = self.cached_get('venues', venue_id)
    return self.scraper.menu_get(venue_id, venue['venue_slug'])

  def check_cache_dirs(self):
    root = self.config['cache_root'] + '/'
    for dir in ['', 'venues', 'beers', 'menus', 'checkins']:
      if not os.path.isdir(root + dir):
        os.mkdir(root + dir)

  def read_config(self, config_path):
    with open(config_path, 'r') as conf_fh:
      return json.load(conf_fh)

  def venue_list(self, location):
    return self.config['locations'][location]

  def cache_store(self, c_type, c_id, c_data):
    with open(self.config['cache_root'] + '/' + c_type + '/' + str(c_id), 'w') as c_fh:
      json.dump(c_data, c_fh, indent=2)


class Untappd_Scrape():
  """Scrape what is not available via API"""
  def __init__(self):
    self.bs_url = 'https://untappd.com/v'

  def untappd_request(self, url):
    """Pull from untappd"""
    user_agent = 'Mozilla/5.0 (X11; Linux i686; rv:80.0) Gecko/20100101 Firefox/80.0'
    headers = {'User-Agent': user_agent}
    try:
      response = requests.get(url, headers=headers, verify=False)
    except requests.exceptions.RequestException as http_error:
      raise SystemExit(http_error)
    return response.text

  def menu_get(self, v_id, slug):
    """Get all the taps if menus provided"""
    url = '{}/{}/{}'.format(self.bs_url, slug, v_id)
    resp = self.untappd_request(url)
    soup = bs4.BeautifulSoup(resp, 'html.parser')
    beers = {}
    menus = soup.find_all('ul', {'class': 'menu-section-list'})
    for menu in menus:
      for beer in menu:
        if not isinstance(beer, bs4.element.Tag):
          continue
        details = beer.find('div', {'class': 'beer-details'})
        href = details.find('a', {'data-href': ':beer'}).get('href')
        beer_id = href.split('/')[-1]
        prices = beer.find('div', {'class': 'beer-prices'})
        servings = collections.OrderedDict()
        if prices:
          for serving in prices.find_all('p'):
            size = serving.find('span', {'class': 'size'}).contents[0]
            price = serving.find('span', {'class': 'price'}).contents[0]
            servings[size] = price
        beers[beer_id] = servings
    return beers


class Untappd_Rest(rest_client.RestClient):
  """All things Untappd API and BeautifulSoup"""
  def __init__(self, client_id, client_secret):
    api_url = 'https://api.untappd.com/v4'
    super().__init__(api_url)
    self.standard_query_args.update({'client_id': client_id, 'client_secret': client_secret})
    self.rate_limit = 100
    self.rate_limit_remaining = 100

  def __call__(self, *argv, **kwargs):
    """Append this call argument as segment"""
    if self.method:
      if self.rate_limit_remaining == 0:
        return
      r = self.api_request(*argv, **kwargs)
      if 'headers' in r:
        if 'X-Ratelimit-Remaining' in r.headers:
          self.rate_limit_remaining = r.headers['X-Ratelimit-Remaining']
        if 'X-Ratelimit' in r.headers:
          self.rate_limit = r.headers['X-Ratelimit']
        print('API rate_limit:', self.rate_limit_remaining, '/', self.rate_limit, file=sys.stdout)
      return r
    for arg in argv:
      self.segments.append(str(arg))
    return self


if __name__ == "__main__":
  main()
