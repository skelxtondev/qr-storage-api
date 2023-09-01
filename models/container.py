from db import db


class ContainerModel(db.Model):
    __tablename__ = "containers"

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80), unique=True, nullable=False)
    items = db.relationship("ItemModel", back_populates="container", lazy="dynamic")