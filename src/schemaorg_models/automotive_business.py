from typing import Literal
from pydantic import Field
from schemaorg_models.local_business import LocalBusiness


class AutomotiveBusiness(LocalBusiness):
    """
Car repair, sales, or parts.
    """
    class_: Literal['https://schema.org/AutomotiveBusiness'] = Field('class', alias='class', serialization_alias='class') # type: ignore
