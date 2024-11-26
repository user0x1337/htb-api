from typing import TYPE_CHECKING

from . import htb

if TYPE_CHECKING:
    pass


class Category(htb.HTBObject):
    """The class representing Hack The Box Challenge Category

    Attributes:
        id: ID of the category
        name: Name of the category
        icon_url: Icon URL of the category
    """

    id: int
    name: str
    icon_url: str

    def __repr__(self):
        return f"<Category '{self.id}'>"

    def __init__(self, data: dict, client: htb.HTBClient):
        self._client = client
        self.id = int(data["id"])
        self.name = data["name"]
        self.icon_url = data["icon"]
