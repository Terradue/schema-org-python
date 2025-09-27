from typing import Literal
from pydantic import Field
from schemaorg_models.event import Event


class ExhibitionEvent(Event):
    """
Event type: Exhibition event, e.g. at a museum, library, archive, tradeshow, ...
    """
    class_: Literal['https://schema.org/ExhibitionEvent'] = Field('class', alias='class', serialization_alias='class') # type: ignore
