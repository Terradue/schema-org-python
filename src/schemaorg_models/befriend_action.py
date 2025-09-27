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
    class_: Literal['https://schema.org/BefriendAction'] = Field(default='https://schema.org/BefriendAction', alias='http://www.w3.org/2000/01/rdf-schema#Class', serialization_alias='http://www.w3.org/2000/01/rdf-schema#Class') # type: ignore
