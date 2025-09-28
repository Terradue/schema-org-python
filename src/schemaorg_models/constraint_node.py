from __future__ import annotations
from pydantic import (
    AliasChoices,
    Field,
    HttpUrl
)
from typing import (
    List,
    Literal,
    Optional,
    Union
)
from .intangible import Intangible
from typing import TYPE_CHECKING
if TYPE_CHECKING:
    from .property import Property

class ConstraintNode(Intangible):
    """
The ConstraintNode type is provided to support usecases in which a node in a structured data graph is described with properties which appear to describe a single entity, but are being used in a situation where they serve a more abstract purpose. A [[ConstraintNode]] can be described using [[constraintProperty]] and [[numConstraints]]. These constraint properties can serve a
    variety of purposes, and their values may sometimes be understood to indicate sets of possible values rather than single, exact and specific values.
    """
    class_: Literal['https://schema.org/ConstraintNode'] = Field( # type: ignore
        default='https://schema.org/ConstraintNode',
        alias='@type',
        serialization_alias='@type'
    )
    numConstraints: Optional[Union[int, List[int]]] = Field(
        default=None,
        validation_alias=AliasChoices(
            'numConstraints',
            'https://schema.org/numConstraints'
        ),
        serialization_alias='https://schema.org/numConstraints'
    )
    constraintProperty: Optional[Union[HttpUrl, List[HttpUrl], "Property", List["Property"]]] = Field(
        default=None,
        validation_alias=AliasChoices(
            'constraintProperty',
            'https://schema.org/constraintProperty'
        ),
        serialization_alias='https://schema.org/constraintProperty'
    )
