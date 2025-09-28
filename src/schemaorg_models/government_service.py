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
from .administrative_area import AdministrativeArea
from .service import Service
from .organization import Organization

class GovernmentService(Service):
    """
A service provided by a government organization, e.g. food stamps, veterans benefits, etc.
    """
    class_: Literal['https://schema.org/GovernmentService'] = Field( # type: ignore
        default='https://schema.org/GovernmentService',
        alias='@type',
        serialization_alias='@type'
    )
    jurisdiction: Optional[Union[str, List[str], AdministrativeArea, List[AdministrativeArea]]] = Field(
        default=None,
        validation_alias=AliasChoices(
            'jurisdiction',
            'https://schema.org/jurisdiction'
        ),
        serialization_alias='https://schema.org/jurisdiction'
    )
    serviceOperator: Optional[Union[Organization, List[Organization]]] = Field(
        default=None,
        validation_alias=AliasChoices(
            'serviceOperator',
            'https://schema.org/serviceOperator'
        ),
        serialization_alias='https://schema.org/serviceOperator'
    )
