from typing import Literal
from pydantic import AliasChoices, Field
from schemaorg_models.review import Review


class EmployerReview(Review):
    """
An [[EmployerReview]] is a review of an [[Organization]] regarding its role as an employer, written by a current or former employee of that organization.
    """
    type_: Literal['https://schema.org/EmployerReview'] = Field('class', alias=AliasChoices('@type', 'https://schema.org/EmployerReview'),serialization_alias='class') # type: ignore
