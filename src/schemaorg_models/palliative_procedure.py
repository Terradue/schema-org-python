from typing import Literal
from pydantic import Field
from schemaorg_models.medical_therapy import MedicalTherapy


class PalliativeProcedure(MedicalTherapy):
    """
A medical procedure intended primarily for palliative purposes, aimed at relieving the symptoms of an underlying health condition.
    """
    class_: Literal['https://schema.org/PalliativeProcedure'] = Field('class', alias='class', serialization_alias='class') # type: ignore
