from typing import Literal
from pydantic import AliasChoices, Field
from schemaorg_models.thing import Thing


class Intangible(Thing):
    """
A utility class that serves as the umbrella for a number of 'intangible' things such as quantities, structured values, etc.
    """
    type_: Literal['https://schema.org/Intangible'] = Field('class', alias=AliasChoices('@type', 'https://schema.org/Intangible'),serialization_alias='class') # type: ignore
