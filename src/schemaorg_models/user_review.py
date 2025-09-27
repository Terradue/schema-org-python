from typing import Literal
from pydantic import Field
from schemaorg_models.review import Review


class UserReview(Review):
    """
A review created by an end-user (e.g. consumer, purchaser, attendee etc.), in contrast with [[CriticReview]].
    """
    type_: Literal['https://schema.org/UserReview'] = Field(default='https://schema.org/UserReview', alias='@type', serialization_alias='http://www.w3.org/2000/01/rdf-schema#/Class') # type: ignore
