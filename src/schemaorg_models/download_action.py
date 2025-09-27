from typing import Literal
from pydantic import AliasChoices, Field
from schemaorg_models.transfer_action import TransferAction


class DownloadAction(TransferAction):
    """
The act of downloading an object.
    """
    type_: Literal['https://schema.org/DownloadAction'] = Field('class', alias=AliasChoices('@type', 'https://schema.org/DownloadAction'),serialization_alias='class') # type: ignore
