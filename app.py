from flask import Flask 
from flask_migrate import Migrate 
from flask_restful import Api

from config import Config 
from extensions import db
from resources.recipe import RecipeResourceList, RecipeResource, RecipeResourcePublish
from resources.user import UserListResource

def create_app():
	app = Flask(__name__)
	#app.config.from_object(Config)
	app.config['DEBUG'] = True
	#name deve ser o nome do Role e pass a senha
	app.config['SQLALCHEMY_DATABASE_URI'] = "postgresql+psycopg2://name:pass@localhost/smilecook"
	app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

	register_extensions(app)
	register_resources(app)

	return app

def register_extensions(app):
	db.init_app(app)
	mirate = Migrate(app, db)

def register_resources(app):
	api = Api(app)

	api.add_resource(RecipeResourceList, '/recipes')
	api.add_resource(RecipeResource, '/recipes/<int:recipe_id>')
	api.add_resource(RecipeResourcePublish, '/recipes/<int:recipe_id>/publish')
	api.add_resource(UserListResource, '/users')

if __name__ == '__main__':
	app = create_app()
	app.run()
