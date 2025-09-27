from typing import Literal
from pydantic import AliasChoices, Field
from schemaorg_models.event import Event


class ExhibitionEvent(Event):
    """
Event type: Exhibition event, e.g. at a museum, library, archive, tradeshow, ...
    """
    type_: Literal['https://schema.org/ExhibitionEvent'] = Field('class', alias=AliasChoices('@type', 'https://schema.org/ExhibitionEvent'),serialization_alias='class') # type: ignore
