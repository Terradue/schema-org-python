from typing import Literal
from pydantic import AliasChoices, Field
from schemaorg_models.store import Store


class LiquorStore(Store):
    """
A shop that sells alcoholic drinks such as wine, beer, whisky and other spirits.
    """
    type_: Literal['https://schema.org/LiquorStore'] = Field('class', alias=AliasChoices('@type', 'https://schema.org/LiquorStore'),serialization_alias='class') # type: ignore
