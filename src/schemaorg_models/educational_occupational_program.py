from typing import Union, List, Optional
from datetime import date, datetime
from pydantic import field_serializer, AliasChoices, Field, HttpUrl
from schemaorg_models.intangible import Intangible

from schemaorg_models.person import Person
from schemaorg_models.organization import Organization

class EducationalOccupationalProgram(Intangible):
    """
A program offered by an institution which determines the learning progress to achieve an outcome, usually a credential like a degree or certificate. This would define a discrete set of opportunities (e.g., job, courses) that together constitute a program with a clear start, end, set of requirements, and transition to a new occupational opportunity (e.g., a job), or sometimes a higher educational opportunity (e.g., an advanced degree).
    """
    timeToComplete: Optional[Union["Duration", List["Duration"]]] = Field(default=None,validation_alias=AliasChoices('timeToComplete', 'https://schema.org/timeToComplete'),serialization_alias='https://schema.org/timeToComplete')
    programType: Optional[Union[str, List[str], "DefinedTerm", List["DefinedTerm"]]] = Field(default=None,validation_alias=AliasChoices('programType', 'https://schema.org/programType'),serialization_alias='https://schema.org/programType')
    applicationStartDate: Optional[Union[date, List[date]]] = Field(default=None,validation_alias=AliasChoices('applicationStartDate', 'https://schema.org/applicationStartDate'),serialization_alias='https://schema.org/applicationStartDate')
    offers: Optional[Union["Demand", List["Demand"], "Offer", List["Offer"]]] = Field(default=None,validation_alias=AliasChoices('offers', 'https://schema.org/offers'),serialization_alias='https://schema.org/offers')
    dayOfWeek: Optional[Union["DayOfWeek", List["DayOfWeek"]]] = Field(default=None,validation_alias=AliasChoices('dayOfWeek', 'https://schema.org/dayOfWeek'),serialization_alias='https://schema.org/dayOfWeek')
    applicationDeadline: Optional[Union[str, List[str], date, List[date]]] = Field(default=None,validation_alias=AliasChoices('applicationDeadline', 'https://schema.org/applicationDeadline'),serialization_alias='https://schema.org/applicationDeadline')
    typicalCreditsPerTerm: Optional[Union[int, List[int], "StructuredValue", List["StructuredValue"]]] = Field(default=None,validation_alias=AliasChoices('typicalCreditsPerTerm', 'https://schema.org/typicalCreditsPerTerm'),serialization_alias='https://schema.org/typicalCreditsPerTerm')
    educationalCredentialAwarded: Optional[Union["EducationalOccupationalCredential", List["EducationalOccupationalCredential"], str, List[str], HttpUrl, List[HttpUrl]]] = Field(default=None,validation_alias=AliasChoices('educationalCredentialAwarded', 'https://schema.org/educationalCredentialAwarded'),serialization_alias='https://schema.org/educationalCredentialAwarded')
    @field_serializer('educationalCredentialAwarded')
    def educationalCredentialAwarded2str(self, val) -> str | List[str]:
        def _to_str(value):
            if isinstance(value, HttpUrl):
                return str(value)
            return value

        if isinstance(val, list):
            return [_to_str(i) for i in val]
        return _to_str(val)

    endDate: Optional[Union[datetime, List[datetime], date, List[date]]] = Field(default=None,validation_alias=AliasChoices('endDate', 'https://schema.org/endDate'),serialization_alias='https://schema.org/endDate')
    provider: Optional[Union[Person, List[Person], Organization, List[Organization]]] = Field(default=None,validation_alias=AliasChoices('provider', 'https://schema.org/provider'),serialization_alias='https://schema.org/provider')
    salaryUponCompletion: Optional[Union["MonetaryAmountDistribution", List["MonetaryAmountDistribution"]]] = Field(default=None,validation_alias=AliasChoices('salaryUponCompletion', 'https://schema.org/salaryUponCompletion'),serialization_alias='https://schema.org/salaryUponCompletion')
    numberOfCredits: Optional[Union[int, List[int], "StructuredValue", List["StructuredValue"]]] = Field(default=None,validation_alias=AliasChoices('numberOfCredits', 'https://schema.org/numberOfCredits'),serialization_alias='https://schema.org/numberOfCredits')
    termsPerYear: Optional[Union[float, List[float]]] = Field(default=None,validation_alias=AliasChoices('termsPerYear', 'https://schema.org/termsPerYear'),serialization_alias='https://schema.org/termsPerYear')
    educationalProgramMode: Optional[Union[str, List[str], HttpUrl, List[HttpUrl]]] = Field(default=None,validation_alias=AliasChoices('educationalProgramMode', 'https://schema.org/educationalProgramMode'),serialization_alias='https://schema.org/educationalProgramMode')
    @field_serializer('educationalProgramMode')
    def educationalProgramMode2str(self, val) -> str | List[str]:
        def _to_str(value):
            if isinstance(value, HttpUrl):
                return str(value)
            return value

        if isinstance(val, list):
            return [_to_str(i) for i in val]
        return _to_str(val)

    trainingSalary: Optional[Union["MonetaryAmountDistribution", List["MonetaryAmountDistribution"]]] = Field(default=None,validation_alias=AliasChoices('trainingSalary', 'https://schema.org/trainingSalary'),serialization_alias='https://schema.org/trainingSalary')
    termDuration: Optional[Union["Duration", List["Duration"]]] = Field(default=None,validation_alias=AliasChoices('termDuration', 'https://schema.org/termDuration'),serialization_alias='https://schema.org/termDuration')
    timeOfDay: Optional[Union[str, List[str]]] = Field(default=None,validation_alias=AliasChoices('timeOfDay', 'https://schema.org/timeOfDay'),serialization_alias='https://schema.org/timeOfDay')
    maximumEnrollment: Optional[Union[int, List[int]]] = Field(default=None,validation_alias=AliasChoices('maximumEnrollment', 'https://schema.org/maximumEnrollment'),serialization_alias='https://schema.org/maximumEnrollment')
    financialAidEligible: Optional[Union["DefinedTerm", List["DefinedTerm"], str, List[str]]] = Field(default=None,validation_alias=AliasChoices('financialAidEligible', 'https://schema.org/financialAidEligible'),serialization_alias='https://schema.org/financialAidEligible')
    occupationalCredentialAwarded: Optional[Union[HttpUrl, List[HttpUrl], "EducationalOccupationalCredential", List["EducationalOccupationalCredential"], str, List[str]]] = Field(default=None,validation_alias=AliasChoices('occupationalCredentialAwarded', 'https://schema.org/occupationalCredentialAwarded'),serialization_alias='https://schema.org/occupationalCredentialAwarded')
    @field_serializer('occupationalCredentialAwarded')
    def occupationalCredentialAwarded2str(self, val) -> str | List[str]:
        def _to_str(value):
            if isinstance(value, HttpUrl):
                return str(value)
            return value

        if isinstance(val, list):
            return [_to_str(i) for i in val]
        return _to_str(val)

    hasCourse: Optional[Union["Course", List["Course"]]] = Field(default=None,validation_alias=AliasChoices('hasCourse', 'https://schema.org/hasCourse'),serialization_alias='https://schema.org/hasCourse')
    occupationalCategory: Optional[Union["CategoryCode", List["CategoryCode"], str, List[str]]] = Field(default=None,validation_alias=AliasChoices('occupationalCategory', 'https://schema.org/occupationalCategory'),serialization_alias='https://schema.org/occupationalCategory')
    programPrerequisites: Optional[Union["AlignmentObject", List["AlignmentObject"], "Course", List["Course"], "EducationalOccupationalCredential", List["EducationalOccupationalCredential"], str, List[str]]] = Field(default=None,validation_alias=AliasChoices('programPrerequisites', 'https://schema.org/programPrerequisites'),serialization_alias='https://schema.org/programPrerequisites')
    startDate: Optional[Union[date, List[date], datetime, List[datetime]]] = Field(default=None,validation_alias=AliasChoices('startDate', 'https://schema.org/startDate'),serialization_alias='https://schema.org/startDate')
