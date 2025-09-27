from typing import Literal
from pydantic import AliasChoices, Field
from schemaorg_models.store import Store


class PawnShop(Store):
    """
A shop that will buy, or lend money against the security of, personal possessions.
    """
    type_: Literal['https://schema.org/PawnShop'] = Field('class', alias=AliasChoices('@type', 'https://schema.org/PawnShop'),serialization_alias='class') # type: ignore
