from typing import Literal
from pydantic import AliasChoices, Field
from schemaorg_models.local_business import LocalBusiness


class Store(LocalBusiness):
    """
A retail good store.
    """
    type_: Literal['https://schema.org/Store'] = Field('class', alias=AliasChoices('@type', 'https://schema.org/Store'),serialization_alias='class') # type: ignore
