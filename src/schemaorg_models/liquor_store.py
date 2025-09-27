from typing import Literal
from pydantic import Field
from schemaorg_models.store import Store


class LiquorStore(Store):
    """
A shop that sells alcoholic drinks such as wine, beer, whisky and other spirits.
    """
    class_: Literal['https://schema.org/LiquorStore'] = Field(default='https://schema.org/LiquorStore', alias='class', serialization_alias='class') # type: ignore
