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
from .service import Service
from typing import TYPE_CHECKING
if TYPE_CHECKING:
    from .organization import Organization
    from .administrative_area import AdministrativeArea

class GovernmentService(Service):
    '''
    A service provided by a government organization, e.g. food stamps, veterans benefits, etc.

    Attributes:
        jurisdiction: Indicates a legal jurisdiction, e.g. of some legislation, or where some government service is based.
        serviceOperator: The operating organization, if different from the provider.  This enables the representation of services that are provided by an organization, but operated by another organization like a subcontractor.
    '''
    class_: Literal['https://schema.org/GovernmentService'] = Field( # type: ignore
        default='https://schema.org/GovernmentService',
        alias='@type',
        serialization_alias='@type'
    )
    jurisdiction: Optional[Union[str, List[str], 'AdministrativeArea', List['AdministrativeArea']]] = Field(
        default=None,
        validation_alias=AliasChoices(
            'jurisdiction',
            'https://schema.org/jurisdiction'
        ),
        serialization_alias='https://schema.org/jurisdiction'
    )
    serviceOperator: Optional[Union['Organization', List['Organization']]] = Field(
        default=None,
        validation_alias=AliasChoices(
            'serviceOperator',
            'https://schema.org/serviceOperator'
        ),
        serialization_alias='https://schema.org/serviceOperator'
    )
