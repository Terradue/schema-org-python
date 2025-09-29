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
    from .defined_term import DefinedTerm
    from .quantitative_value import QuantitativeValue

class MolecularEntity(BioChemEntity):
    '''
    Any constitutionally or isotopically distinct atom, molecule, ion, ion pair, radical, radical ion, complex, conformer etc., identifiable as a separately distinguishable entity.

    Attributes:
        chemicalRole: A role played by the BioChemEntity within a chemical context.
        inChI: Non-proprietary identifier for molecular entity that can be used in printed and electronic data sources thus enabling easier linking of diverse data compilations.
        smiles: A specification in form of a line notation for describing the structure of chemical species using short ASCII strings.  Double bond stereochemistry \ indicators may need to be escaped in the string in formats where the backslash is an escape character.
        molecularWeight: This is the molecular weight of the entity being described, not of the parent. Units should be included in the form '&lt;Number&gt; &lt;unit&gt;', for example '12 amu' or as '&lt;QuantitativeValue&gt;.
        potentialUse: Intended use of the BioChemEntity by humans.
        inChIKey: InChIKey is a hashed version of the full InChI (using the SHA-256 algorithm).
        molecularFormula: The empirical formula is the simplest whole number ratio of all the atoms in a molecule.
        iupacName: Systematic method of naming chemical compounds as recommended by the International Union of Pure and Applied Chemistry (IUPAC).
        monoisotopicMolecularWeight: The monoisotopic mass is the sum of the masses of the atoms in a molecule using the unbound, ground-state, rest mass of the principal (most abundant) isotope for each element instead of the isotopic average mass. Please include the units in the form '&lt;Number&gt; &lt;unit&gt;', for example '770.230488 g/mol' or as '&lt;QuantitativeValue&gt;.
    '''
    class_: Literal['https://schema.org/MolecularEntity'] = Field( # type: ignore
        default='https://schema.org/MolecularEntity',
        alias='@type',
        serialization_alias='@type'
    )
    chemicalRole: Optional[Union['DefinedTerm', List['DefinedTerm']]] = Field(
        default=None,
        validation_alias=AliasChoices(
            'chemicalRole',
            'https://schema.org/chemicalRole'
        ),
        serialization_alias='https://schema.org/chemicalRole'
    )
    inChI: Optional[Union[str, List[str]]] = Field(
        default=None,
        validation_alias=AliasChoices(
            'inChI',
            'https://schema.org/inChI'
        ),
        serialization_alias='https://schema.org/inChI'
    )
    smiles: Optional[Union[str, List[str]]] = Field(
        default=None,
        validation_alias=AliasChoices(
            'smiles',
            'https://schema.org/smiles'
        ),
        serialization_alias='https://schema.org/smiles'
    )
    molecularWeight: Optional[Union[str, List[str], 'QuantitativeValue', List['QuantitativeValue']]] = Field(
        default=None,
        validation_alias=AliasChoices(
            'molecularWeight',
            'https://schema.org/molecularWeight'
        ),
        serialization_alias='https://schema.org/molecularWeight'
    )
    potentialUse: Optional[Union['DefinedTerm', List['DefinedTerm']]] = Field(
        default=None,
        validation_alias=AliasChoices(
            'potentialUse',
            'https://schema.org/potentialUse'
        ),
        serialization_alias='https://schema.org/potentialUse'
    )
    inChIKey: Optional[Union[str, List[str]]] = Field(
        default=None,
        validation_alias=AliasChoices(
            'inChIKey',
            'https://schema.org/inChIKey'
        ),
        serialization_alias='https://schema.org/inChIKey'
    )
    molecularFormula: Optional[Union[str, List[str]]] = Field(
        default=None,
        validation_alias=AliasChoices(
            'molecularFormula',
            'https://schema.org/molecularFormula'
        ),
        serialization_alias='https://schema.org/molecularFormula'
    )
    iupacName: Optional[Union[str, List[str]]] = Field(
        default=None,
        validation_alias=AliasChoices(
            'iupacName',
            'https://schema.org/iupacName'
        ),
        serialization_alias='https://schema.org/iupacName'
    )
    monoisotopicMolecularWeight: Optional[Union[str, List[str], 'QuantitativeValue', List['QuantitativeValue']]] = Field(
        default=None,
        validation_alias=AliasChoices(
            'monoisotopicMolecularWeight',
            'https://schema.org/monoisotopicMolecularWeight'
        ),
        serialization_alias='https://schema.org/monoisotopicMolecularWeight'
    )
