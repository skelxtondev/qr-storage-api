from marshmallow import Schema, fields


class PlainItemSchema(Schema):
    Iid = fields.Int(dump_only=True)
    name = fields.Str(required=True)
    amount = fields.Int(required=True)


class PlainContainerSchema(Schema):
    id = fields.Int(dump_only=True)
    name = fields.Str(required=True)


class ItemSchema(PlainItemSchema):
    container_id = fields.Int(required=True, load_only=True)
    container = fields.Nested(PlainContainerSchema(), dump_only=True)


class ContainerSchema(PlainContainerSchema):
    items = fields.List(fields.Nested(PlainItemSchema()), dump_only=True)


class ItemUpdateSchema(Schema):
    name = fields.Str()
    amount = fields.Float()
    container_id = fields.Int()
