from typing import Literal
from pydantic import Field
from schemaorg_models.review import Review


class UserReview(Review):
    """
A review created by an end-user (e.g. consumer, purchaser, attendee etc.), in contrast with [[CriticReview]].
    """
    class_: Literal['https://schema.org/UserReview'] = Field(default='https://schema.org/UserReview', alias='class', serialization_alias='class') # type: ignore
