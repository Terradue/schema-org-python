from typing import Literal
from pydantic import Field
from schemaorg_models.thing import Thing


class Intangible(Thing):
    """
A utility class that serves as the umbrella for a number of 'intangible' things such as quantities, structured values, etc.
    """
    class_: Literal['https://schema.org/Intangible'] = Field(default='https://schema.org/Intangible', alias='class', serialization_alias='class') # type: ignore
