from typing import Literal
from pydantic import AliasChoices, Field
from schemaorg_models.qualitative_value import QualitativeValue


class BedType(QualitativeValue):
    """
A type of bed. This is used for indicating the bed or beds available in an accommodation.
    """
    type_: Literal['https://schema.org/BedType'] = Field('class', alias=AliasChoices('@type', 'https://schema.org/BedType'),serialization_alias='class') # type: ignore
