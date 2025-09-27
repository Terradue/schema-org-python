from typing import Literal
from pydantic import Field
from schemaorg_models.dose_schedule import DoseSchedule


class MaximumDoseSchedule(DoseSchedule):
    """
The maximum dosing schedule considered safe for a drug or supplement as recommended by an authority or by the drug/supplement's manufacturer. Capture the recommending authority in the recognizingAuthority property of MedicalEntity.
    """
    class_: Literal['https://schema.org/MaximumDoseSchedule'] = Field('class', alias='class', serialization_alias='class') # type: ignore
