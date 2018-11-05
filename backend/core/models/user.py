# security/models.py
import datetime
from flask_security import UserMixin
from ...extensions import db
from .roles import RolesModel

roles_users = db.Table(
    'roles_users',
    db.Column('user_id', db.Integer(), db.ForeignKey('user.id')),
    db.Column('role_id', db.Integer(), db.ForeignKey('role.id'))
)


class UserModel(db.Model, UserMixin):
    __tablename__ = "user"
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(255), unique=True)
    email = db.Column(db.String(255), unique=True)
    password = db.Column(db.String(255))
    active = db.Column(db.Boolean(), default=True)
    confirmed_at = db.Column(db.DateTime(), default=datetime.datetime.utcnow())

    roles = db.relationship(RolesModel, secondary=roles_users,
                            backref=db.backref('users', lazy='dynamic'))

    def __str__(self):
        return "{}".format(self.username)
