from typing import Literal
from pydantic import Field
from schemaorg_models.local_business import LocalBusiness


class SelfStorage(LocalBusiness):
    """
A self-storage facility.
    """
    class_: Literal['https://schema.org/SelfStorage'] = Field(default='https://schema.org/SelfStorage', alias='class', serialization_alias='class') # type: ignore
