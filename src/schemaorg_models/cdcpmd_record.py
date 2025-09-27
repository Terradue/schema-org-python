from typing import List, Literal, Optional, Union
from datetime import date, datetime
from pydantic import AliasChoices, Field
from schemaorg_models.structured_value import StructuredValue


class CDCPMDRecord(StructuredValue):
    """
A CDCPMDRecord is a data structure representing a record in a CDC tabular data format
      used for hospital data reporting. See [documentation](/docs/cdc-covid.html) for details, and the linked CDC materials for authoritative
      definitions used as the source here.
      
    """
    type_: Literal['https://schema.org/CDCPMDRecord'] = Field(default='https://schema.org/CDCPMDRecord', alias='@type', serialization_alias='http://www.w3.org/2000/01/rdf-schema#/Class') # type: ignore
    cvdNumICUBedsOcc: Optional[Union[float, List[float]]] = Field(default=None, validation_alias=AliasChoices('cvdNumICUBedsOcc', 'https://schema.org/cvdNumICUBedsOcc'), serialization_alias='https://schema.org/cvdNumICUBedsOcc')
    cvdNumVent: Optional[Union[float, List[float]]] = Field(default=None, validation_alias=AliasChoices('cvdNumVent', 'https://schema.org/cvdNumVent'), serialization_alias='https://schema.org/cvdNumVent')
    cvdNumICUBeds: Optional[Union[float, List[float]]] = Field(default=None, validation_alias=AliasChoices('cvdNumICUBeds', 'https://schema.org/cvdNumICUBeds'), serialization_alias='https://schema.org/cvdNumICUBeds')
    cvdNumBeds: Optional[Union[float, List[float]]] = Field(default=None, validation_alias=AliasChoices('cvdNumBeds', 'https://schema.org/cvdNumBeds'), serialization_alias='https://schema.org/cvdNumBeds')
    cvdCollectionDate: Optional[Union[str, List[str], datetime, List[datetime]]] = Field(default=None, validation_alias=AliasChoices('cvdCollectionDate', 'https://schema.org/cvdCollectionDate'), serialization_alias='https://schema.org/cvdCollectionDate')
    cvdNumC19OverflowPats: Optional[Union[float, List[float]]] = Field(default=None, validation_alias=AliasChoices('cvdNumC19OverflowPats', 'https://schema.org/cvdNumC19OverflowPats'), serialization_alias='https://schema.org/cvdNumC19OverflowPats')
    cvdFacilityId: Optional[Union[str, List[str]]] = Field(default=None, validation_alias=AliasChoices('cvdFacilityId', 'https://schema.org/cvdFacilityId'), serialization_alias='https://schema.org/cvdFacilityId')
    cvdNumC19OFMechVentPats: Optional[Union[float, List[float]]] = Field(default=None, validation_alias=AliasChoices('cvdNumC19OFMechVentPats', 'https://schema.org/cvdNumC19OFMechVentPats'), serialization_alias='https://schema.org/cvdNumC19OFMechVentPats')
    cvdFacilityCounty: Optional[Union[str, List[str]]] = Field(default=None, validation_alias=AliasChoices('cvdFacilityCounty', 'https://schema.org/cvdFacilityCounty'), serialization_alias='https://schema.org/cvdFacilityCounty')
    cvdNumC19Died: Optional[Union[float, List[float]]] = Field(default=None, validation_alias=AliasChoices('cvdNumC19Died', 'https://schema.org/cvdNumC19Died'), serialization_alias='https://schema.org/cvdNumC19Died')
    cvdNumTotBeds: Optional[Union[float, List[float]]] = Field(default=None, validation_alias=AliasChoices('cvdNumTotBeds', 'https://schema.org/cvdNumTotBeds'), serialization_alias='https://schema.org/cvdNumTotBeds')
    cvdNumC19HOPats: Optional[Union[float, List[float]]] = Field(default=None, validation_alias=AliasChoices('cvdNumC19HOPats', 'https://schema.org/cvdNumC19HOPats'), serialization_alias='https://schema.org/cvdNumC19HOPats')
    cvdNumC19HospPats: Optional[Union[float, List[float]]] = Field(default=None, validation_alias=AliasChoices('cvdNumC19HospPats', 'https://schema.org/cvdNumC19HospPats'), serialization_alias='https://schema.org/cvdNumC19HospPats')
    cvdNumC19MechVentPats: Optional[Union[float, List[float]]] = Field(default=None, validation_alias=AliasChoices('cvdNumC19MechVentPats', 'https://schema.org/cvdNumC19MechVentPats'), serialization_alias='https://schema.org/cvdNumC19MechVentPats')
    cvdNumVentUse: Optional[Union[float, List[float]]] = Field(default=None, validation_alias=AliasChoices('cvdNumVentUse', 'https://schema.org/cvdNumVentUse'), serialization_alias='https://schema.org/cvdNumVentUse')
    cvdNumBedsOcc: Optional[Union[float, List[float]]] = Field(default=None, validation_alias=AliasChoices('cvdNumBedsOcc', 'https://schema.org/cvdNumBedsOcc'), serialization_alias='https://schema.org/cvdNumBedsOcc')
    datePosted: Optional[Union[date, List[date], datetime, List[datetime]]] = Field(default=None, validation_alias=AliasChoices('datePosted', 'https://schema.org/datePosted'), serialization_alias='https://schema.org/datePosted')
