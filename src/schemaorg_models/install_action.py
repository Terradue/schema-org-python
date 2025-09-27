from typing import Literal
from pydantic import AliasChoices, Field
from schemaorg_models.consume_action import ConsumeAction


class InstallAction(ConsumeAction):
    """
The act of installing an application.
    """
    type_: Literal['https://schema.org/InstallAction'] = Field('class', alias=AliasChoices('@type', 'https://schema.org/InstallAction'),serialization_alias='class') # type: ignore
