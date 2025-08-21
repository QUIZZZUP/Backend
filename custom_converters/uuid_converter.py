import uuid

from werkzeug.routing import BaseConverter


class UUIDConverter(BaseConverter):
    def __init__(self, url_map):
        super(UUIDConverter, self).__init__(url_map)

    def to_python(self, value):
        try:
            return uuid.UUID(value)
        except ValueError:
            raise ValueError(f"{value} is not a valid UUID")

    def to_url(self, value):
        return str(value)