from typing import Literal
from pydantic import Field
from schemaorg_models.transfer_action import TransferAction


class DownloadAction(TransferAction):
    """
The act of downloading an object.
    """
    class_: Literal['https://schema.org/DownloadAction'] = Field(default='https://schema.org/DownloadAction', alias='@type', serialization_alias='@type') # type: ignore
