from flask import request
from flask_restful import Resource
from http import HTTPStatus
from flask_jwt_extended import jwt_required, get_jwt_identity
from marshmallow import ValidationError
from webargs import fields
from webargs.flaskparser import use_kwargs
from models.user import User
from models.recipe import Recipe
from schemas.user import UserSchema
from schemas.recipe import RecipeSchema


user_schema = UserSchema()
user_public_schema = UserSchema(exclude=('email', ))
recipe_list_schema = RecipeSchema(many=True)


class UserListResource(Resource):
    def post(self):
        json_data = request.get_json()
        try:
            data = user_schema.load(data=json_data)
        except ValidationError as err:
            return {'message': 'Validation errors', 'errors': err.messages}, HTTPStatus.BAD_REQUEST
        if User.get_by_username(data.get('username')):
            return {'message': 'username already used'}, HTTPStatus.BAD_REQUEST
        if User.get_by_username(data.get('email')):
            return {'message': 'email already used'}, HTTPStatus.BAD_REQUEST

        user = User(**data)
        user.save()
        data = user_schema.dump(user)
        return data, HTTPStatus.CREATED


class UserResource(Resource):
    @jwt_required(optional=True)
    def get(self, username):
        user = User.get_by_username(username=username)
        if user is None:
            return {'message': 'user not found'}, HTTPStatus.NOT_FOUND

        current_user = get_jwt_identity()
        if current_user == user.id:
            data = user_schema.dump(user)
        else:
            data = user_public_schema.dump(user)
        return data, HTTPStatus.OK


class MeResource(Resource):
    @jwt_required()
    def get(self):
        user = User.get_by_id(id=get_jwt_identity())
        data = user_schema.dump(user)
        return data, HTTPStatus.OK


class UserRecipeListResource(Resource):
    @jwt_required(optional=True)
    @use_kwargs({'visibility': fields.Str(missing='public')}, location='query')
    def get(self, username, visibility):
        user = User.get_by_username(username=username)
        if user is None:
            return {'message': 'User not found'}, HTTPStatus.NOT_FOUND

        current_user = get_jwt_identity()
        if current_user != user.id or visibility not in ['all', 'private']:
            visibility = 'public'
        recipes = Recipe.get_all_by_user(user_id=user.id, visibility=visibility)
        data = recipe_list_schema.dump(recipes)
        return data, HTTPStatus.OK
