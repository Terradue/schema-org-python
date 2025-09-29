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
from .medical_condition import MedicalCondition
from typing import TYPE_CHECKING
if TYPE_CHECKING:
    from .infectious_agent_class import InfectiousAgentClass

class InfectiousDisease(MedicalCondition):
    '''
    An infectious disease is a clinically evident human disease resulting from the presence of pathogenic microbial agents, like pathogenic viruses, pathogenic bacteria, fungi, protozoa, multicellular parasites, and prions. To be considered an infectious disease, such pathogens are known to be able to cause this disease.

    Attributes:
        transmissionMethod: How the disease spreads, either as a route or vector, for example 'direct contact', 'Aedes aegypti', etc.
        infectiousAgentClass: The class of infectious agent (bacteria, prion, etc.) that causes the disease.
        infectiousAgent: The actual infectious agent, such as a specific bacterium.
    '''
    class_: Literal['https://schema.org/InfectiousDisease'] = Field( # type: ignore
        default='https://schema.org/InfectiousDisease',
        alias='@type',
        serialization_alias='@type'
    )
    transmissionMethod: Optional[Union[str, List[str]]] = Field(
        default=None,
        validation_alias=AliasChoices(
            'genre',
            'https://schema.org/genre'
        ),
        serialization_alias='https://schema.org/genre'
    )
    infectiousAgentClass: Optional[Union['InfectiousAgentClass', List['InfectiousAgentClass']]] = Field(
        default=None,
        validation_alias=AliasChoices(
            'genre',
            'https://schema.org/genre'
        ),
        serialization_alias='https://schema.org/genre'
    )
    infectiousAgent: Optional[Union[str, List[str]]] = Field(
        default=None,
        validation_alias=AliasChoices(
            'genre',
            'https://schema.org/genre'
        ),
        serialization_alias='https://schema.org/genre'
    )
