''' Manage.py  
    To manage database schema via migrations
'''
from flask_script import Manager
from flask_migrate import Migrate, MigrateCommand
import database.models as model
from beer_server import create_app

app = create_app()
migrate = Migrate(app, model.db)
manager = Manager(app)
manager.add_command('db', MigrateCommand)

if __name__ == '__main__':
    manager.run()
