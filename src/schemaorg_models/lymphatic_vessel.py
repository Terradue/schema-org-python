from typing import List, Literal, Optional, Union
from pydantic import AliasChoices, Field
from schemaorg_models.vessel import Vessel

from schemaorg_models.anatomical_structure import AnatomicalStructure
from schemaorg_models.anatomical_system import AnatomicalSystem
from schemaorg_models.vessel import Vessel

class LymphaticVessel(Vessel):
    """
A type of blood vessel that specifically carries lymph fluid unidirectionally toward the heart.
    """
    class_: Literal['https://schema.org/LymphaticVessel'] = Field(default='https://schema.org/LymphaticVessel', alias='http://www.w3.org/2000/01/rdf-schema#Class', serialization_alias='http://www.w3.org/2000/01/rdf-schema#Class') # type: ignore
    regionDrained: Optional[Union[AnatomicalStructure, List[AnatomicalStructure], AnatomicalSystem, List[AnatomicalSystem]]] = Field(default=None, validation_alias=AliasChoices('regionDrained', 'https://schema.org/regionDrained'), serialization_alias='https://schema.org/regionDrained')
    runsTo: Optional[Union[Vessel, List[Vessel]]] = Field(default=None, validation_alias=AliasChoices('runsTo', 'https://schema.org/runsTo'), serialization_alias='https://schema.org/runsTo')
    originatesFrom: Optional[Union[Vessel, List[Vessel]]] = Field(default=None, validation_alias=AliasChoices('originatesFrom', 'https://schema.org/originatesFrom'), serialization_alias='https://schema.org/originatesFrom')
