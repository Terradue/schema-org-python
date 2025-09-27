from typing import List, Literal, Optional, Union
from pydantic import AliasChoices, Field
from schemaorg_models.inform_action import InformAction

from schemaorg_models.comment import Comment
from schemaorg_models.rsvp_response_type import RsvpResponseType

class RsvpAction(InformAction):
    """
The act of notifying an event organizer as to whether you expect to attend the event.
    """
    class_: Literal['https://schema.org/RsvpAction'] = Field('class', alias='class', serialization_alias='class') # type: ignore
    additionalNumberOfGuests: Optional[Union[float, List[float]]] = Field(default=None,validation_alias=AliasChoices('additionalNumberOfGuests', 'https://schema.org/additionalNumberOfGuests'), serialization_alias='https://schema.org/additionalNumberOfGuests')
    comment: Optional[Union[Comment, List[Comment]]] = Field(default=None,validation_alias=AliasChoices('comment', 'https://schema.org/comment'), serialization_alias='https://schema.org/comment')
    rsvpResponse: Optional[Union[RsvpResponseType, List[RsvpResponseType]]] = Field(default=None,validation_alias=AliasChoices('rsvpResponse', 'https://schema.org/rsvpResponse'), serialization_alias='https://schema.org/rsvpResponse')
