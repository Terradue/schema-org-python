from typing import Literal
from pydantic import Field
from schemaorg_models.review import Review


class EmployerReview(Review):
    """
An [[EmployerReview]] is a review of an [[Organization]] regarding its role as an employer, written by a current or former employee of that organization.
    """
    type_: Literal['https://schema.org/EmployerReview'] = Field(default='https://schema.org/EmployerReview', alias='@type', serialization_alias='http://www.w3.org/2000/01/rdf-schema#/Class') # type: ignore
