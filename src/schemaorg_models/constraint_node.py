from __future__ import annotations
from datetime import (
    date,
    datetime,
    time
)
from pydantic import (
    field_serializer,
    field_validator,
    AliasChoices,
    BaseModel,
    ConfigDict,
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
    '''
    The ConstraintNode type is provided to support usecases in which a node in a structured data graph is described with properties which appear to describe a single entity, but are being used in a situation where they serve a more abstract purpose. A [[ConstraintNode]] can be described using [[constraintProperty]] and [[numConstraints]]. These constraint properties can serve a
    variety of purposes, and their values may sometimes be understood to indicate sets of possible values rather than single, exact and specific values.

    Attributes:
        numConstraints: Indicates the number of constraints property values defined for a particular [[ConstraintNode]] such as [[StatisticalVariable]]. This helps applications understand if they have access to a sufficiently complete description of a [[StatisticalVariable]] or other construct that is defined using properties on template-style nodes.
        constraintProperty: Indicates a property used as a constraint. For example, in the definition of a [[StatisticalVariable]]. The value is a property, either from within Schema.org or from other compatible (e.g. RDF) systems such as DataCommons.org or Wikidata.org. 
    '''
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
    constraintProperty: Optional[Union[HttpUrl, List[HttpUrl], 'Property', List['Property']]] = Field(
        default=None,
        validation_alias=AliasChoices(
            'constraintProperty',
            'https://schema.org/constraintProperty'
        ),
        serialization_alias='https://schema.org/constraintProperty'
    )
