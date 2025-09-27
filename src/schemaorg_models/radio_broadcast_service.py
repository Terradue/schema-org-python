from typing import Literal
from pydantic import Field
from schemaorg_models.broadcast_service import BroadcastService


class RadioBroadcastService(BroadcastService):
    """
A delivery service through which radio content is provided via broadcast over the air or online.
    """
    class_: Literal['https://schema.org/RadioBroadcastService'] = Field(default='https://schema.org/RadioBroadcastService', alias='http://www.w3.org/2000/01/rdf-schema#Class', serialization_alias='http://www.w3.org/2000/01/rdf-schema#Class') # type: ignore
