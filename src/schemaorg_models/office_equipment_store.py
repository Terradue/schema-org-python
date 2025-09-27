from typing import Literal
from pydantic import AliasChoices, Field
from schemaorg_models.store import Store


class OfficeEquipmentStore(Store):
    """
An office equipment store.
    """
    type_: Literal['https://schema.org/OfficeEquipmentStore'] = Field('class', alias=AliasChoices('@type', 'https://schema.org/OfficeEquipmentStore'),serialization_alias='class') # type: ignore
