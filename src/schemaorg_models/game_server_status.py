from typing import Literal
from pydantic import Field
from schemaorg_models.status_enumeration import StatusEnumeration


class GameServerStatus(StatusEnumeration):
    """
Status of a game server.
    """
    type_: Literal['https://schema.org/GameServerStatus'] = Field(default='https://schema.org/GameServerStatus', alias='@type', serialization_alias='@type') # type: ignore
