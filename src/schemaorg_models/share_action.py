from typing import Literal
from pydantic import Field
from schemaorg_models.communicate_action import CommunicateAction


class ShareAction(CommunicateAction):
    """
The act of distributing content to people for their amusement or edification.
    """
    type_: Literal['https://schema.org/ShareAction'] = Field(default='https://schema.org/ShareAction', alias='@type', serialization_alias='@type') # type: ignore
