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
    from .thing import Thing
    from .superficial_anatomy import SuperficialAnatomy
    from .physical_activity_category import PhysicalActivityCategory
    from .category_code import CategoryCode
    from .anatomical_structure import AnatomicalStructure
    from .anatomical_system import AnatomicalSystem

class PhysicalActivity(LifestyleModification):
    '''
    Any bodily activity that enhances or maintains physical fitness and overall health and wellness. Includes activity that is part of daily living and routine, structured exercise, and exercise prescribed as part of a medical treatment or recovery plan.

    Attributes:
        pathophysiology: Changes in the normal mechanical, physical, and biochemical functions that are associated with this activity or condition.
        category: A category for the item. Greater signs or slashes can be used to informally indicate a category hierarchy.
        epidemiology: The characteristics of associated patients, such as age, gender, race etc.
        associatedAnatomy: The anatomy of the underlying organ system or structures associated with this entity.
    '''
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
    category: Optional[Union['PhysicalActivityCategory', List['PhysicalActivityCategory'], 'CategoryCode', List['CategoryCode'], str, List[str], 'Thing', List['Thing'], HttpUrl, List[HttpUrl]]] = Field(
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
    associatedAnatomy: Optional[Union['AnatomicalSystem', List['AnatomicalSystem'], 'SuperficialAnatomy', List['SuperficialAnatomy'], 'AnatomicalStructure', List['AnatomicalStructure']]] = Field(
        default=None,
        validation_alias=AliasChoices(
            'associatedAnatomy',
            'https://schema.org/associatedAnatomy'
        ),
        serialization_alias='https://schema.org/associatedAnatomy'
    )
