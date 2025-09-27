from typing import Literal
from pydantic import AliasChoices, Field
from schemaorg_models.local_business import LocalBusiness


class Library(LocalBusiness):
    """
A library.
    """
    type_: Literal['https://schema.org/Library'] = Field('class', alias=AliasChoices('@type', 'https://schema.org/Library'),serialization_alias='class') # type: ignore
