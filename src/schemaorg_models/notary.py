from typing import Literal
from pydantic import AliasChoices, Field
from schemaorg_models.legal_service import LegalService


class Notary(LegalService):
    """
A notary.
    """
    type_: Literal['https://schema.org/Notary'] = Field('class', alias=AliasChoices('@type', 'https://schema.org/Notary'),serialization_alias='class') # type: ignore
