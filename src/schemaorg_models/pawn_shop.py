from typing import Literal
from pydantic import Field
from schemaorg_models.store import Store


class PawnShop(Store):
    """
A shop that will buy, or lend money against the security of, personal possessions.
    """
    class_: Literal['https://schema.org/PawnShop'] = Field('class', alias='class', serialization_alias='class') # type: ignore
