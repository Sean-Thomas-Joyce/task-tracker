from datetime import date, datetime
from enum import Enum


def custom_encoder(obj: object):
    if isinstance(obj, Enum):
        return obj.name
    if isinstance(obj, (datetime, date)):
        return obj.isoformat()
    raise TypeError(f"Type {type(obj)} not serializable")
