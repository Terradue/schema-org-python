from typing import Literal
from pydantic import Field
from schemaorg_models.legal_service import LegalService


class Attorney(LegalService):
    """
Professional service: Attorney. \
\
This type is deprecated - [[LegalService]] is more inclusive and less ambiguous.
    """
    class_: Literal['https://schema.org/Attorney'] = Field(default='https://schema.org/Attorney', alias='http://www.w3.org/2000/01/rdf-schema#Class', serialization_alias='http://www.w3.org/2000/01/rdf-schema#Class') # type: ignore
