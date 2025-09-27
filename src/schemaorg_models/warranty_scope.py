from typing import Literal
from pydantic import Field
from schemaorg_models.enumeration import Enumeration


class WarrantyScope(Enumeration):
    """
The scope of the warranty promise.
    """
    class_: Literal['https://schema.org/WarrantyScope'] = Field(default='https://schema.org/WarrantyScope', alias='http://www.w3.org/2000/01/rdf-schema#Class', serialization_alias='http://www.w3.org/2000/01/rdf-schema#Class') # type: ignore
