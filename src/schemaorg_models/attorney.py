from typing import Literal
from pydantic import Field
from schemaorg_models.legal_service import LegalService


class Attorney(LegalService):
    """
Professional service: Attorney. \
\
This type is deprecated - [[LegalService]] is more inclusive and less ambiguous.
    """
    class_: Literal['https://schema.org/Attorney'] = Field('class', alias='class', serialization_alias='class') # type: ignore
