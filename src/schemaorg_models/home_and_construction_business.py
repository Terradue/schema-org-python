from typing import Literal
from pydantic import AliasChoices, Field
from schemaorg_models.local_business import LocalBusiness


class HomeAndConstructionBusiness(LocalBusiness):
    """
A construction business.\
\
A HomeAndConstructionBusiness is a [[LocalBusiness]] that provides services around homes and buildings.\
\
As a [[LocalBusiness]] it can be described as a [[provider]] of one or more [[Service]]\\(s).
    """
    type_: Literal['https://schema.org/HomeAndConstructionBusiness'] = Field('class', alias=AliasChoices('@type', 'https://schema.org/HomeAndConstructionBusiness'),serialization_alias='class') # type: ignore
