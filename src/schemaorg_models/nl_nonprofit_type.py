from typing import Literal
from pydantic import Field
from schemaorg_models.nonprofit_type import NonprofitType


class NLNonprofitType(NonprofitType):
    """
NLNonprofitType: Non-profit organization type originating from the Netherlands.
    """
    class_: Literal['https://schema.org/NLNonprofitType'] = Field(default='https://schema.org/NLNonprofitType', alias='http://www.w3.org/2000/01/rdf-schema#Class', serialization_alias='http://www.w3.org/2000/01/rdf-schema#Class') # type: ignore
