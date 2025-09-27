from typing import Literal
from pydantic import Field
from schemaorg_models.transfer_action import TransferAction


class TakeAction(TransferAction):
    """
The act of gaining ownership of an object from an origin. Reciprocal of GiveAction.\
\
Related actions:\
\
* [[GiveAction]]: The reciprocal of TakeAction.\
* [[ReceiveAction]]: Unlike ReceiveAction, TakeAction implies that ownership has been transferred.
    """
    type_: Literal['https://schema.org/TakeAction'] = Field(default='https://schema.org/TakeAction', alias='@type', serialization_alias='http://www.w3.org/2000/01/rdf-schema#/Class') # type: ignore
