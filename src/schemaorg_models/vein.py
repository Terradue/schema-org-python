from typing import List, Literal, Optional, Union
from pydantic import AliasChoices, Field
from schemaorg_models.vessel import Vessel

from schemaorg_models.anatomical_structure import AnatomicalStructure
from schemaorg_models.anatomical_system import AnatomicalSystem
from schemaorg_models.vessel import Vessel

class Vein(Vessel):
    """
A type of blood vessel that specifically carries blood to the heart.
    """
    type_: Literal['https://schema.org/Vein'] = Field(default='https://schema.org/Vein', alias='@type', serialization_alias='@type') # type: ignore
    regionDrained: Optional[Union[AnatomicalStructure, List[AnatomicalStructure], AnatomicalSystem, List[AnatomicalSystem]]] = Field(default=None, validation_alias=AliasChoices('regionDrained', 'https://schema.org/regionDrained'), serialization_alias='https://schema.org/regionDrained')
    drainsTo: Optional[Union[Vessel, List[Vessel]]] = Field(default=None, validation_alias=AliasChoices('drainsTo', 'https://schema.org/drainsTo'), serialization_alias='https://schema.org/drainsTo')
    tributary: Optional[Union[AnatomicalStructure, List[AnatomicalStructure]]] = Field(default=None, validation_alias=AliasChoices('tributary', 'https://schema.org/tributary'), serialization_alias='https://schema.org/tributary')
