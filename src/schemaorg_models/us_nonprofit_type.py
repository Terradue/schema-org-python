from typing import Literal
from pydantic import AliasChoices, Field
from schemaorg_models.nonprofit_type import NonprofitType


class USNonprofitType(NonprofitType):
    """
USNonprofitType: Non-profit organization type originating from the United States.
    """
    type_: Literal['https://schema.org/USNonprofitType'] = Field('class', alias=AliasChoices('@type', 'https://schema.org/USNonprofitType'),serialization_alias='class') # type: ignore
