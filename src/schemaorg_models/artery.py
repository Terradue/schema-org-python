from typing import Union, List, Optional
from pydantic import AliasChoices, Field
from schemaorg_models.vessel import Vessel

from schemaorg_models.anatomical_structure import AnatomicalStructure

class Artery(Vessel):
    """
A type of blood vessel that specifically carries blood away from the heart.
    """
    arterialBranch: Optional[Union[AnatomicalStructure, List[AnatomicalStructure]]] = Field(default=None,validation_alias=AliasChoices('arterialBranch', 'https://schema.org/arterialBranch'),serialization_alias='https://schema.org/arterialBranch')
    supplyTo: Optional[Union[AnatomicalStructure, List[AnatomicalStructure]]] = Field(default=None,validation_alias=AliasChoices('supplyTo', 'https://schema.org/supplyTo'),serialization_alias='https://schema.org/supplyTo')
