from typing import Literal
from pydantic import Field
from schemaorg_models.medical_enumeration import MedicalEnumeration


class InfectiousAgentClass(MedicalEnumeration):
    """
Classes of agents or pathogens that transmit infectious diseases. Enumerated type.
    """
    class_: Literal['https://schema.org/InfectiousAgentClass'] = Field(default='https://schema.org/InfectiousAgentClass', alias='http://www.w3.org/2000/01/rdf-schema#Class', serialization_alias='http://www.w3.org/2000/01/rdf-schema#Class') # type: ignore
