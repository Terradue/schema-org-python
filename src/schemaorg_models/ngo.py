from typing import Literal
from pydantic import AliasChoices, Field
from schemaorg_models.organization import Organization


class NGO(Organization):
    """
Organization: Non-governmental Organization.
    """
    type_: Literal['https://schema.org/NGO'] = Field('class', alias=AliasChoices('@type', 'https://schema.org/NGO'),serialization_alias='class') # type: ignore
