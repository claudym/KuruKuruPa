from marshmallow import Schema, fields, post_dump, validate, validates, ValidationError
from flask import url_for
from schemas.user import UserSchema


class RecipeSchema(Schema):
    class Meta:
        ordered = True

    @validates('cook_time')
    def validate_cook_time(self, value):
        if value < 1:
            raise ValidationError('Cook time must be greater than 0')
        if value > 6000:
            raise ValidationError('Cook time must be less than 6000 minutes')

    def validate_num_of_servings(n):
        if n < 1:
            raise ValidationError('Servings have to be at least 1')
        if n > 10000:
            raise ValidationError('Servings cannot be greater that 10,000')

    @post_dump(pass_many=True)
    def wrap(self, data, many, **kwargs):
        if many:
            return {'data': data}
        return data

    id = fields.Int(dump_only=True)
    name = fields.Str(required=True, validate=[validate.Length(max=100)])
    description = fields.Str(validate=[validate.Length(max=200)])
    directions = fields.Str(validate=[validate.Length(max=200)])
    is_publish = fields.Boolean(dump_only=True)
    created_at = fields.DateTime(dump_only=True)
    updated_at = fields.DateTime(dump_only=True)
    num_of_servings = fields.Int(validate=validate_num_of_servings)
    cook_time = fields.Int()
    author = fields.Nested(UserSchema, attribute='user', dump_only=True, only=['id', 'username'])
    cover_url = fields.Method(serialize='dump_cover_url')


    def dump_cover_url(self, recipe):
        if recipe.cover_image:
            return url_for('static', filename=f'images/recipes/{recipe.cover_image}', _external=True)
