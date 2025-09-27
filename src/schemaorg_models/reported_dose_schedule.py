from typing import Literal
from pydantic import Field
from schemaorg_models.dose_schedule import DoseSchedule


class ReportedDoseSchedule(DoseSchedule):
    """
A patient-reported or observed dosing schedule for a drug or supplement.
    """
    type_: Literal['https://schema.org/ReportedDoseSchedule'] = Field(default='https://schema.org/ReportedDoseSchedule', alias='@type', serialization_alias='http://www.w3.org/2000/01/rdf-schema#/Class') # type: ignore
