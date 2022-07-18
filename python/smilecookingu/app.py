from flask import Flask
from flask_restful import Api
from flask_migrate import Migrate
from extensions import db, jwt
from resources.user import UserListResource
from resources.recipe import RecipeListResource, RecipeResource, RecipePublishResource


def create_app():
    app = Flask(__name__)
    app.config.from_object('config.Config.DevelopmentConfig')
    register_extensions(app)
    register_resources(app)
    return app


def register_extensions(app):
    db.init_app(app)
    Migrate(app, db)
    jwt.init_app(app)


def register_resources(app):
    api = Api(app)
    api.add_resource(RecipeListResource, '/recipes')
    api.add_resource(RecipeResource, '/recipes/<int:recipe_id>')
    api.add_resource(RecipePublishResource, '/recipes/<int:recipe_id>/publish')
    api.add_resource(UserListResource, '/users')


if __name__ == '__main__':
    application = create_app()
    application.run()
