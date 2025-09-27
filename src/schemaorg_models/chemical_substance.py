from typing import List, Literal, Optional, Union
from pydantic import AliasChoices, Field
from schemaorg_models.bio_chem_entity import BioChemEntity

from schemaorg_models.defined_term import DefinedTerm

class ChemicalSubstance(BioChemEntity):
    """
A chemical substance is 'a portion of matter of constant composition, composed of molecular entities of the same type or of different types' (source: [ChEBI:59999](https://www.ebi.ac.uk/chebi/searchId.do?chebiId=59999)).
    """
    type_: Literal['https://schema.org/ChemicalSubstance'] = Field(default='https://schema.org/ChemicalSubstance', alias='@type', serialization_alias='@type') # type: ignore
    chemicalComposition: Optional[Union[str, List[str]]] = Field(default=None, validation_alias=AliasChoices('chemicalComposition', 'https://schema.org/chemicalComposition'), serialization_alias='https://schema.org/chemicalComposition')
    chemicalRole: Optional[Union[DefinedTerm, List[DefinedTerm]]] = Field(default=None, validation_alias=AliasChoices('chemicalRole', 'https://schema.org/chemicalRole'), serialization_alias='https://schema.org/chemicalRole')
    potentialUse: Optional[Union[DefinedTerm, List[DefinedTerm]]] = Field(default=None, validation_alias=AliasChoices('potentialUse', 'https://schema.org/potentialUse'), serialization_alias='https://schema.org/potentialUse')
