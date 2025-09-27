from typing import Literal
from pydantic import AliasChoices, Field
from schemaorg_models.dose_schedule import DoseSchedule


class RecommendedDoseSchedule(DoseSchedule):
    """
A recommended dosing schedule for a drug or supplement as prescribed or recommended by an authority or by the drug/supplement's manufacturer. Capture the recommending authority in the recognizingAuthority property of MedicalEntity.
    """
    type_: Literal['https://schema.org/RecommendedDoseSchedule'] = Field('class', alias=AliasChoices('@type', 'https://schema.org/RecommendedDoseSchedule'),serialization_alias='class') # type: ignore
