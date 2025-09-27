from typing import Literal
from pydantic import AliasChoices, Field
from schemaorg_models.quantity import Quantity


class Duration(Quantity):
    """
The duration of the item (movie, audio recording, event, etc.) in [ISO 8601 duration format](http://en.wikipedia.org/wiki/ISO_8601).
    """
    type_: Literal['https://schema.org/Duration'] = Field('class', alias=AliasChoices('@type', 'https://schema.org/Duration'),serialization_alias='class') # type: ignore
