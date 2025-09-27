from typing import Literal
from pydantic import Field
from schemaorg_models.nonprofit_type import NonprofitType


class UKNonprofitType(NonprofitType):
    """
UKNonprofitType: Non-profit organization type originating from the United Kingdom.
    """
    class_: Literal['https://schema.org/UKNonprofitType'] = Field(default='https://schema.org/UKNonprofitType', alias='@type', serialization_alias='@type') # type: ignore
