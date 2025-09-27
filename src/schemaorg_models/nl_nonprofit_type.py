from typing import Literal
from pydantic import Field
from schemaorg_models.nonprofit_type import NonprofitType


class NLNonprofitType(NonprofitType):
    """
NLNonprofitType: Non-profit organization type originating from the Netherlands.
    """
    type_: Literal['https://schema.org/NLNonprofitType'] = Field(default='https://schema.org/NLNonprofitType', alias='@type', serialization_alias='@type') # type: ignore
