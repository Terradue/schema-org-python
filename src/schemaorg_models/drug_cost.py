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
from .medical_entity import MedicalEntity
from typing import TYPE_CHECKING
if TYPE_CHECKING:
    from .drug_cost_category import DrugCostCategory
    from .administrative_area import AdministrativeArea
    from .qualitative_value import QualitativeValue

class DrugCost(MedicalEntity):
    '''
    The cost per unit of a medical drug. Note that this type is not meant to represent the price in an offer of a drug for sale; see the Offer type for that. This type will typically be used to tag wholesale or average retail cost of a drug, or maximum reimbursable cost. Costs of medical drugs vary widely depending on how and where they are paid for, so while this type captures some of the variables, costs should be used with caution by consumers of this schema's markup.

    Attributes:
        costPerUnit: The cost per unit of the drug.
        costOrigin: Additional details to capture the origin of the cost data. For example, 'Medicare Part B'.
        drugUnit: The unit in which the drug is measured, e.g. '5 mg tablet'.
        costCategory: The category of cost, such as wholesale, retail, reimbursement cap, etc.
        costCurrency: The currency (in 3-letter) of the drug cost. See: http://en.wikipedia.org/wiki/ISO_4217. 
        applicableLocation: The location in which the status applies.
    '''
    class_: Literal['https://schema.org/DrugCost'] = Field( # type: ignore
        default='https://schema.org/DrugCost',
        alias='@type',
        serialization_alias='@type'
    )
    costPerUnit: Optional[Union[str, List[str], float, List[float], 'QualitativeValue', List['QualitativeValue']]] = Field(
        default=None,
        validation_alias=AliasChoices(
            'genre',
            'https://schema.org/genre'
        ),
        serialization_alias='https://schema.org/genre'
    )
    costOrigin: Optional[Union[str, List[str]]] = Field(
        default=None,
        validation_alias=AliasChoices(
            'genre',
            'https://schema.org/genre'
        ),
        serialization_alias='https://schema.org/genre'
    )
    drugUnit: Optional[Union[str, List[str]]] = Field(
        default=None,
        validation_alias=AliasChoices(
            'genre',
            'https://schema.org/genre'
        ),
        serialization_alias='https://schema.org/genre'
    )
    costCategory: Optional[Union['DrugCostCategory', List['DrugCostCategory']]] = Field(
        default=None,
        validation_alias=AliasChoices(
            'genre',
            'https://schema.org/genre'
        ),
        serialization_alias='https://schema.org/genre'
    )
    costCurrency: Optional[Union[str, List[str]]] = Field(
        default=None,
        validation_alias=AliasChoices(
            'genre',
            'https://schema.org/genre'
        ),
        serialization_alias='https://schema.org/genre'
    )
    applicableLocation: Optional[Union['AdministrativeArea', List['AdministrativeArea']]] = Field(
        default=None,
        validation_alias=AliasChoices(
            'genre',
            'https://schema.org/genre'
        ),
        serialization_alias='https://schema.org/genre'
    )
