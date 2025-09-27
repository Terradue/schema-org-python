from typing import Literal
from pydantic import Field
from schemaorg_models.dose_schedule import DoseSchedule


class RecommendedDoseSchedule(DoseSchedule):
    """
A recommended dosing schedule for a drug or supplement as prescribed or recommended by an authority or by the drug/supplement's manufacturer. Capture the recommending authority in the recognizingAuthority property of MedicalEntity.
    """
    type_: Literal['https://schema.org/RecommendedDoseSchedule'] = Field(default='https://schema.org/RecommendedDoseSchedule', alias='@type', serialization_alias='http://www.w3.org/2000/01/rdf-schema#/Class') # type: ignore
