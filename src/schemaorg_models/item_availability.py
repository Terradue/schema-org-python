from typing import Literal
from pydantic import Field
from schemaorg_models.enumeration import Enumeration


class ItemAvailability(Enumeration):
    """
A list of possible product availability options.
    """
    class_: Literal['https://schema.org/ItemAvailability'] = Field(default='https://schema.org/ItemAvailability', alias='http://www.w3.org/2000/01/rdf-schema#Class', serialization_alias='http://www.w3.org/2000/01/rdf-schema#Class') # type: ignore
