from typing import Literal
from pydantic import AliasChoices, Field
from schemaorg_models.action import Action


class OrganizeAction(Action):
    """
The act of manipulating/administering/supervising/controlling one or more objects.
    """
    type_: Literal['https://schema.org/OrganizeAction'] = Field('class', alias=AliasChoices('@type', 'https://schema.org/OrganizeAction'),serialization_alias='class') # type: ignore
