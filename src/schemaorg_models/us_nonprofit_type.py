from typing import Literal
from pydantic import Field
from schemaorg_models.nonprofit_type import NonprofitType


class USNonprofitType(NonprofitType):
    """
USNonprofitType: Non-profit organization type originating from the United States.
    """
    type_: Literal['https://schema.org/USNonprofitType'] = Field(default='https://schema.org/USNonprofitType', alias='@type', serialization_alias='http://www.w3.org/2000/01/rdf-schema#/Class') # type: ignore
