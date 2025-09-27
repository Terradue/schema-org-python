from typing import Literal
from pydantic import Field
from schemaorg_models.action import Action


class OrganizeAction(Action):
    """
The act of manipulating/administering/supervising/controlling one or more objects.
    """
    type_: Literal['https://schema.org/OrganizeAction'] = Field(default='https://schema.org/OrganizeAction', alias='@type', serialization_alias='http://www.w3.org/2000/01/rdf-schema#/Class') # type: ignore
