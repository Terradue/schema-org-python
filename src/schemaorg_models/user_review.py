from typing import Literal
from pydantic import AliasChoices, Field
from schemaorg_models.review import Review


class UserReview(Review):
    """
A review created by an end-user (e.g. consumer, purchaser, attendee etc.), in contrast with [[CriticReview]].
    """
    type_: Literal['https://schema.org/UserReview'] = Field('class', alias=AliasChoices('@type', 'https://schema.org/UserReview'),serialization_alias='class') # type: ignore
