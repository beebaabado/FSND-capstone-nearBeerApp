'''
'''
import os
import json
from sqlalchemy import Column, String, Integer, Numeric, DateTime
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate

# TODO put this in config file
# database_filename = "nearbeer"
# # #project_dir = os.path.dirname(os.path.abspath(__file__))  # used if file in project dir
#database_path = "postgresql://{}@{}/{}".format('postgres','localhost:5432', database_filename)
#database_path = ""
db = SQLAlchemy()
migrate = Migrate()

'''
setup_db(app)
    binds a flask application and a SQLAlchemy service
'''
def setup_db(app, db_path=""):
    '''Setup db'''
    if db_path=="":
        if app.config['TESTING'] is True:
            db_path= app.config['DATABASE_URI_TEST']
            print(f"DATABASE:  {app.config['DATABASE_URI_TEST']}")
            #print(f"DATABASE:  {app.config['SQLALCHEMY_DATABASE_URI_TEST']}")
        else:
            db_path = app.config["DATABASE_URI"]
            #print(f"DATABASE:  {app.config['SQLALCHEMY_DATABASE_URI']}")
    app.config["SQLALCHEMY_DATABASE_URI"] = db_path
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

''' BeerModel class
    Use as base class all nearbeer classes
'''
class BeerModel(db.Model):
    __abstract__ = True

    '''
    insert()
        inserts a new item into database
    '''
    def insert(self):
        db.session.add(self)
        db.session.commit()

    '''
    delete()
        deletes an exisitng model from the database
    '''
    def delete(self):
        db.session.delete(self)
        db.session.commit()

    '''
    update()
        updates an existing model in databaes
    '''
    def update(self):
        db.session.commit()
    
    def format(self):
        return {
          'error': "must override in child class"
        }
        
    def __repr__(self):
        return json.dumps(self.format())


'''
BeerVenue
  association table representing all possible connections between beers and Venues
'''
class BeerVenue(BeerModel):
    __tablename__='beervenue'
    venue_id =  db.Column( db.Integer, db.ForeignKey('venue.id'), primary_key=True)
    beer_id = db.Column( db.Integer, db.ForeignKey('beer.id'), primary_key=True)

    # Create relationships to beer and venue
    beer = db.relationship("Beer", back_populates="venues")
    venue = db.relationship("Venue", back_populates="beers")
    
    def format(self):
        return {
            'venue_id': self.venue_id,
            'beer_id': self.beer_id
        }

'''
Beer
   a persistent beer entity, extends the base SQLAlchemy Model
'''
class Beer(BeerModel):
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

    def format(self):
        return {
            'id': self.id,
            'name': self.name,
            'bid' : self.bid,
            'brewery_name' : self.brewery_name,
            'brewery_slug' : self.brewery_slug,
            'abv': str(self.abv),
            'url': "https://untappd.com/b" + "/" + self.brewery_slug + self.slug + "/" + self.bid,
            'style': self.style,
            'major_style' : self.major_style,
            'rating': str(self.rating),
            'user_rating': str(self.user_rating),
            'last_seen' : self.last_seen,
            'venue_id': self.venue_id
        }
'''
Venue
'''        
class Venue(BeerModel):
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

'''
Style
'''        
class Style(BeerModel):
    ''' 
    Representation of beer major style and posbbile sub styles
    '''
    __tablename__ = 'style'
    id = Column(Integer, primary_key=True)
    major = Column(String(25), unique=True, nullable=False)
    sub_styles = Column(String, nullable=False)
    
    def format(self):
        return {
            'id': self.id,
            'major': self.major,
            'sub_styles': self.sub_styles
        }
 
