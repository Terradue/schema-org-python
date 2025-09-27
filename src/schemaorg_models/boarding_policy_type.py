from typing import Literal
from pydantic import Field
from schemaorg_models.enumeration import Enumeration


class BoardingPolicyType(Enumeration):
    """
A type of boarding policy used by an airline.
    """
    class_: Literal['https://schema.org/BoardingPolicyType'] = Field(default='https://schema.org/BoardingPolicyType', alias='http://www.w3.org/2000/01/rdf-schema#Class', serialization_alias='http://www.w3.org/2000/01/rdf-schema#Class') # type: ignore
