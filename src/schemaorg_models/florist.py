from typing import Literal
from pydantic import Field
from schemaorg_models.store import Store


class Florist(Store):
    """
A florist.
    """
    class_: Literal['https://schema.org/Florist'] = Field(default='https://schema.org/Florist', alias='http://www.w3.org/2000/01/rdf-schema#Class', serialization_alias='http://www.w3.org/2000/01/rdf-schema#Class') # type: ignore
