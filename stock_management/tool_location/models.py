# -*- coding: utf-8 -*-
"""User models."""
import datetime as dt

from flask_login import UserMixin
from sqlalchemy.ext.hybrid import hybrid_property

from stock_management.database import Column, PkModel, db, reference_col, relationship
from stock_management.extensions import bcrypt

class ToolLocation(UserMixin, PkModel):
    """A user of the app."""

    __tablename__ = "tool_location"
    ID_Tools = db.Column(db.Integer, primary_key=True, nullable=False)
    ID_Location = db.Column(db.Integer, primary_key=True, nullable=False)
    Quantity = db.Column(db.Integer, nullable=False)
    Price = db.Column(db.Integer, nullable=False)
    Status = db.Column(db.String(10), nullable=False)
    EstDate = db.Column(db.Date, nullable=False)

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
