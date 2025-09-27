from typing import List, Literal, Optional, Union
from datetime import date
from pydantic import field_serializer, AliasChoices, Field, HttpUrl
from schemaorg_models.creative_work import CreativeWork

from schemaorg_models.person import Person
from schemaorg_models.organization import Organization
from schemaorg_models.administrative_area import AdministrativeArea

class Legislation(CreativeWork):
    """
A legal document such as an act, decree, bill, etc. (enforceable or not) or a component of a legal act (like an article).
    """
    type_: Literal['https://schema.org/Legislation'] = Field(default='https://schema.org/Legislation', alias='@type', serialization_alias='@type') # type: ignore
    legislationApplies: Optional[Union["Legislation", List["Legislation"]]] = Field(default=None, validation_alias=AliasChoices('legislationApplies', 'https://schema.org/legislationApplies'), serialization_alias='https://schema.org/legislationApplies')
    legislationCountersignedBy: Optional[Union[Person, List[Person], Organization, List[Organization]]] = Field(default=None, validation_alias=AliasChoices('legislationCountersignedBy', 'https://schema.org/legislationCountersignedBy'), serialization_alias='https://schema.org/legislationCountersignedBy')
    legislationChanges: Optional[Union["Legislation", List["Legislation"]]] = Field(default=None, validation_alias=AliasChoices('legislationChanges', 'https://schema.org/legislationChanges'), serialization_alias='https://schema.org/legislationChanges')
    legislationCommences: Optional[Union["Legislation", List["Legislation"]]] = Field(default=None, validation_alias=AliasChoices('legislationCommences', 'https://schema.org/legislationCommences'), serialization_alias='https://schema.org/legislationCommences')
    legislationRepeals: Optional[Union["Legislation", List["Legislation"]]] = Field(default=None, validation_alias=AliasChoices('legislationRepeals', 'https://schema.org/legislationRepeals'), serialization_alias='https://schema.org/legislationRepeals')
    legislationType: Optional[Union[str, List[str], "CategoryCode", List["CategoryCode"]]] = Field(default=None, validation_alias=AliasChoices('legislationType', 'https://schema.org/legislationType'), serialization_alias='https://schema.org/legislationType')
    jurisdiction: Optional[Union[str, List[str], AdministrativeArea, List[AdministrativeArea]]] = Field(default=None, validation_alias=AliasChoices('jurisdiction', 'https://schema.org/jurisdiction'), serialization_alias='https://schema.org/jurisdiction')
    legislationJurisdiction: Optional[Union[str, List[str], AdministrativeArea, List[AdministrativeArea]]] = Field(default=None, validation_alias=AliasChoices('legislationJurisdiction', 'https://schema.org/legislationJurisdiction'), serialization_alias='https://schema.org/legislationJurisdiction')
    legislationCorrects: Optional[Union["Legislation", List["Legislation"]]] = Field(default=None, validation_alias=AliasChoices('legislationCorrects', 'https://schema.org/legislationCorrects'), serialization_alias='https://schema.org/legislationCorrects')
    legislationTransposes: Optional[Union["Legislation", List["Legislation"]]] = Field(default=None, validation_alias=AliasChoices('legislationTransposes', 'https://schema.org/legislationTransposes'), serialization_alias='https://schema.org/legislationTransposes')
    legislationDate: Optional[Union[date, List[date]]] = Field(default=None, validation_alias=AliasChoices('legislationDate', 'https://schema.org/legislationDate'), serialization_alias='https://schema.org/legislationDate')
    legislationEnsuresImplementationOf: Optional[Union["Legislation", List["Legislation"]]] = Field(default=None, validation_alias=AliasChoices('legislationEnsuresImplementationOf', 'https://schema.org/legislationEnsuresImplementationOf'), serialization_alias='https://schema.org/legislationEnsuresImplementationOf')
    legislationPassedBy: Optional[Union[Person, List[Person], Organization, List[Organization]]] = Field(default=None, validation_alias=AliasChoices('legislationPassedBy', 'https://schema.org/legislationPassedBy'), serialization_alias='https://schema.org/legislationPassedBy')
    legislationConsolidates: Optional[Union["Legislation", List["Legislation"]]] = Field(default=None, validation_alias=AliasChoices('legislationConsolidates', 'https://schema.org/legislationConsolidates'), serialization_alias='https://schema.org/legislationConsolidates')
    legislationDateOfApplicability: Optional[Union[date, List[date]]] = Field(default=None, validation_alias=AliasChoices('legislationDateOfApplicability', 'https://schema.org/legislationDateOfApplicability'), serialization_alias='https://schema.org/legislationDateOfApplicability')
    legislationIdentifier: Optional[Union[HttpUrl, List[HttpUrl], str, List[str]]] = Field(default=None, validation_alias=AliasChoices('legislationIdentifier', 'https://schema.org/legislationIdentifier'), serialization_alias='https://schema.org/legislationIdentifier')
    @field_serializer('legislationIdentifier')
    def legislationIdentifier2str(self, val) -> str | List[str]:
        def _to_str(value):
            if isinstance(value, HttpUrl):
                return str(value)
            return value

        if isinstance(val, list):
            return [_to_str(i) for i in val]
        return _to_str(val)

    legislationLegalForce: Optional[Union["LegalForceStatus", List["LegalForceStatus"]]] = Field(default=None, validation_alias=AliasChoices('legislationLegalForce', 'https://schema.org/legislationLegalForce'), serialization_alias='https://schema.org/legislationLegalForce')
    legislationAmends: Optional[Union["Legislation", List["Legislation"]]] = Field(default=None, validation_alias=AliasChoices('legislationAmends', 'https://schema.org/legislationAmends'), serialization_alias='https://schema.org/legislationAmends')
    legislationDateVersion: Optional[Union[date, List[date]]] = Field(default=None, validation_alias=AliasChoices('legislationDateVersion', 'https://schema.org/legislationDateVersion'), serialization_alias='https://schema.org/legislationDateVersion')
    legislationResponsible: Optional[Union[Person, List[Person], Organization, List[Organization]]] = Field(default=None, validation_alias=AliasChoices('legislationResponsible', 'https://schema.org/legislationResponsible'), serialization_alias='https://schema.org/legislationResponsible')
