from typing import Literal
from pydantic import Field
from schemaorg_models.transfer_action import TransferAction


class DownloadAction(TransferAction):
    """
The act of downloading an object.
    """
    class_: Literal['https://schema.org/DownloadAction'] = Field(default='https://schema.org/DownloadAction', alias='http://www.w3.org/2000/01/rdf-schema#Class', serialization_alias='http://www.w3.org/2000/01/rdf-schema#Class') # type: ignore
