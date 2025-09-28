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
from .educational_occupational_program import EducationalOccupationalProgram
from typing import TYPE_CHECKING
if TYPE_CHECKING:
    from .category_code import CategoryCode
    from .monetary_amount_distribution import MonetaryAmountDistribution

class WorkBasedProgram(EducationalOccupationalProgram):
    """
A program with both an educational and employment component. Typically based at a workplace and structured around work-based learning, with the aim of instilling competencies related to an occupation. WorkBasedProgram is used to distinguish programs such as apprenticeships from school, college or other classroom based educational programs.
    """
    class_: Literal['https://schema.org/WorkBasedProgram'] = Field( # type: ignore
        default='https://schema.org/WorkBasedProgram',
        alias='@type',
        serialization_alias='@type'
    )
    trainingSalary: Optional[Union[MonetaryAmountDistribution, List[MonetaryAmountDistribution]]] = Field(
        default=None,
        validation_alias=AliasChoices(
            'trainingSalary',
            'https://schema.org/trainingSalary'
        ),
        serialization_alias='https://schema.org/trainingSalary'
    )
    occupationalCategory: Optional[Union[CategoryCode, List[CategoryCode], str, List[str]]] = Field(
        default=None,
        validation_alias=AliasChoices(
            'occupationalCategory',
            'https://schema.org/occupationalCategory'
        ),
        serialization_alias='https://schema.org/occupationalCategory'
    )
