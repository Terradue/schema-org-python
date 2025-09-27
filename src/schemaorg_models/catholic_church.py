from typing import Literal
from pydantic import AliasChoices, Field
from schemaorg_models.church import Church


class CatholicChurch(Church):
    """
A Catholic church.
    """
    type_: Literal['https://schema.org/CatholicChurch'] = Field('class', alias=AliasChoices('@type', 'https://schema.org/CatholicChurch'),serialization_alias='class') # type: ignore
