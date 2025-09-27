from typing import Literal
from pydantic import Field
from schemaorg_models.organization import Organization


class PerformingGroup(Organization):
    """
A performance group, such as a band, an orchestra, or a circus.
    """
    class_: Literal['https://schema.org/PerformingGroup'] = Field(default='https://schema.org/PerformingGroup', alias='http://www.w3.org/2000/01/rdf-schema#Class', serialization_alias='http://www.w3.org/2000/01/rdf-schema#Class') # type: ignore
