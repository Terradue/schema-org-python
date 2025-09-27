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
    class_: Literal['https://schema.org/TakeAction'] = Field(default='https://schema.org/TakeAction', alias='class', serialization_alias='class') # type: ignore
