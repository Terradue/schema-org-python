from typing import Literal
from pydantic import Field
from schemaorg_models.church import Church


class CatholicChurch(Church):
    """
A Catholic church.
    """
    type_: Literal['https://schema.org/CatholicChurch'] = Field(default='https://schema.org/CatholicChurch', alias='@type', serialization_alias='@type') # type: ignore
