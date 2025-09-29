from __future__ import annotations
from datetime import (
    date,
    datetime,
    time
)
from pydantic import (
    field_serializer,
    field_validator,
    AliasChoices,
    BaseModel,
    ConfigDict,
    Field,
    HttpUrl
)
from typing import (
    List,
    Literal,
    Optional,
    Union
)
from .structured_value import StructuredValue

class CDCPMDRecord(StructuredValue):
    '''
    A CDCPMDRecord is a data structure representing a record in a CDC tabular data format
      used for hospital data reporting. See [documentation](/docs/cdc-covid.html) for details, and the linked CDC materials for authoritative
      definitions used as the source here.
      

    Attributes:
        cvdNumICUBedsOcc: numicubedsocc - ICU BED OCCUPANCY: Total number of staffed inpatient ICU beds that are occupied.
        cvdNumVent: numvent - MECHANICAL VENTILATORS: Total number of ventilators available.
        cvdNumICUBeds: numicubeds - ICU BEDS: Total number of staffed inpatient intensive care unit (ICU) beds.
        cvdNumBeds: numbeds - HOSPITAL INPATIENT BEDS: Inpatient beds, including all staffed, licensed, and overflow (surge) beds used for inpatients.
        cvdCollectionDate: collectiondate - Date for which patient counts are reported.
        cvdNumC19OverflowPats: numc19overflowpats - ED/OVERFLOW: Patients with suspected or confirmed COVID-19 who are in the ED or any overflow location awaiting an inpatient bed.
        cvdFacilityId: Identifier of the NHSN facility that this data record applies to. Use [[cvdFacilityCounty]] to indicate the county. To provide other details, [[healthcareReportingData]] can be used on a [[Hospital]] entry.
        cvdNumC19OFMechVentPats: numc19ofmechventpats - ED/OVERFLOW and VENTILATED: Patients with suspected or confirmed COVID-19 who are in the ED or any overflow location awaiting an inpatient bed and on a mechanical ventilator.
        cvdFacilityCounty: Name of the County of the NHSN facility that this data record applies to. Use [[cvdFacilityId]] to identify the facility. To provide other details, [[healthcareReportingData]] can be used on a [[Hospital]] entry.
        cvdNumC19Died: numc19died - DEATHS: Patients with suspected or confirmed COVID-19 who died in the hospital, ED, or any overflow location.
        cvdNumTotBeds: numtotbeds - ALL HOSPITAL BEDS: Total number of all inpatient and outpatient beds, including all staffed, ICU, licensed, and overflow (surge) beds used for inpatients or outpatients.
        cvdNumC19HOPats: numc19hopats - HOSPITAL ONSET: Patients hospitalized in an NHSN inpatient care location with onset of suspected or confirmed COVID-19 14 or more days after hospitalization.
        cvdNumC19HospPats: numc19hosppats - HOSPITALIZED: Patients currently hospitalized in an inpatient care location who have suspected or confirmed COVID-19.
        cvdNumC19MechVentPats: numc19mechventpats - HOSPITALIZED and VENTILATED: Patients hospitalized in an NHSN inpatient care location who have suspected or confirmed COVID-19 and are on a mechanical ventilator.
        cvdNumVentUse: numventuse - MECHANICAL VENTILATORS IN USE: Total number of ventilators in use.
        cvdNumBedsOcc: numbedsocc - HOSPITAL INPATIENT BED OCCUPANCY: Total number of staffed inpatient beds that are occupied.
        datePosted: Publication date of an online listing.
    '''
    class_: Literal['https://schema.org/CDCPMDRecord'] = Field( # type: ignore
        default='https://schema.org/CDCPMDRecord',
        alias='@type',
        serialization_alias='@type'
    )
    cvdNumICUBedsOcc: Optional[Union[float, List[float]]] = Field(
        default=None,
        validation_alias=AliasChoices(
            'cvdNumICUBedsOcc',
            'https://schema.org/cvdNumICUBedsOcc'
        ),
        serialization_alias='https://schema.org/cvdNumICUBedsOcc'
    )
    cvdNumVent: Optional[Union[float, List[float]]] = Field(
        default=None,
        validation_alias=AliasChoices(
            'cvdNumVent',
            'https://schema.org/cvdNumVent'
        ),
        serialization_alias='https://schema.org/cvdNumVent'
    )
    cvdNumICUBeds: Optional[Union[float, List[float]]] = Field(
        default=None,
        validation_alias=AliasChoices(
            'cvdNumICUBeds',
            'https://schema.org/cvdNumICUBeds'
        ),
        serialization_alias='https://schema.org/cvdNumICUBeds'
    )
    cvdNumBeds: Optional[Union[float, List[float]]] = Field(
        default=None,
        validation_alias=AliasChoices(
            'cvdNumBeds',
            'https://schema.org/cvdNumBeds'
        ),
        serialization_alias='https://schema.org/cvdNumBeds'
    )
    cvdCollectionDate: Optional[Union[str, List[str], datetime, List[datetime]]] = Field(
        default=None,
        validation_alias=AliasChoices(
            'cvdCollectionDate',
            'https://schema.org/cvdCollectionDate'
        ),
        serialization_alias='https://schema.org/cvdCollectionDate'
    )
    cvdNumC19OverflowPats: Optional[Union[float, List[float]]] = Field(
        default=None,
        validation_alias=AliasChoices(
            'cvdNumC19OverflowPats',
            'https://schema.org/cvdNumC19OverflowPats'
        ),
        serialization_alias='https://schema.org/cvdNumC19OverflowPats'
    )
    cvdFacilityId: Optional[Union[str, List[str]]] = Field(
        default=None,
        validation_alias=AliasChoices(
            'cvdFacilityId',
            'https://schema.org/cvdFacilityId'
        ),
        serialization_alias='https://schema.org/cvdFacilityId'
    )
    cvdNumC19OFMechVentPats: Optional[Union[float, List[float]]] = Field(
        default=None,
        validation_alias=AliasChoices(
            'cvdNumC19OFMechVentPats',
            'https://schema.org/cvdNumC19OFMechVentPats'
        ),
        serialization_alias='https://schema.org/cvdNumC19OFMechVentPats'
    )
    cvdFacilityCounty: Optional[Union[str, List[str]]] = Field(
        default=None,
        validation_alias=AliasChoices(
            'cvdFacilityCounty',
            'https://schema.org/cvdFacilityCounty'
        ),
        serialization_alias='https://schema.org/cvdFacilityCounty'
    )
    cvdNumC19Died: Optional[Union[float, List[float]]] = Field(
        default=None,
        validation_alias=AliasChoices(
            'cvdNumC19Died',
            'https://schema.org/cvdNumC19Died'
        ),
        serialization_alias='https://schema.org/cvdNumC19Died'
    )
    cvdNumTotBeds: Optional[Union[float, List[float]]] = Field(
        default=None,
        validation_alias=AliasChoices(
            'cvdNumTotBeds',
            'https://schema.org/cvdNumTotBeds'
        ),
        serialization_alias='https://schema.org/cvdNumTotBeds'
    )
    cvdNumC19HOPats: Optional[Union[float, List[float]]] = Field(
        default=None,
        validation_alias=AliasChoices(
            'cvdNumC19HOPats',
            'https://schema.org/cvdNumC19HOPats'
        ),
        serialization_alias='https://schema.org/cvdNumC19HOPats'
    )
    cvdNumC19HospPats: Optional[Union[float, List[float]]] = Field(
        default=None,
        validation_alias=AliasChoices(
            'cvdNumC19HospPats',
            'https://schema.org/cvdNumC19HospPats'
        ),
        serialization_alias='https://schema.org/cvdNumC19HospPats'
    )
    cvdNumC19MechVentPats: Optional[Union[float, List[float]]] = Field(
        default=None,
        validation_alias=AliasChoices(
            'cvdNumC19MechVentPats',
            'https://schema.org/cvdNumC19MechVentPats'
        ),
        serialization_alias='https://schema.org/cvdNumC19MechVentPats'
    )
    cvdNumVentUse: Optional[Union[float, List[float]]] = Field(
        default=None,
        validation_alias=AliasChoices(
            'cvdNumVentUse',
            'https://schema.org/cvdNumVentUse'
        ),
        serialization_alias='https://schema.org/cvdNumVentUse'
    )
    cvdNumBedsOcc: Optional[Union[float, List[float]]] = Field(
        default=None,
        validation_alias=AliasChoices(
            'cvdNumBedsOcc',
            'https://schema.org/cvdNumBedsOcc'
        ),
        serialization_alias='https://schema.org/cvdNumBedsOcc'
    )
    datePosted: Optional[Union[date, List[date], datetime, List[datetime]]] = Field(
        default=None,
        validation_alias=AliasChoices(
            'datePosted',
            'https://schema.org/datePosted'
        ),
        serialization_alias='https://schema.org/datePosted'
    )
