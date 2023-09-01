from sqlalchemy import ForeignKey
from db import db


class ItemModel(db.Model):
    __tablename__ = "items"

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80), unique=False, nullable=False)
    description = db.Column(db.String)
    amount = db.Column(db.Integer, unique=False, nullable=False)

    container_id = db.Column = db.Column(db.Integer, db.ForeignKey("containers.id"), unique=False, nullable=False)
    container = db.relationship("ContainerModel", back_populates="items")
