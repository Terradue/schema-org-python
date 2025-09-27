from typing import Literal
from pydantic import AliasChoices, Field
from schemaorg_models.communicate_action import CommunicateAction


class ShareAction(CommunicateAction):
    """
The act of distributing content to people for their amusement or edification.
    """
    type_: Literal['https://schema.org/ShareAction'] = Field('class', alias=AliasChoices('@type', 'https://schema.org/ShareAction'),serialization_alias='class') # type: ignore
