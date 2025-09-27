from typing import Literal
from pydantic import Field
from schemaorg_models.enumeration import Enumeration


class MedicalEnumeration(Enumeration):
    """
Enumerations related to health and the practice of medicine: A concept that is used to attribute a quality to another concept, as a qualifier, a collection of items or a listing of all of the elements of a set in medicine practice.
    """
    type_: Literal['https://schema.org/MedicalEnumeration'] = Field(default='https://schema.org/MedicalEnumeration', alias='@type', serialization_alias='http://www.w3.org/2000/01/rdf-schema#/Class') # type: ignore
