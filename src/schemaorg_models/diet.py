from __future__ import annotations
from pydantic import (
    AliasChoices,
    Field
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
    """
A strategy of regulating the intake of food to achieve or maintain a specific health-related goal.
    """
    class_: Literal['https://schema.org/Diet'] = Field( # type: ignore
        default='https://schema.org/Diet',
        alias='@type',
        serialization_alias='@type'
    )
    risks: Optional[Union[str, List[str]]] = Field(
        default=None,
        validation_alias=AliasChoices(
            'risks',
            'https://schema.org/risks'
        ),
        serialization_alias='https://schema.org/risks'
    )
    physiologicalBenefits: Optional[Union[str, List[str]]] = Field(
        default=None,
        validation_alias=AliasChoices(
            'physiologicalBenefits',
            'https://schema.org/physiologicalBenefits'
        ),
        serialization_alias='https://schema.org/physiologicalBenefits'
    )
    dietFeatures: Optional[Union[str, List[str]]] = Field(
        default=None,
        validation_alias=AliasChoices(
            'dietFeatures',
            'https://schema.org/dietFeatures'
        ),
        serialization_alias='https://schema.org/dietFeatures'
    )
    expertConsiderations: Optional[Union[str, List[str]]] = Field(
        default=None,
        validation_alias=AliasChoices(
            'expertConsiderations',
            'https://schema.org/expertConsiderations'
        ),
        serialization_alias='https://schema.org/expertConsiderations'
    )
    endorsers: Optional[Union["Organization", List["Organization"], "Person", List["Person"]]] = Field(
        default=None,
        validation_alias=AliasChoices(
            'endorsers',
            'https://schema.org/endorsers'
        ),
        serialization_alias='https://schema.org/endorsers'
    )
