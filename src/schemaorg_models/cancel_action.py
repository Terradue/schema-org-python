from typing import Literal
from pydantic import Field
from schemaorg_models.plan_action import PlanAction


class CancelAction(PlanAction):
    """
The act of asserting that a future event/action is no longer going to happen.\
\
Related actions:\
\
* [[ConfirmAction]]: The antonym of CancelAction.
    """
    class_: Literal['https://schema.org/CancelAction'] = Field(default='https://schema.org/CancelAction', alias='class', serialization_alias='class') # type: ignore
