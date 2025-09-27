from typing import Literal
from pydantic import Field
from schemaorg_models.enumeration import Enumeration


class ReturnFeesEnumeration(Enumeration):
    """
Enumerates several kinds of policies for product return fees.
    """
    class_: Literal['https://schema.org/ReturnFeesEnumeration'] = Field(default='https://schema.org/ReturnFeesEnumeration', alias='http://www.w3.org/2000/01/rdf-schema#Class', serialization_alias='http://www.w3.org/2000/01/rdf-schema#Class') # type: ignore
