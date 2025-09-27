from typing import Literal
from pydantic import Field
from schemaorg_models.qualitative_value import QualitativeValue


class BedType(QualitativeValue):
    """
A type of bed. This is used for indicating the bed or beds available in an accommodation.
    """
    type_: Literal['https://schema.org/BedType'] = Field(default='https://schema.org/BedType', alias='@type', serialization_alias='@type') # type: ignore
