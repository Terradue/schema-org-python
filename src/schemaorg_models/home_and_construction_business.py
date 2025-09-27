from typing import Literal
from pydantic import Field
from schemaorg_models.local_business import LocalBusiness


class HomeAndConstructionBusiness(LocalBusiness):
    """
A construction business.\
\
A HomeAndConstructionBusiness is a [[LocalBusiness]] that provides services around homes and buildings.\
\
As a [[LocalBusiness]] it can be described as a [[provider]] of one or more [[Service]]\\(s).
    """
    class_: Literal['https://schema.org/HomeAndConstructionBusiness'] = Field('class', alias='class', serialization_alias='class') # type: ignore
