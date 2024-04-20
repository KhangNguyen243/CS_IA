# -*- coding: utf-8 -*-
"""User models."""
import datetime as dt

from flask_login import UserMixin
from sqlalchemy.ext.hybrid import hybrid_property

from stock_management.database import Column, PkModel, db, reference_col, relationship
from stock_management.extensions import bcrypt


class Tool (UserMixin, PkModel):
    """A user of the app."""

    __tablename__ = "tool"
    type = db.Column(db.String(10), nullable=False)
    nodel = db.Column(db.String(20), nullable=False)
    quantity = db.Column(db.Integer, nullable=False)
    price = db.Column(db.Integer, nullable=False)