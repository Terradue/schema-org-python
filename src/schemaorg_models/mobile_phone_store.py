from typing import Literal
from pydantic import Field
from schemaorg_models.store import Store


class MobilePhoneStore(Store):
    """
A store that sells mobile phones and related accessories.
    """
    type_: Literal['https://schema.org/MobilePhoneStore'] = Field(default='https://schema.org/MobilePhoneStore', alias='@type', serialization_alias='http://www.w3.org/2000/01/rdf-schema#/Class') # type: ignore
