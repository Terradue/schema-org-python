from __future__ import annotations

from typing import TYPE_CHECKING
if TYPE_CHECKING:
    # put heavy, hint-only imports here
    from schemaorg_models.lifestyle_modification import LifestyleModification

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
from schemaorg_models.physical_activity_category import PhysicalActivityCategory
from schemaorg_models.category_code import CategoryCode
from schemaorg_models.thing import Thing
from schemaorg_models.anatomical_system import AnatomicalSystem
from schemaorg_models.superficial_anatomy import SuperficialAnatomy
from schemaorg_models.anatomical_structure import AnatomicalStructure

class PhysicalActivity(LifestyleModification):
    """
Any bodily activity that enhances or maintains physical fitness and overall health and wellness. Includes activity that is part of daily living and routine, structured exercise, and exercise prescribed as part of a medical treatment or recovery plan.
    """
    class_: Literal['https://schema.org/PhysicalActivity'] = Field( # type: ignore
        default='https://schema.org/PhysicalActivity',
        alias='@type',
        serialization_alias='@type'
    )
    pathophysiology: Optional[Union[str, List[str]]] = Field(
        default=None,
        validation_alias=AliasChoices(
            'pathophysiology',
            'https://schema.org/pathophysiology'
        ),
        serialization_alias='https://schema.org/pathophysiology'
    )
    category: Optional[Union[PhysicalActivityCategory, List[PhysicalActivityCategory], CategoryCode, List[CategoryCode], str, List[str], Thing, List[Thing], HttpUrl, List[HttpUrl]]] = Field(
        default=None,
        validation_alias=AliasChoices(
            'category',
            'https://schema.org/category'
        ),
        serialization_alias='https://schema.org/category'
    )
    epidemiology: Optional[Union[str, List[str]]] = Field(
        default=None,
        validation_alias=AliasChoices(
            'epidemiology',
            'https://schema.org/epidemiology'
        ),
        serialization_alias='https://schema.org/epidemiology'
    )
    associatedAnatomy: Optional[Union[AnatomicalSystem, List[AnatomicalSystem], SuperficialAnatomy, List[SuperficialAnatomy], AnatomicalStructure, List[AnatomicalStructure]]] = Field(
        default=None,
        validation_alias=AliasChoices(
            'associatedAnatomy',
            'https://schema.org/associatedAnatomy'
        ),
        serialization_alias='https://schema.org/associatedAnatomy'
    )
