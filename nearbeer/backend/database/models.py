from decimal import ConversionSyntax
import os
from sqlalchemy import Column, String, Integer, Numeric, DateTime, ForeignKey
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
import json


#TODO put this in config file
database_filename = "nearbeer"
#project_dir = os.path.dirname(os.path.abspath(__file__))  # used if file in project dir
database_path = "postgresql://{}@{}/{}".format('postgres','localhost:5432', database_filename)

db = SQLAlchemy()

'''
setup_db(app)
    binds a flask application and a SQLAlchemy service
'''
def setup_db(app):
    '''Setup db'''
    app.config["SQLALCHEMY_DATABASE_URI"] = database_path
    app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
    db.app = app
    db.init_app(app)
    migrate = Migrate(app, db)
'''
db_drop_and_create_all()
    drops the database tables and starts fresh
    can be used to initialize a clean database
    !!NOTE you can change the database_filename variable to have multuple verisons of a database
    uncomment db.drop_all if you want to start with clean db
'''
def db_drop_and_create_all():
    db.drop_all()
    db.create_all()


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
    url = Column(String, nullable=False)
    venue_id = Column(String(25), nullable=False)

    venues = db.relationship ('Venue', backref='beer', lazy=True) #Lazy is default  
    #venues = db.relationship ('Venue', back_populates='beer')  #Use backref one statement vs back_populates in both child and parent.
   

    '''
    insert()
        inserts a new model into a database
        the model must have a unique name
        the model must have a unique id or null id
        EXAMPLE
            beer = Beer(name=req_name, venue_blob=req_venue_blob)
            beer.insert()
    '''
    def insert(self):

        db.session.add(self)
        db.session.commit()

    '''
    delete()
        deletes a model into a database
        the model must exist in the database
        EXAMPLE
            beer = Beer.query.filter(Beer.id == id).one_or_none()
            beer.delete()
    '''
    def delete(self):
        db.session.delete(self)
        db.session.commit()

    '''
    update()
        updates a new model into a database
        the model must exist in the database
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
    beer_id = Column(Integer, ForeignKey('beer.id'))
    #beer = db.relationship ('Beer', back_populates='venues')  #Use backref one statement vs back_populates in both child and parent.

    '''
    insert()
        inserts a new model into a database
        the model must have a unique name
        the model must have a unique id or null id
        EXAMPLE
            beer = Beer(name=req_name, venue_blob=req_venue_blob)
            beer.insert()
    '''
    def insert(self):

        db.session.add(self)
        db.session.commit()

    '''
    delete()
        deletes a model into a database
        the model must exist in the database
        EXAMPLE
            beer = Beer.query.filter(Beer.id == id).one_or_none()
            beer.delete()
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
            venue.name = 'BBQ RoadHouse & Bar'
            venue.update()
    '''
    def update(self):
        db.session.commit()
    
    def format(self):
        return {
            'id': self.id,
            'name': self.name
        }
        
    def __repr__(self):
        return json.dumps(self.format()) 
