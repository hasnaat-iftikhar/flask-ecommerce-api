from marshmallow import Schema, fields, validate, validates_schema, ValidationError
from app.models.product import Product

class ProductSchema(Schema):
    id = fields.Int(dump_only=True)
    name = fields.Str(
        required=True,
        validate=[
            validate.Length(min=1, max=100, error="Name must be 1-100 characters"),
            validate.Regexp(r"^[a-zA-Z0-9 ]+$", error="Only letters, numbers, and spaces allowed")
        ]
    )
    price = fields.Float(
        required=True,
        validate=validate.Range(min=0.01)
    )
    stock = fields.Int(
        required=True,
        validate=validate.Range(min=0)
    )
    category = fields.Str(
        validate=validate.OneOf(["electronics", "clothing", "books", "general"])
    )
    is_active = fields.Bool(dump_only=True)
    created_at = fields.DateTime(dump_only=True)

    @validates_schema
    def validate_name_uniqueness(self, data, **kwargs):
        if Product.query.filter(Product.name.ilike(data["name"])).first():
            raise ValidationError("Product name already exists", "name")