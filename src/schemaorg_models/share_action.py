from typing import Literal
from pydantic import Field
from schemaorg_models.communicate_action import CommunicateAction


class ShareAction(CommunicateAction):
    """
The act of distributing content to people for their amusement or edification.
    """
    class_: Literal['https://schema.org/ShareAction'] = Field('class', alias='class', serialization_alias='class') # type: ignore
