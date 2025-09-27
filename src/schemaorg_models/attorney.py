from typing import Literal
from pydantic import Field
from schemaorg_models.legal_service import LegalService


class Attorney(LegalService):
    """
Professional service: Attorney. \
\
This type is deprecated - [[LegalService]] is more inclusive and less ambiguous.
    """
    type_: Literal['https://schema.org/Attorney'] = Field(default='https://schema.org/Attorney', alias='@type', serialization_alias='@type') # type: ignore
