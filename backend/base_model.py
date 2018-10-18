from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy_mixins import AllFeaturesMixin

Base = declarative_base(name="Model")


class BaseModel(Base, AllFeaturesMixin):
    __abstract__ = True

    @classmethod
    def find(cls, t_id):
        return cls.query.filter(cls.id == t_id).first()
