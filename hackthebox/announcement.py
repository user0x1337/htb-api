from datetime import datetime
from typing import TYPE_CHECKING

import dateutil.parser

from . import htb

if TYPE_CHECKING:
    pass


class Announcement(htb.HTBObject):
    """The class representing Hack The Box Announcement

    Attributes:
        id: ID of the announcement
        title: Title of the announcement
        updated_at: Date/Time of the announcement
        created_at: Creation date of the announcement
    """

    id: int
    title: str
    updated_at: datetime
    created_at: datetime

    def __repr__(self):
        return f"<Announcement '{self.id}'>"

    def __init__(self, data: dict, client: htb.HTBClient):
        self._client = client
        self.id = int(data["id"])
        self.title = data["title"]
        self.updated_at = dateutil.parser.parse(data["updated_at"])
        self.created_at = dateutil.parser.parse(data["created_at"])