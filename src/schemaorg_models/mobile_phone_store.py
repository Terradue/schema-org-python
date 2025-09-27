from typing import Literal
from pydantic import AliasChoices, Field
from schemaorg_models.store import Store


class MobilePhoneStore(Store):
    """
A store that sells mobile phones and related accessories.
    """
    type_: Literal['https://schema.org/MobilePhoneStore'] = Field('class', alias=AliasChoices('@type', 'https://schema.org/MobilePhoneStore'),serialization_alias='class') # type: ignore
