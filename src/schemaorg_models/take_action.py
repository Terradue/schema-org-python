from typing import Literal
from pydantic import AliasChoices, Field
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
    type_: Literal['https://schema.org/TakeAction'] = Field('class', alias=AliasChoices('@type', 'https://schema.org/TakeAction'),serialization_alias='class') # type: ignore
