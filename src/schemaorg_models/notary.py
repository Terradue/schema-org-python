from typing import Literal
from pydantic import Field
from schemaorg_models.legal_service import LegalService


class Notary(LegalService):
    """
A notary.
    """
    class_: Literal['https://schema.org/Notary'] = Field('class', alias='class', serialization_alias='class') # type: ignore
