from __future__ import annotations

from .review import Review    

from pydantic import (
    Field
)
from typing import (
    Literal
)

class EmployerReview(Review):
    """
An [[EmployerReview]] is a review of an [[Organization]] regarding its role as an employer, written by a current or former employee of that organization.
    """
    class_: Literal['https://schema.org/EmployerReview'] = Field( # type: ignore
        default='https://schema.org/EmployerReview',
        alias='@type',
        serialization_alias='@type'
    )
