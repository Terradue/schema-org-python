from typing import Literal
from pydantic import Field
from schemaorg_models.medical_therapy import MedicalTherapy


class PalliativeProcedure(MedicalTherapy):
    """
A medical procedure intended primarily for palliative purposes, aimed at relieving the symptoms of an underlying health condition.
    """
    class_: Literal['https://schema.org/PalliativeProcedure'] = Field(default='https://schema.org/PalliativeProcedure', alias='@type', serialization_alias='@type') # type: ignore
