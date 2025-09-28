from __future__ import annotations

from typing import TYPE_CHECKING
if TYPE_CHECKING:
    # put heavy, hint-only imports here
    from schemaorg_models.review import Review

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
