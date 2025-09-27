from typing import Literal
from pydantic import AliasChoices, Field
from schemaorg_models.medical_enumeration import MedicalEnumeration


class InfectiousAgentClass(MedicalEnumeration):
    """
Classes of agents or pathogens that transmit infectious diseases. Enumerated type.
    """
    type_: Literal['https://schema.org/InfectiousAgentClass'] = Field('class', alias=AliasChoices('@type', 'https://schema.org/InfectiousAgentClass'),serialization_alias='class') # type: ignore
