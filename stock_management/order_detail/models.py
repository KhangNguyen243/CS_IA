# -*- coding: utf-8 -*-
"""User models."""
import datetime as dt

from flask_login import UserMixin
from sqlalchemy.ext.hybrid import hybrid_property

from stock_management.database import Column, PkModel, db, reference_col, relationship
from stock_management.extensions import bcrypt


class Role(PkModel):
    """A role for a user."""

    __tablename__ = "roles"
    name = Column(db.String(80), unique=True, nullable=False)
    user_id = reference_col("users", nullable=True)
    user = relationship("User", backref="roles")

    def __init__(self, name, **kwargs):
        """Create instance."""
        super().__init__(name=name, **kwargs)

    def __repr__(self):
        """Represent instance as a unique string."""
        return f"<Role({self.name})>"


class User(UserMixin, PkModel):
    """A user of the app."""

    __tablename__ = "order_details"
    ID_OrderDetail = db.Column(db.Integer, primary_key=True, nullable=False)
    ID_Tools = db.Column(db.Integer, db.ForeignKey('tools.ID'), nullable=False)  # Assuming there's a 'Tools' table
    ID_PurchaseOrder = db.Column(db.Integer, db.ForeignKey('purchase_order.ID_PurchaseOrder'), nullable=False)
    Quantity = db.Column(db.Integer, nullable=False)
    Price = db.Column(db.Integer, nullable=False)

