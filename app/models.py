from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy_mixins import AllFeaturesMixin

Base = declarative_base(name="Model")


class BaseModel(Base, AllFeaturesMixin):
    __abstract__ = True
