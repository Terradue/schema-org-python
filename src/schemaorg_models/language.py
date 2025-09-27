from typing import Literal
from pydantic import Field
from schemaorg_models.intangible import Intangible


class Language(Intangible):
    """
A sub property of instrument. The language used on this action.
    """
    class_: Literal['https://schema.org/Language'] = Field(default='https://schema.org/Language', alias='http://www.w3.org/2000/01/rdf-schema#Class', serialization_alias='http://www.w3.org/2000/01/rdf-schema#Class') # type: ignore
