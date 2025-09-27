from typing import Literal
from pydantic import Field
from schemaorg_models.organization import Organization


class Cooperative(Organization):
    """
An organization that is a joint project of multiple organizations or persons.
    """
    class_: Literal['https://schema.org/Cooperative'] = Field(default='https://schema.org/Cooperative', alias='http://www.w3.org/2000/01/rdf-schema#Class', serialization_alias='http://www.w3.org/2000/01/rdf-schema#Class') # type: ignore
