from typing import List, Literal, Optional, Union
from pydantic import AliasChoices, Field
from schemaorg_models.find_action import FindAction

from schemaorg_models.delivery_method import DeliveryMethod

class TrackAction(FindAction):
    """
An agent tracks an object for updates.\
\
Related actions:\
\
* [[FollowAction]]: Unlike FollowAction, TrackAction refers to the interest on the location of innanimates objects.\
* [[SubscribeAction]]: Unlike SubscribeAction, TrackAction refers to  the interest on the location of innanimate objects.
    """
    type_: Literal['https://schema.org/TrackAction'] = Field(default='https://schema.org/TrackAction', alias='@type', serialization_alias='@type') # type: ignore
    deliveryMethod: Optional[Union[DeliveryMethod, List[DeliveryMethod]]] = Field(default=None, validation_alias=AliasChoices('deliveryMethod', 'https://schema.org/deliveryMethod'), serialization_alias='https://schema.org/deliveryMethod')
