from typing import Literal
from pydantic import Field
from schemaorg_models.store import Store


class OfficeEquipmentStore(Store):
    """
An office equipment store.
    """
    type_: Literal['https://schema.org/OfficeEquipmentStore'] = Field(default='https://schema.org/OfficeEquipmentStore', alias='@type', serialization_alias='http://www.w3.org/2000/01/rdf-schema#/Class') # type: ignore
