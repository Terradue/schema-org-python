from typing import Literal
from pydantic import Field
from schemaorg_models.store import Store


class PawnShop(Store):
    """
A shop that will buy, or lend money against the security of, personal possessions.
    """
    type_: Literal['https://schema.org/PawnShop'] = Field(default='https://schema.org/PawnShop', alias='@type', serialization_alias='@type') # type: ignore
