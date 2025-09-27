from typing import Literal
from pydantic import Field
from schemaorg_models.audience import Audience


class Researcher(Audience):
    """
Researchers.
    """
    class_: Literal['https://schema.org/Researcher'] = Field(default='https://schema.org/Researcher', alias='http://www.w3.org/2000/01/rdf-schema#Class', serialization_alias='http://www.w3.org/2000/01/rdf-schema#Class') # type: ignore
