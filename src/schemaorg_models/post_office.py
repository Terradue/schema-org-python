from typing import Literal
from pydantic import AliasChoices, Field
from schemaorg_models.government_office import GovernmentOffice


class PostOffice(GovernmentOffice):
    """
A post office.
    """
    type_: Literal['https://schema.org/PostOffice'] = Field('class', alias=AliasChoices('@type', 'https://schema.org/PostOffice'),serialization_alias='class') # type: ignore
