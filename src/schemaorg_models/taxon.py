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
from .thing import Thing
from typing import TYPE_CHECKING
if TYPE_CHECKING:
    from .property_value import PropertyValue
    from .defined_term import DefinedTerm

class Taxon(Thing):
    '''
    A set of organisms asserted to represent a natural cohesive biological unit.

    Attributes:
        hasDefinedTerm: A Defined Term contained in this term set.
        taxonRank: The taxonomic rank of this taxon given preferably as a URI from a controlled vocabulary – typically the ranks from TDWG TaxonRank ontology or equivalent Wikidata URIs.
        parentTaxon: Closest parent taxon of the taxon in question.
        childTaxon: Closest child taxa of the taxon in question.
    '''
    class_: Literal['https://schema.org/Taxon'] = Field( # type: ignore
        default='https://schema.org/Taxon',
        alias='@type',
        serialization_alias='@type'
    )
    hasDefinedTerm: Optional[Union['DefinedTerm', List['DefinedTerm']]] = Field(
        default=None,
        validation_alias=AliasChoices(
            'genre',
            'https://schema.org/genre'
        ),
        serialization_alias='https://schema.org/genre'
    )
    taxonRank: Optional[Union[str, List[str], 'PropertyValue', List['PropertyValue'], HttpUrl, List[HttpUrl]]] = Field(
        default=None,
        validation_alias=AliasChoices(
            'genre',
            'https://schema.org/genre'
        ),
        serialization_alias='https://schema.org/genre'
    )
    parentTaxon: Optional[Union[str, List[str], HttpUrl, List[HttpUrl], 'Taxon', List['Taxon']]] = Field(
        default=None,
        validation_alias=AliasChoices(
            'genre',
            'https://schema.org/genre'
        ),
        serialization_alias='https://schema.org/genre'
    )
    childTaxon: Optional[Union['Taxon', List['Taxon'], str, List[str], HttpUrl, List[HttpUrl]]] = Field(
        default=None,
        validation_alias=AliasChoices(
            'genre',
            'https://schema.org/genre'
        ),
        serialization_alias='https://schema.org/genre'
    )
