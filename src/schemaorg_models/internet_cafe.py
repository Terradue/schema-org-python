from typing import Literal
from pydantic import AliasChoices, Field
from schemaorg_models.local_business import LocalBusiness


class InternetCafe(LocalBusiness):
    """
An internet cafe.
    """
    type_: Literal['https://schema.org/InternetCafe'] = Field('class', alias=AliasChoices('@type', 'https://schema.org/InternetCafe'),serialization_alias='class') # type: ignore
