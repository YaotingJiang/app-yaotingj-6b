from flask_mongoengine import MongoEngine
from services.dogWalkerService import init_dog_walkers
from services.dogOwnerService import init_dog_owners
from services.routeService import init_routes

db = MongoEngine()

def initialize_db(app):
    db.init_app(app)
    init_dog_walkers()
    init_dog_owners()
    init_routes()

def fetch_engine():
    return db