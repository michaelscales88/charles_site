# services/tasks.py
from json import loads
from flask_sqlalchemy import Model
from sqlalchemy.inspection import inspect
from backend.base_model import BaseModel


def to_list(value):
    return loads(value)


def to_bool(value):
    return loads(value) is True


def get_model_by_tablename(tablename):
    for c in BaseModel._decl_class_registry.values():
        if hasattr(c, '__tablename__') and c.__tablename__ == tablename:
            return c


def get_model_headers(model_name=None):
    model = get_model_by_tablename(model_name)
    return list(model.headers) if model else None


def get_pk(table):
    return inspect(table).primary_key[0].name


def get_foreign_id(query_obj, column_name):
    if isinstance(query_obj, Model):
        return getattr(query_obj, column_name, None)
    if isinstance(query_obj, dict):
        return query_obj.get(column_name)
