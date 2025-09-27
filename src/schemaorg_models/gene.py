from typing import List, Literal, Optional, Union
from pydantic import AliasChoices, Field
from schemaorg_models.bio_chem_entity import BioChemEntity

from schemaorg_models.bio_chem_entity import BioChemEntity
from schemaorg_models.anatomical_system import AnatomicalSystem
from schemaorg_models.anatomical_structure import AnatomicalStructure
from schemaorg_models.defined_term import DefinedTerm

class Gene(BioChemEntity):
    """
A discrete unit of inheritance which affects one or more biological traits (Source: [https://en.wikipedia.org/wiki/Gene](https://en.wikipedia.org/wiki/Gene)). Examples include FOXP2 (Forkhead box protein P2), SCARNA21 (small Cajal body-specific RNA 21), A- (agouti genotype).
    """
    type_: Literal['https://schema.org/Gene'] = Field(default='https://schema.org/Gene', alias='@type', serialization_alias='@type') # type: ignore
    expressedIn: Optional[Union[BioChemEntity, List[BioChemEntity], AnatomicalSystem, List[AnatomicalSystem], AnatomicalStructure, List[AnatomicalStructure], DefinedTerm, List[DefinedTerm]]] = Field(default=None, validation_alias=AliasChoices('expressedIn', 'https://schema.org/expressedIn'), serialization_alias='https://schema.org/expressedIn')
    hasBioPolymerSequence: Optional[Union[str, List[str]]] = Field(default=None, validation_alias=AliasChoices('hasBioPolymerSequence', 'https://schema.org/hasBioPolymerSequence'), serialization_alias='https://schema.org/hasBioPolymerSequence')
    alternativeOf: Optional[Union["Gene", List["Gene"]]] = Field(default=None, validation_alias=AliasChoices('alternativeOf', 'https://schema.org/alternativeOf'), serialization_alias='https://schema.org/alternativeOf')
    encodesBioChemEntity: Optional[Union[BioChemEntity, List[BioChemEntity]]] = Field(default=None, validation_alias=AliasChoices('encodesBioChemEntity', 'https://schema.org/encodesBioChemEntity'), serialization_alias='https://schema.org/encodesBioChemEntity')
