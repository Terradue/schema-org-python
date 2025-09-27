from typing import Literal
from pydantic import Field
from schemaorg_models.consume_action import ConsumeAction


class InstallAction(ConsumeAction):
    """
The act of installing an application.
    """
    type_: Literal['https://schema.org/InstallAction'] = Field(default='https://schema.org/InstallAction', alias='@type', serialization_alias='http://www.w3.org/2000/01/rdf-schema#/Class') # type: ignore
