from flask import Flask
from flask_restful import Api
from flask_migrate import Migrate
from config import Config
from extensions import db
from models.user import User
from resources.recipe import RecipeListResource, RecipeResource, RecipePublishResource

app = Flask(__name__)
api = Api(app)

api.add_resource(RecipeListResource, '/recipes')
api.add_resource(RecipeResource, '/recipes/<int:recipe_id>')
api.add_resource(RecipePublishResource, '/recipes/<int:recipe_id>/publish')

if __name__ == '__main__':
    app.run(port=5000, debug=True)
