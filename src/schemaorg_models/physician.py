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
from .medical_business import MedicalBusiness
from typing import TYPE_CHECKING
if TYPE_CHECKING:
    from .medical_therapy import MedicalTherapy
    from .hospital import Hospital
    from .medical_test import MedicalTest
    from .medical_procedure import MedicalProcedure
    from .medical_specialty import MedicalSpecialty
    from .category_code import CategoryCode

class Physician(MedicalBusiness):
    '''
    An individual physician or a physician's office considered as a [[MedicalOrganization]].

    Attributes:
        hospitalAffiliation: A hospital with which the physician or office is affiliated.
        availableService: A medical service available from this provider.
        usNPI: A <a href="https://en.wikipedia.org/wiki/National_Provider_Identifier">National Provider Identifier</a> (NPI) 
    is a unique 10-digit identification number issued to health care providers in the United States by the Centers for Medicare and Medicaid Services.
        occupationalCategory: A category describing the job, preferably using a term from a taxonomy such as [BLS O*NET-SOC](http://www.onetcenter.org/taxonomy.html), [ISCO-08](https://www.ilo.org/public/english/bureau/stat/isco/isco08/) or similar, with the property repeated for each applicable value. Ideally the taxonomy should be identified, and both the textual label and formal code for the category should be provided.\

Note: for historical reasons, any textual label and formal code provided as a literal may be assumed to be from O*NET-SOC.
        medicalSpecialty: A medical specialty of the provider.
    '''
    class_: Literal['https://schema.org/Physician'] = Field( # type: ignore
        default='https://schema.org/Physician',
        alias='@type',
        serialization_alias='@type'
    )
    hospitalAffiliation: Optional[Union['Hospital', List['Hospital']]] = Field(
        default=None,
        validation_alias=AliasChoices(
            'genre',
            'https://schema.org/genre'
        ),
        serialization_alias='https://schema.org/genre'
    )
    availableService: Optional[Union['MedicalProcedure', List['MedicalProcedure'], 'MedicalTherapy', List['MedicalTherapy'], 'MedicalTest', List['MedicalTest']]] = Field(
        default=None,
        validation_alias=AliasChoices(
            'genre',
            'https://schema.org/genre'
        ),
        serialization_alias='https://schema.org/genre'
    )
    usNPI: Optional[Union[str, List[str]]] = Field(
        default=None,
        validation_alias=AliasChoices(
            'genre',
            'https://schema.org/genre'
        ),
        serialization_alias='https://schema.org/genre'
    )
    occupationalCategory: Optional[Union['CategoryCode', List['CategoryCode'], str, List[str]]] = Field(
        default=None,
        validation_alias=AliasChoices(
            'genre',
            'https://schema.org/genre'
        ),
        serialization_alias='https://schema.org/genre'
    )
    medicalSpecialty: Optional[Union['MedicalSpecialty', List['MedicalSpecialty']]] = Field(
        default=None,
        validation_alias=AliasChoices(
            'genre',
            'https://schema.org/genre'
        ),
        serialization_alias='https://schema.org/genre'
    )
