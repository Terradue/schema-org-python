from typing import Literal
from pydantic import Field
from schemaorg_models.quantity import Quantity


class Duration(Quantity):
    """
The duration of the item (movie, audio recording, event, etc.) in [ISO 8601 duration format](http://en.wikipedia.org/wiki/ISO_8601).
    """
    class_: Literal['https://schema.org/Duration'] = Field(default='https://schema.org/Duration', alias='@type', serialization_alias='@type') # type: ignore
