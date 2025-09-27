from typing import Literal
from pydantic import Field
from schemaorg_models.transfer_action import TransferAction


class DownloadAction(TransferAction):
    """
The act of downloading an object.
    """
    class_: Literal['https://schema.org/DownloadAction'] = Field('class', alias='class', serialization_alias='class') # type: ignore
