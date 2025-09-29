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
from .educational_occupational_program import EducationalOccupationalProgram
from typing import TYPE_CHECKING
if TYPE_CHECKING:
    from .monetary_amount_distribution import MonetaryAmountDistribution
    from .category_code import CategoryCode

class WorkBasedProgram(EducationalOccupationalProgram):
    '''
    A program with both an educational and employment component. Typically based at a workplace and structured around work-based learning, with the aim of instilling competencies related to an occupation. WorkBasedProgram is used to distinguish programs such as apprenticeships from school, college or other classroom based educational programs.

    Attributes:
        trainingSalary: The estimated salary earned while in the program.
        occupationalCategory: A category describing the job, preferably using a term from a taxonomy such as [BLS O*NET-SOC](http://www.onetcenter.org/taxonomy.html), [ISCO-08](https://www.ilo.org/public/english/bureau/stat/isco/isco08/) or similar, with the property repeated for each applicable value. Ideally the taxonomy should be identified, and both the textual label and formal code for the category should be provided.\

Note: for historical reasons, any textual label and formal code provided as a literal may be assumed to be from O*NET-SOC.
    '''
    class_: Literal['https://schema.org/WorkBasedProgram'] = Field( # type: ignore
        default='https://schema.org/WorkBasedProgram',
        alias='@type',
        serialization_alias='@type'
    )
    trainingSalary: Optional[Union['MonetaryAmountDistribution', List['MonetaryAmountDistribution']]] = Field(
        default=None,
        validation_alias=AliasChoices(
            'trainingSalary',
            'https://schema.org/trainingSalary'
        ),
        serialization_alias='https://schema.org/trainingSalary'
    )
    occupationalCategory: Optional[Union['CategoryCode', List['CategoryCode'], str, List[str]]] = Field(
        default=None,
        validation_alias=AliasChoices(
            'occupationalCategory',
            'https://schema.org/occupationalCategory'
        ),
        serialization_alias='https://schema.org/occupationalCategory'
    )
