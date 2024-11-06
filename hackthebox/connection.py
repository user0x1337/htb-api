from typing import TYPE_CHECKING

from . import htb

if TYPE_CHECKING:
    pass


class ConnectionServer(htb.HTBObject):
    """The class representing Hack The Box Connection Server

        Attributes:
            id: ID of the connection (referencing the VPN server)
            hostname: hostname of the connection
            port: port of the connection
            friendly_name: friendly name of the connection
        """

    id: int
    hostname: str
    port: int
    friendly_name: str

    def __init__(self, data: dict, client: htb.HTBClient):
        self._client = client
        self.id = int(data["id"])
        self.hostname = data["hostname"]
        self.port = int(data["port"])
        self.friendly_name = data["friendly_name"]

    def __repr__(self):
        return f"<Connection Status '{self.friendly_name}'>"

    def __str__(self):
        return f"{self.friendly_name}"


class ConnectionDetails(htb.HTBObject):
    """The class representing Hack The Box Connection details

        Attributes:
            name: Username which established the connection
            ip4: IP4-Address of the connection
            ip6: IP6-Address of the connection

        """

    name: str
    ip4: str
    ip6: str

    def __init__(self, data: dict, client: htb.HTBClient):
        self._client = client
        self.name = data["name"]
        self.ip4 = data["ip4"]
        self.ip6 = data["ip6"]


    def __repr__(self):
        return f"<Connection Details '{self.ip4}'>"

    def __str__(self):
        return f"{self.self.ip4}"

class ConnectionStatus(htb.HTBObject):
    """The class representing Hack The Box Connection status

    Attributes:
        type: Type of the connection
        location_friendly_name: Friendly name of the connection
        connection_server: Info of the connected server
        connection_details: Connection details
    """

    type: str
    location_type_friendly: str
    connection_server: ConnectionServer
    connection_details: ConnectionDetails

    def __init__(self,
                 data: dict,
                 client: htb.HTBClient,
                 connection_server: ConnectionServer,
                 connection_details: ConnectionDetails):
        assert data is not None

        self._client = client
        self.type = data["type"]
        self.location_type_friendly = data["location_type_friendly"]
        self.connection_details = connection_details
        self.connection_server = connection_server

    def __repr__(self):
        return f"<Connection Status '{self.location_type_friendly}'>"

    def __str__(self):
        return f"{self.location_type_friendly}"
