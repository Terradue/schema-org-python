from typing import Literal
from pydantic import Field
from schemaorg_models.interact_action import InteractAction


class BefriendAction(InteractAction):
    """
The act of forming a personal connection with someone (object) mutually/bidirectionally/symmetrically.\
\
Related actions:\
\
* [[FollowAction]]: Unlike FollowAction, BefriendAction implies that the connection is reciprocal.
    """
    class_: Literal['https://schema.org/BefriendAction'] = Field('class', alias='class', serialization_alias='class') # type: ignore
