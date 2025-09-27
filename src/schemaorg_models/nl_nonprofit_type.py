from typing import Literal
from pydantic import Field
from schemaorg_models.nonprofit_type import NonprofitType


class NLNonprofitType(NonprofitType):
    """
NLNonprofitType: Non-profit organization type originating from the Netherlands.
    """
    class_: Literal['https://schema.org/NLNonprofitType'] = Field(default='https://schema.org/NLNonprofitType', alias='class', serialization_alias='class') # type: ignore
