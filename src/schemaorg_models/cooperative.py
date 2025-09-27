from typing import Literal
from pydantic import AliasChoices, Field
from schemaorg_models.organization import Organization


class Cooperative(Organization):
    """
An organization that is a joint project of multiple organizations or persons.
    """
    type_: Literal['https://schema.org/Cooperative'] = Field('class', alias=AliasChoices('@type', 'https://schema.org/Cooperative'),serialization_alias='class') # type: ignore
