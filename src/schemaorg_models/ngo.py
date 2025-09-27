from typing import Literal
from pydantic import Field
from schemaorg_models.organization import Organization


class NGO(Organization):
    """
Organization: Non-governmental Organization.
    """
    class_: Literal['https://schema.org/NGO'] = Field('class', alias='class', serialization_alias='class') # type: ignore
