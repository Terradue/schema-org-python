from typing import Literal
from pydantic import Field
from schemaorg_models.audience import Audience


class Researcher(Audience):
    """
Researchers.
    """
    type_: Literal['https://schema.org/Researcher'] = Field(default='https://schema.org/Researcher', alias='@type', serialization_alias='http://www.w3.org/2000/01/rdf-schema#/Class') # type: ignore
