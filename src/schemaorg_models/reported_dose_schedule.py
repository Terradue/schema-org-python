from typing import Literal
from pydantic import AliasChoices, Field
from schemaorg_models.dose_schedule import DoseSchedule


class ReportedDoseSchedule(DoseSchedule):
    """
A patient-reported or observed dosing schedule for a drug or supplement.
    """
    type_: Literal['https://schema.org/ReportedDoseSchedule'] = Field('class', alias=AliasChoices('@type', 'https://schema.org/ReportedDoseSchedule'),serialization_alias='class') # type: ignore
