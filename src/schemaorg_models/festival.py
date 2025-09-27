from typing import Literal
from pydantic import Field
from schemaorg_models.event import Event


class Festival(Event):
    """
Event type: Festival.
    """
    type_: Literal['https://schema.org/Festival'] = Field(default='https://schema.org/Festival', alias='@type', serialization_alias='@type') # type: ignore
