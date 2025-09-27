from typing import Literal
from pydantic import Field
from schemaorg_models.automotive_business import AutomotiveBusiness


class AutoDealer(AutomotiveBusiness):
    """
An car dealership.
    """
    class_: Literal['https://schema.org/AutoDealer'] = Field(default='https://schema.org/AutoDealer', alias='@type', serialization_alias='@type') # type: ignore
