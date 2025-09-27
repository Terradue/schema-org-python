from typing import Literal
from pydantic import AliasChoices, Field
from schemaorg_models.plan_action import PlanAction


class CancelAction(PlanAction):
    """
The act of asserting that a future event/action is no longer going to happen.\
\
Related actions:\
\
* [[ConfirmAction]]: The antonym of CancelAction.
    """
    type_: Literal['https://schema.org/CancelAction'] = Field('class', alias=AliasChoices('@type', 'https://schema.org/CancelAction'),serialization_alias='class') # type: ignore
