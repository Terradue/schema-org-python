from typing import Literal
from pydantic import Field
from schemaorg_models.nonprofit_type import NonprofitType


class USNonprofitType(NonprofitType):
    """
USNonprofitType: Non-profit organization type originating from the United States.
    """
    class_: Literal['https://schema.org/USNonprofitType'] = Field('class', alias='class', serialization_alias='class') # type: ignore
