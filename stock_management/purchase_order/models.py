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

    __tablename__ = "purchase_order"
    ID_PurchaseOrder = db.Column(db.Integer, primary_key=True, nullable=False)
    ID_Location = db.Column(db.Integer, db.ForeignKey('locations.id'), nullable=False)  # Assuming there's a 'Location' table
    OrderDate = db.Column(db.Date, nullable=False)

    # Relationship with OrderDetail table (one-to-many)
    order_details = db.relationship('OrderDetail', backref='purchase_order', lazy=True)

    @hybrid_property
    def password(self):
        """Hashed password."""
        return self._password

    @password.setter
    def password(self, value):
        """Set password."""
        self._password = bcrypt.generate_password_hash(value)

    def check_password(self, value):
        """Check password."""
        return bcrypt.check_password_hash(self._password, value)

    @property
    def full_name(self):
        """Full user name."""
        return f"{self.first_name} {self.last_name}"

    def __repr__(self):
        """Represent instance as a unique string."""
        return f"<User({self.username!r})>"
