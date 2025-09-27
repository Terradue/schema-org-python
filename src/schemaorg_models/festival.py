from typing import Literal
from pydantic import AliasChoices, Field
from schemaorg_models.event import Event


class Festival(Event):
    """
Event type: Festival.
    """
    type_: Literal['https://schema.org/Festival'] = Field('class', alias=AliasChoices('@type', 'https://schema.org/Festival'),serialization_alias='class') # type: ignore
