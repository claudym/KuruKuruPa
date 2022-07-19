from flask import Flask
from flask_restful import Api
from flask_migrate import Migrate
from extensions import db, jwt
from resources.token import TokenResource, RefreshResource, RevokeResource, block_list
from resources.user import UserListResource, UserResource, MeResource
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

    @jwt.token_in_blocklist_loader
    def check_if_token_in_blocklist(jwt_header, jwt_payload):
        jti = jwt_payload['jti']
        return jti in block_list


def register_resources(app):
    api = Api(app)
    api.add_resource(RecipeListResource, '/recipes')
    api.add_resource(RecipeResource, '/recipes/<int:recipe_id>')
    api.add_resource(RecipePublishResource, '/recipes/<int:recipe_id>/publish')
    api.add_resource(UserListResource, '/users')
    api.add_resource(UserResource, '/users/<string:username>')
    api.add_resource(MeResource, '/me')
    api.add_resource(TokenResource, '/token')
    api.add_resource(RefreshResource, '/refresh')
    api.add_resource(RevokeResource, '/revoke')


if __name__ == '__main__':
    application = create_app()
    application.run()
