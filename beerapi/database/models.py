from decimal import ConversionSyntax
import os
from sqlalchemy import Column, String, Integer, Numeric, DateTime, ForeignKey
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
import json


#TODO put this in config file
database_filename = "nearbeer"
# #project_dir = os.path.dirname(os.path.abspath(__file__))  # used if file in project dir
database_path = "postgresql://{}@{}/{}".format('postgres','localhost:5432', database_filename)


db = SQLAlchemy()
migrate = Migrate()

'''
setup_db(app)
    binds a flask application and a SQLAlchemy service
'''
def setup_db(app, database_path=""):
    '''Setup db'''
    if database_path=="":
        database_path=app.config["SQLALCHEMY_DATABASE_URI"] 
    # app.config["SQLALCHEMY_DATABASE_URI"] = database_path
    # app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
    db.app = app
    db.init_app(app)
    migrate.init_app(app, db)
'''
db_drop_and_create_all()
    drops the database tables and starts fresh
    can be used to initialize a clean database
    !!NOTE you can change the database_filename variable to have multuple verisons of a database
    uncomment db.drop_all if you want to start with clean db
'''
def db_drop_and_create_all():
    ''' drop and create '''
    db.drop_all()
    db.create_all()

'''
BeerVenue
  association table representing all possible connections between beers and Venues
'''
class BeerVenue(db.Model):
    __tablename__='beervenue'
    venue_id =  db.Column( db.Integer, db.ForeignKey('venue.id'), primary_key=True)
    beer_id = db.Column( db.Integer, db.ForeignKey('beer.id'), primary_key=True)

    # Create relationships to beer and venue
    beer = db.relationship("Beer", back_populates="venues")
    venue = db.relationship("Venue", back_populates="beers")

    def __repr__(self):
       return f'<BeerVenue:  {self.venue_id}, {self.beer_id}>'

'''
Beer
   a persistent beer entity, extends the base SQLAlchemy Model
'''
class Beer(db.Model):
    __tablename__ = 'beer'
    id = Column(Integer, primary_key=True)
    abv = Column(Numeric(3,1), nullable=False)
    name = Column(String(80), nullable=False)
    slug = Column(String, nullable=False)
    style = Column(String(80), nullable=False) 
    bid = Column(String(25), nullable=False)
    brewery_name = Column(String(80), nullable=False)
    brewery_slug = Column(String, nullable=False)
    last_seen = Column(DateTime, nullable=False)
    major_style = Column(String(80), nullable=False)
    rating = Column(Numeric(3,2),  nullable=False)
    user_rating = Column(Numeric(3,2), nullable=True, default=0.00)
    url = Column(String, nullable=False)
    venue_id = Column(String, nullable=False)
    # child relationship setup
    venues = db.relationship ('BeerVenue', back_populates='beer') 

    '''
    insert()
        inserts a new beer into a database
        the beer  must have a unique name
        the beer must have a unique id, cannot be null
        EXAMPLE
            beer = Beer(name=req_name)
            beer.insert()
    '''
    def insert(self):

        db.session.add(self)
        db.session.commit()

    '''
    delete()
        deletes an exisitng beer from the database
        EXAMPLE
            beer = Beer.query.filter(Beer.id == id).one_or_none()
            beer.delete()
    '''
    def delete(self):
        db.session.delete(self)
        db.session.commit()

    '''
    update()
        updates an existing beer in the database
        EXAMPLE
            beer = Beer.query.filter(Beer.id == id).one_or_none()
            beer.name = 'Chocolate Coffee Stout'
            beer.update()
    '''
    def update(self):
        db.session.commit()
    
    def format(self):
        return {
            'id': self.id,
            'name': self.name,
            'abv': str(self.abv),
            'url': "https://untappd.com/b" + "/" + self.brewery_slug + self.slug + "/" + self.bid,
            'style': self.style,
            'rating': str(self.rating),
            'user_rating': str(self.user_rating),
            'venue_id': self.venue_id
        }
        
    def __repr__(self):
        return json.dumps(self.format())

class Venue(db.Model):
    __tablename__ = 'venue'
    id = Column(Integer, primary_key=True)
    venue_id = Column(String(25), unique=True, nullable=False)
    name = Column(String(80), nullable=False)
    slug = Column(String, nullable=False)
    lng = Column(Numeric(10,7), nullable=False)
    lat = Column(Numeric(10,7), nullable=False)
    city = Column(String(80), nullable=False)
    state = Column(String(2), nullable=False)
    address = Column(String, nullable=False)
    country = Column(String(80), nullable=False)
    # the venue blob - this stores a lazy json blob for venue menu, optional field
    #  TODO DEFINE the required datatype is [{'venue': string, 'id':string, '???':number}]
    venue_blob =  Column(String(180), nullable=True, default='No Menu Available.')

    # child relationship setup
    beers = db.relationship ('BeerVenue', back_populates='venue')  
    
    '''
    insert()
        inserts a new venue into the database
        the model must have a unique name
        the model must have a unique id, not null
        EXAMPLE
            venue = Venue(venue_id=req_venue_id, 
                          name=venue_name, 
                          slug=venue_slug,
                          lng=venue_lng,
                          lat=venue_lat,
                          city=venue_city,
                          state=venue_city,
                          address=venue_address)
            venue.insert()
    '''
    def insert(self):

        db.session.add(self)
        db.session.commit()

    '''
    delete()
        deletes an exisitn venue from database
        EXAMPLE
            venue = Venue.query.filter(Venue.id == id).one_or_none()
            venue.delete()
    '''
    def delete(self):
        db.session.delete(self)
        db.session.commit()

    '''
    update()
        updates a new model into a database
        the model must exist in the database
        EXAMPLE
            venue = Venue.query.filter(Venue.id == id).one_or_none()
            venue.name = new_venue_name
            venue.update()
    '''
    def update(self):
        db.session.commit()
    
    def format(self):
        return {
            'id': self.id,
            'venue_id': self.venue_id,
            'name': self.name,
            'slug': self.slug,
            'lat': str(self.lat),
            'lng': str(self.lng),
            'address': self.address,
            'city': self.city,
            'state': self.state,
            'country': self.country,
            'blob': self.venue_blob
        }
        
    def __repr__(self):
        return json.dumps(self.format()) 


class Style(db.Model):
    ''' 
    Representation of beer major style and posbbile sub styles
    '''
    __tablename__ = 'style'
    id = Column(Integer, primary_key=True)
    major = Column(String(25), unique=True, nullable=False)
    sub_styles = Column(String, nullable=False)
    
    '''
    insert()
        inserts a new style into the database
        the style must have a unique major name
        the style must have a unique id or null id
        EXAMPLE
            style = Style(major=req_major, sub_styles=list_of_sub_styles)
            style.insert()
    '''
    def insert(self):
        db.session.add(self)
        db.session.commit()

    '''
    delete()
        deletes a style from the database
        the model must exist in the database
        EXAMPLE
            style = Style.query.filter(Style.id == id).one_or_none()
            style.delete()
    '''
    def delete(self):
        db.session.delete(self)
        db.session.commit()

    '''
    update()
        updates exisitng style in the database
        EXAMPLE
            style = Style.query.filter(Style.id == id).one_or_none()
            style.major = 'Sour'
            style.substyles = 'Sour', 'Gose'
            style.update()
    '''
    def update(self):
        db.session.commit()
    
    def format(self):
        return {
            'id': self.id,
            'major': self.major,
            'sub_styles': self.sub_styles
        }
        
    def __repr__(self):
        return json.dumps(self.format()) 
