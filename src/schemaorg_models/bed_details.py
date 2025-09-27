from typing import List, Literal, Optional, Union
from pydantic import AliasChoices, Field
from schemaorg_models.intangible import Intangible


class BedDetails(Intangible):
    """
An entity holding detailed information about the available bed types, e.g. the quantity of twin beds for a hotel room. For the single case of just one bed of a certain type, you can use bed directly with a text. See also [[BedType]] (under development).
    """
    class_: Literal['https://schema.org/BedDetails'] = Field(default='https://schema.org/BedDetails', alias='@type', serialization_alias='@type') # type: ignore
    typeOfBed: Optional[Union["BedType", List["BedType"], str, List[str]]] = Field(default=None, validation_alias=AliasChoices('typeOfBed', 'https://schema.org/typeOfBed'), serialization_alias='https://schema.org/typeOfBed')
    numberOfBeds: Optional[Union[float, List[float]]] = Field(default=None, validation_alias=AliasChoices('numberOfBeds', 'https://schema.org/numberOfBeds'), serialization_alias='https://schema.org/numberOfBeds')
