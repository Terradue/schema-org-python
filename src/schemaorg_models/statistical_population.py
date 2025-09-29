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
    from .__class import _Class

class StatisticalPopulation(Intangible):
    '''
    A StatisticalPopulation is a set of instances of a certain given type that satisfy some set of constraints. The property [[populationType]] is used to specify the type. Any property that can be used on instances of that type can appear on the statistical population. For example, a [[StatisticalPopulation]] representing all [[Person]]s with a [[homeLocation]] of East Podunk California would be described by applying the appropriate [[homeLocation]] and [[populationType]] properties to a [[StatisticalPopulation]] item that stands for that set of people.
The properties [[numConstraints]] and [[constraintProperty]] are used to specify which of the populations properties are used to specify the population. Note that the sense of "population" used here is the general sense of a statistical
population, and does not imply that the population consists of people. For example, a [[populationType]] of [[Event]] or [[NewsArticle]] could be used. See also [[Observation]], where a [[populationType]] such as [[Person]] or [[Event]] can be indicated directly. In most cases it may be better to use [[StatisticalVariable]] instead of [[StatisticalPopulation]].

    Attributes:
        populationType: Indicates the populationType common to all members of a [[StatisticalPopulation]] or all cases within the scope of a [[StatisticalVariable]].
    '''
    class_: Literal['https://schema.org/StatisticalPopulation'] = Field( # type: ignore
        default='https://schema.org/StatisticalPopulation',
        alias='@type',
        serialization_alias='@type'
    )
    populationType: Optional[Union['_Class', List['_Class']]] = Field(
        default=None,
        validation_alias=AliasChoices(
            'genre',
            'https://schema.org/genre'
        ),
        serialization_alias='https://schema.org/genre'
    )
