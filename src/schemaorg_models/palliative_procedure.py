from typing import Literal
from pydantic import AliasChoices, Field
from schemaorg_models.medical_therapy import MedicalTherapy


class PalliativeProcedure(MedicalTherapy):
    """
A medical procedure intended primarily for palliative purposes, aimed at relieving the symptoms of an underlying health condition.
    """
    type_: Literal['https://schema.org/PalliativeProcedure'] = Field('class', alias=AliasChoices('@type', 'https://schema.org/PalliativeProcedure'),serialization_alias='class') # type: ignore
