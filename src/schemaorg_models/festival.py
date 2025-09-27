from typing import Literal
from pydantic import Field
from schemaorg_models.event import Event


class Festival(Event):
    """
Event type: Festival.
    """
    class_: Literal['https://schema.org/Festival'] = Field('class', alias='class', serialization_alias='class') # type: ignore
