from __future__ import annotations
from pydantic import (
    AliasChoices,
    Field
)
from typing import (
    List,
    Literal,
    Optional,
    Union
)
from .find_action import FindAction
from .delivery_method import DeliveryMethod

class TrackAction(FindAction):
    """
An agent tracks an object for updates.\
\
Related actions:\
\
* [[FollowAction]]: Unlike FollowAction, TrackAction refers to the interest on the location of innanimates objects.\
* [[SubscribeAction]]: Unlike SubscribeAction, TrackAction refers to  the interest on the location of innanimate objects.
    """
    class_: Literal['https://schema.org/TrackAction'] = Field( # type: ignore
        default='https://schema.org/TrackAction',
        alias='@type',
        serialization_alias='@type'
    )
    deliveryMethod: Optional[Union[DeliveryMethod, List[DeliveryMethod]]] = Field(
        default=None,
        validation_alias=AliasChoices(
            'deliveryMethod',
            'https://schema.org/deliveryMethod'
        ),
        serialization_alias='https://schema.org/deliveryMethod'
    )
