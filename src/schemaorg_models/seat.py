from typing import List, Literal, Optional, Union
from pydantic import AliasChoices, Field
from schemaorg_models.intangible import Intangible


class Seat(Intangible):
    """
Used to describe a seat, such as a reserved seat in an event reservation.
    """
    type_: Literal['https://schema.org/Seat'] = Field(default='https://schema.org/Seat', alias='@type', serialization_alias='http://www.w3.org/2000/01/rdf-schema#/Class') # type: ignore
    seatNumber: Optional[Union[str, List[str]]] = Field(default=None, validation_alias=AliasChoices('seatNumber', 'https://schema.org/seatNumber'), serialization_alias='https://schema.org/seatNumber')
    seatSection: Optional[Union[str, List[str]]] = Field(default=None, validation_alias=AliasChoices('seatSection', 'https://schema.org/seatSection'), serialization_alias='https://schema.org/seatSection')
    seatingType: Optional[Union[str, List[str], "QualitativeValue", List["QualitativeValue"]]] = Field(default=None, validation_alias=AliasChoices('seatingType', 'https://schema.org/seatingType'), serialization_alias='https://schema.org/seatingType')
    seatRow: Optional[Union[str, List[str]]] = Field(default=None, validation_alias=AliasChoices('seatRow', 'https://schema.org/seatRow'), serialization_alias='https://schema.org/seatRow')
