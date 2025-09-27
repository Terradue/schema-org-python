from typing import List, Literal, Optional, Union
from pydantic import AliasChoices, Field
from schemaorg_models.bio_chem_entity import BioChemEntity

from schemaorg_models.defined_term import DefinedTerm

class MolecularEntity(BioChemEntity):
    """
Any constitutionally or isotopically distinct atom, molecule, ion, ion pair, radical, radical ion, complex, conformer etc., identifiable as a separately distinguishable entity.
    """
    type_: Literal['https://schema.org/MolecularEntity'] = Field(default='https://schema.org/MolecularEntity', alias='@type', serialization_alias='http://www.w3.org/2000/01/rdf-schema#/Class') # type: ignore
    chemicalRole: Optional[Union[DefinedTerm, List[DefinedTerm]]] = Field(default=None, validation_alias=AliasChoices('chemicalRole', 'https://schema.org/chemicalRole'), serialization_alias='https://schema.org/chemicalRole')
    inChI: Optional[Union[str, List[str]]] = Field(default=None, validation_alias=AliasChoices('inChI', 'https://schema.org/inChI'), serialization_alias='https://schema.org/inChI')
    smiles: Optional[Union[str, List[str]]] = Field(default=None, validation_alias=AliasChoices('smiles', 'https://schema.org/smiles'), serialization_alias='https://schema.org/smiles')
    molecularWeight: Optional[Union[str, List[str], "QuantitativeValue", List["QuantitativeValue"]]] = Field(default=None, validation_alias=AliasChoices('molecularWeight', 'https://schema.org/molecularWeight'), serialization_alias='https://schema.org/molecularWeight')
    potentialUse: Optional[Union[DefinedTerm, List[DefinedTerm]]] = Field(default=None, validation_alias=AliasChoices('potentialUse', 'https://schema.org/potentialUse'), serialization_alias='https://schema.org/potentialUse')
    inChIKey: Optional[Union[str, List[str]]] = Field(default=None, validation_alias=AliasChoices('inChIKey', 'https://schema.org/inChIKey'), serialization_alias='https://schema.org/inChIKey')
    molecularFormula: Optional[Union[str, List[str]]] = Field(default=None, validation_alias=AliasChoices('molecularFormula', 'https://schema.org/molecularFormula'), serialization_alias='https://schema.org/molecularFormula')
    iupacName: Optional[Union[str, List[str]]] = Field(default=None, validation_alias=AliasChoices('iupacName', 'https://schema.org/iupacName'), serialization_alias='https://schema.org/iupacName')
    monoisotopicMolecularWeight: Optional[Union[str, List[str], "QuantitativeValue", List["QuantitativeValue"]]] = Field(default=None, validation_alias=AliasChoices('monoisotopicMolecularWeight', 'https://schema.org/monoisotopicMolecularWeight'), serialization_alias='https://schema.org/monoisotopicMolecularWeight')
