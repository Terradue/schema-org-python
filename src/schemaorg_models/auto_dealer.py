from typing import Literal
from pydantic import AliasChoices, Field
from schemaorg_models.automotive_business import AutomotiveBusiness


class AutoDealer(AutomotiveBusiness):
    """
An car dealership.
    """
    type_: Literal['https://schema.org/AutoDealer'] = Field('class', alias=AliasChoices('@type', 'https://schema.org/AutoDealer'),serialization_alias='class') # type: ignore
