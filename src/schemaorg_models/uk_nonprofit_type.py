from typing import Literal
from pydantic import AliasChoices, Field
from schemaorg_models.nonprofit_type import NonprofitType


class UKNonprofitType(NonprofitType):
    """
UKNonprofitType: Non-profit organization type originating from the United Kingdom.
    """
    type_: Literal['https://schema.org/UKNonprofitType'] = Field('class', alias=AliasChoices('@type', 'https://schema.org/UKNonprofitType'),serialization_alias='class') # type: ignore
