from typing import List, Literal, Optional, Union
from pydantic import AliasChoices, Field
from schemaorg_models.anatomical_structure import AnatomicalStructure

from schemaorg_models.anatomical_structure import AnatomicalStructure
from schemaorg_models.vessel import Vessel

class Muscle(AnatomicalStructure):
    """
A muscle is an anatomical structure consisting of a contractile form of tissue that animals use to effect movement.
    """
    class_: Literal['https://schema.org/Muscle'] = Field(default='https://schema.org/Muscle', alias='http://www.w3.org/2000/01/rdf-schema#Class', serialization_alias='http://www.w3.org/2000/01/rdf-schema#Class') # type: ignore
    antagonist: Optional[Union["Muscle", List["Muscle"]]] = Field(default=None, validation_alias=AliasChoices('antagonist', 'https://schema.org/antagonist'), serialization_alias='https://schema.org/antagonist')
    insertion: Optional[Union[AnatomicalStructure, List[AnatomicalStructure]]] = Field(default=None, validation_alias=AliasChoices('insertion', 'https://schema.org/insertion'), serialization_alias='https://schema.org/insertion')
    nerve: Optional[Union["Nerve", List["Nerve"]]] = Field(default=None, validation_alias=AliasChoices('nerve', 'https://schema.org/nerve'), serialization_alias='https://schema.org/nerve')
    bloodSupply: Optional[Union[Vessel, List[Vessel]]] = Field(default=None, validation_alias=AliasChoices('bloodSupply', 'https://schema.org/bloodSupply'), serialization_alias='https://schema.org/bloodSupply')
    muscleAction: Optional[Union[str, List[str]]] = Field(default=None, validation_alias=AliasChoices('muscleAction', 'https://schema.org/muscleAction'), serialization_alias='https://schema.org/muscleAction')
