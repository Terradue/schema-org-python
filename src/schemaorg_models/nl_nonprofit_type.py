from typing import Literal
from pydantic import AliasChoices, Field
from schemaorg_models.nonprofit_type import NonprofitType


class NLNonprofitType(NonprofitType):
    """
NLNonprofitType: Non-profit organization type originating from the Netherlands.
    """
    type_: Literal['https://schema.org/NLNonprofitType'] = Field('class', alias=AliasChoices('@type', 'https://schema.org/NLNonprofitType'),serialization_alias='class') # type: ignore
