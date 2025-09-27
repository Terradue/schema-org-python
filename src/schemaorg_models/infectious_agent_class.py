from typing import Literal
from pydantic import Field
from schemaorg_models.medical_enumeration import MedicalEnumeration


class InfectiousAgentClass(MedicalEnumeration):
    """
Classes of agents or pathogens that transmit infectious diseases. Enumerated type.
    """
    class_: Literal['https://schema.org/InfectiousAgentClass'] = Field('class', alias='class', serialization_alias='class') # type: ignore
