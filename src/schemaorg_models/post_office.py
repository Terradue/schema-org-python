from typing import Literal
from pydantic import Field
from schemaorg_models.government_office import GovernmentOffice


class PostOffice(GovernmentOffice):
    """
A post office.
    """
    class_: Literal['https://schema.org/PostOffice'] = Field('class', alias='class', serialization_alias='class') # type: ignore
