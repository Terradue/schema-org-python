from typing import Literal
from pydantic import Field
from schemaorg_models.inform_action import InformAction


class ConfirmAction(InformAction):
    """
The act of notifying someone that a future event/action is going to happen as expected.\
\
Related actions:\
\
* [[CancelAction]]: The antonym of ConfirmAction.
    """
    type_: Literal['https://schema.org/ConfirmAction'] = Field(default='https://schema.org/ConfirmAction', alias='@type', serialization_alias='@type') # type: ignore
