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
from .lifestyle_modification import LifestyleModification
from typing import TYPE_CHECKING
if TYPE_CHECKING:
    from .organization import Organization
    from .person import Person

class Diet(LifestyleModification):
    '''
    A strategy of regulating the intake of food to achieve or maintain a specific health-related goal.

    Attributes:
        risks: Specific physiologic risks associated to the diet plan.
        physiologicalBenefits: Specific physiologic benefits associated to the plan.
        dietFeatures: Nutritional information specific to the dietary plan. May include dietary recommendations on what foods to avoid, what foods to consume, and specific alterations/deviations from the USDA or other regulatory body's approved dietary guidelines.
        expertConsiderations: Medical expert advice related to the plan.
        endorsers: People or organizations that endorse the plan.
    '''
    class_: Literal['https://schema.org/Diet'] = Field( # type: ignore
        default='https://schema.org/Diet',
        alias='@type',
        serialization_alias='@type'
    )
    risks: Optional[Union[str, List[str]]] = Field(
        default=None,
        validation_alias=AliasChoices(
            'genre',
            'https://schema.org/genre'
        ),
        serialization_alias='https://schema.org/genre'
    )
    physiologicalBenefits: Optional[Union[str, List[str]]] = Field(
        default=None,
        validation_alias=AliasChoices(
            'genre',
            'https://schema.org/genre'
        ),
        serialization_alias='https://schema.org/genre'
    )
    dietFeatures: Optional[Union[str, List[str]]] = Field(
        default=None,
        validation_alias=AliasChoices(
            'genre',
            'https://schema.org/genre'
        ),
        serialization_alias='https://schema.org/genre'
    )
    expertConsiderations: Optional[Union[str, List[str]]] = Field(
        default=None,
        validation_alias=AliasChoices(
            'genre',
            'https://schema.org/genre'
        ),
        serialization_alias='https://schema.org/genre'
    )
    endorsers: Optional[Union['Organization', List['Organization'], 'Person', List['Person']]] = Field(
        default=None,
        validation_alias=AliasChoices(
            'genre',
            'https://schema.org/genre'
        ),
        serialization_alias='https://schema.org/genre'
    )
