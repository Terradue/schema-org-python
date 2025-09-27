from typing import Literal
from pydantic import AliasChoices, Field
from schemaorg_models.store import Store


class ComputerStore(Store):
    """
A computer store.
    """
    type_: Literal['https://schema.org/ComputerStore'] = Field('class', alias=AliasChoices('@type', 'https://schema.org/ComputerStore'),serialization_alias='class') # type: ignore
