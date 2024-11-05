from typing import TYPE_CHECKING

from . import htb

if TYPE_CHECKING:
    pass


class Notice(htb.HTBObject):
    """The class representing Hack The Box Notice

    Attributes:
        id: ID of the notice
        type: Type of the notice
        message: Message of the notice
        url: URL of the notice
        url_exact: Exact url of the notice
        dismissible: Is notice dismissible?
    """

    id: int
    type: str
    message: str
    url: str
    url_exact: bool
    dismissible: bool

    def __repr__(self):
        return f"<Notice '{self.id}'>"

    def __init__(self, data: dict, client: htb.HTBClient):
        self._client = client
        self.id = int(data["id"])
        self.type = data["type"]
        self.message = data["message"]
        self.url = data["url"]
        self.url_exact = data["url_exact"]
        self.dismissible = data["dismissible"]