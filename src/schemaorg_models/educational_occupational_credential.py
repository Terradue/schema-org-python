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
from .creative_work import CreativeWork
from typing import TYPE_CHECKING
if TYPE_CHECKING:
    from .duration import Duration
    from .defined_term import DefinedTerm
    from .organization import Organization
    from .administrative_area import AdministrativeArea

class EducationalOccupationalCredential(CreativeWork):
    '''
    An educational or occupational credential. A diploma, academic degree, certification, qualification, badge, etc., that may be awarded to a person or other entity that meets the requirements defined by the credentialer.

    Attributes:
        recognizedBy: An organization that acknowledges the validity, value or utility of a credential. Note: recognition may include a process of quality assurance or accreditation.
        validFor: The duration of validity of a permit or similar thing.
        validIn: The geographic area where the item is valid. Applies for example to a [[Permit]], a [[Certification]], or an [[EducationalOccupationalCredential]]. 
        educationalLevel: The level in terms of progression through an educational or training context. Examples of educational levels include 'beginner', 'intermediate' or 'advanced', and formal sets of level indicators.
        competencyRequired: Knowledge, skill, ability or personal attribute that must be demonstrated by a person or other entity in order to do something such as earn an Educational Occupational Credential or understand a LearningResource.
        credentialCategory: The category or type of credential being described, for example "degree”, “certificate”, “badge”, or more specific term.
    '''
    class_: Literal['https://schema.org/EducationalOccupationalCredential'] = Field( # type: ignore
        default='https://schema.org/EducationalOccupationalCredential',
        alias='@type',
        serialization_alias='@type'
    )
    recognizedBy: Optional[Union['Organization', List['Organization']]] = Field(
        default=None,
        validation_alias=AliasChoices(
            'recognizedBy',
            'https://schema.org/recognizedBy'
        ),
        serialization_alias='https://schema.org/recognizedBy'
    )
    validFor: Optional[Union['Duration', List['Duration']]] = Field(
        default=None,
        validation_alias=AliasChoices(
            'validFor',
            'https://schema.org/validFor'
        ),
        serialization_alias='https://schema.org/validFor'
    )
    validIn: Optional[Union['AdministrativeArea', List['AdministrativeArea']]] = Field(
        default=None,
        validation_alias=AliasChoices(
            'validIn',
            'https://schema.org/validIn'
        ),
        serialization_alias='https://schema.org/validIn'
    )
    educationalLevel: Optional[Union[str, List[str], HttpUrl, List[HttpUrl], 'DefinedTerm', List['DefinedTerm']]] = Field(
        default=None,
        validation_alias=AliasChoices(
            'educationalLevel',
            'https://schema.org/educationalLevel'
        ),
        serialization_alias='https://schema.org/educationalLevel'
    )
    competencyRequired: Optional[Union['DefinedTerm', List['DefinedTerm'], str, List[str], HttpUrl, List[HttpUrl]]] = Field(
        default=None,
        validation_alias=AliasChoices(
            'competencyRequired',
            'https://schema.org/competencyRequired'
        ),
        serialization_alias='https://schema.org/competencyRequired'
    )
    credentialCategory: Optional[Union['DefinedTerm', List['DefinedTerm'], str, List[str], HttpUrl, List[HttpUrl]]] = Field(
        default=None,
        validation_alias=AliasChoices(
            'credentialCategory',
            'https://schema.org/credentialCategory'
        ),
        serialization_alias='https://schema.org/credentialCategory'
    )
