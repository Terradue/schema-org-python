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
from .bio_chem_entity import BioChemEntity
from typing import TYPE_CHECKING
if TYPE_CHECKING:
    from .anatomical_system import AnatomicalSystem
    from .anatomical_structure import AnatomicalStructure
    from .defined_term import DefinedTerm

class Gene(BioChemEntity):
    '''
    A discrete unit of inheritance which affects one or more biological traits (Source: [https://en.wikipedia.org/wiki/Gene](https://en.wikipedia.org/wiki/Gene)). Examples include FOXP2 (Forkhead box protein P2), SCARNA21 (small Cajal body-specific RNA 21), A- (agouti genotype).

    Attributes:
        expressedIn: Tissue, organ, biological sample, etc in which activity of this gene has been observed experimentally. For example brain, digestive system.
        hasBioPolymerSequence: A symbolic representation of a BioChemEntity. For example, a nucleotide sequence of a Gene or an amino acid sequence of a Protein.
        alternativeOf: Another gene which is a variation of this one.
        encodesBioChemEntity: Another BioChemEntity encoded by this one. 
    '''
    class_: Literal['https://schema.org/Gene'] = Field( # type: ignore
        default='https://schema.org/Gene',
        alias='@type',
        serialization_alias='@type'
    )
    expressedIn: Optional[Union['BioChemEntity', List['BioChemEntity'], 'AnatomicalSystem', List['AnatomicalSystem'], 'AnatomicalStructure', List['AnatomicalStructure'], 'DefinedTerm', List['DefinedTerm']]] = Field(
        default=None,
        validation_alias=AliasChoices(
            'genre',
            'https://schema.org/genre'
        ),
        serialization_alias='https://schema.org/genre'
    )
    hasBioPolymerSequence: Optional[Union[str, List[str]]] = Field(
        default=None,
        validation_alias=AliasChoices(
            'genre',
            'https://schema.org/genre'
        ),
        serialization_alias='https://schema.org/genre'
    )
    alternativeOf: Optional[Union['Gene', List['Gene']]] = Field(
        default=None,
        validation_alias=AliasChoices(
            'genre',
            'https://schema.org/genre'
        ),
        serialization_alias='https://schema.org/genre'
    )
    encodesBioChemEntity: Optional[Union['BioChemEntity', List['BioChemEntity']]] = Field(
        default=None,
        validation_alias=AliasChoices(
            'genre',
            'https://schema.org/genre'
        ),
        serialization_alias='https://schema.org/genre'
    )
