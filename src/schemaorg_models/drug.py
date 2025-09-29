from __future__ import annotations
from pydantic import (
    AliasChoices,
    Field,
    HttpUrl
)
from typing import (
    List,
    Literal,
    Optional,
    Union
)
from .substance import Substance
from typing import TYPE_CHECKING
if TYPE_CHECKING:
    from .drug_strength import DrugStrength
    from .medical_enumeration import MedicalEnumeration
    from .drug_pregnancy_category import DrugPregnancyCategory
    from .health_insurance_plan import HealthInsurancePlan
    from .drug_legal_status import DrugLegalStatus
    from .drug_prescription_status import DrugPrescriptionStatus
    from .maximum_dose_schedule import MaximumDoseSchedule
    from .dose_schedule import DoseSchedule
    from .drug_class import DrugClass

class Drug(Substance):
    """
Specifying a drug or medicine used in a medication procedure.
    """
    class_: Literal['https://schema.org/Drug'] = Field( # type: ignore
        default='https://schema.org/Drug',
        alias='@type',
        serialization_alias='@type'
    )
    alcoholWarning: Optional[Union[str, List[str]]] = Field(
        default=None,
        validation_alias=AliasChoices(
            'alcoholWarning',
            'https://schema.org/alcoholWarning'
        ),
        serialization_alias='https://schema.org/alcoholWarning'
    )
    legalStatus: Optional[Union["DrugLegalStatus", List["DrugLegalStatus"], "MedicalEnumeration", List["MedicalEnumeration"], str, List[str]]] = Field(
        default=None,
        validation_alias=AliasChoices(
            'legalStatus',
            'https://schema.org/legalStatus'
        ),
        serialization_alias='https://schema.org/legalStatus'
    )
    proprietaryName: Optional[Union[str, List[str]]] = Field(
        default=None,
        validation_alias=AliasChoices(
            'proprietaryName',
            'https://schema.org/proprietaryName'
        ),
        serialization_alias='https://schema.org/proprietaryName'
    )
    mechanismOfAction: Optional[Union[str, List[str]]] = Field(
        default=None,
        validation_alias=AliasChoices(
            'mechanismOfAction',
            'https://schema.org/mechanismOfAction'
        ),
        serialization_alias='https://schema.org/mechanismOfAction'
    )
    interactingDrug: Optional[Union["Drug", List["Drug"]]] = Field(
        default=None,
        validation_alias=AliasChoices(
            'interactingDrug',
            'https://schema.org/interactingDrug'
        ),
        serialization_alias='https://schema.org/interactingDrug'
    )
    isAvailableGenerically: Optional[Union[bool, List[bool]]] = Field(
        default=None,
        validation_alias=AliasChoices(
            'isAvailableGenerically',
            'https://schema.org/isAvailableGenerically'
        ),
        serialization_alias='https://schema.org/isAvailableGenerically'
    )
    isProprietary: Optional[Union[bool, List[bool]]] = Field(
        default=None,
        validation_alias=AliasChoices(
            'isProprietary',
            'https://schema.org/isProprietary'
        ),
        serialization_alias='https://schema.org/isProprietary'
    )
    maximumIntake: Optional[Union["MaximumDoseSchedule", List["MaximumDoseSchedule"]]] = Field(
        default=None,
        validation_alias=AliasChoices(
            'maximumIntake',
            'https://schema.org/maximumIntake'
        ),
        serialization_alias='https://schema.org/maximumIntake'
    )
    prescribingInfo: Optional[Union[HttpUrl, List[HttpUrl]]] = Field(
        default=None,
        validation_alias=AliasChoices(
            'prescribingInfo',
            'https://schema.org/prescribingInfo'
        ),
        serialization_alias='https://schema.org/prescribingInfo'
    )
    doseSchedule: Optional[Union["DoseSchedule", List["DoseSchedule"]]] = Field(
        default=None,
        validation_alias=AliasChoices(
            'doseSchedule',
            'https://schema.org/doseSchedule'
        ),
        serialization_alias='https://schema.org/doseSchedule'
    )
    foodWarning: Optional[Union[str, List[str]]] = Field(
        default=None,
        validation_alias=AliasChoices(
            'foodWarning',
            'https://schema.org/foodWarning'
        ),
        serialization_alias='https://schema.org/foodWarning'
    )
    administrationRoute: Optional[Union[str, List[str]]] = Field(
        default=None,
        validation_alias=AliasChoices(
            'administrationRoute',
            'https://schema.org/administrationRoute'
        ),
        serialization_alias='https://schema.org/administrationRoute'
    )
    overdosage: Optional[Union[str, List[str]]] = Field(
        default=None,
        validation_alias=AliasChoices(
            'overdosage',
            'https://schema.org/overdosage'
        ),
        serialization_alias='https://schema.org/overdosage'
    )
    activeIngredient: Optional[Union[str, List[str]]] = Field(
        default=None,
        validation_alias=AliasChoices(
            'activeIngredient',
            'https://schema.org/activeIngredient'
        ),
        serialization_alias='https://schema.org/activeIngredient'
    )
    rxcui: Optional[Union[str, List[str]]] = Field(
        default=None,
        validation_alias=AliasChoices(
            'rxcui',
            'https://schema.org/rxcui'
        ),
        serialization_alias='https://schema.org/rxcui'
    )
    pregnancyWarning: Optional[Union[str, List[str]]] = Field(
        default=None,
        validation_alias=AliasChoices(
            'pregnancyWarning',
            'https://schema.org/pregnancyWarning'
        ),
        serialization_alias='https://schema.org/pregnancyWarning'
    )
    relatedDrug: Optional[Union["Drug", List["Drug"]]] = Field(
        default=None,
        validation_alias=AliasChoices(
            'relatedDrug',
            'https://schema.org/relatedDrug'
        ),
        serialization_alias='https://schema.org/relatedDrug'
    )
    clinicalPharmacology: Optional[Union[str, List[str]]] = Field(
        default=None,
        validation_alias=AliasChoices(
            'clinicalPharmacology',
            'https://schema.org/clinicalPharmacology'
        ),
        serialization_alias='https://schema.org/clinicalPharmacology'
    )
    breastfeedingWarning: Optional[Union[str, List[str]]] = Field(
        default=None,
        validation_alias=AliasChoices(
            'breastfeedingWarning',
            'https://schema.org/breastfeedingWarning'
        ),
        serialization_alias='https://schema.org/breastfeedingWarning'
    )
    clincalPharmacology: Optional[Union[str, List[str]]] = Field(
        default=None,
        validation_alias=AliasChoices(
            'clincalPharmacology',
            'https://schema.org/clincalPharmacology'
        ),
        serialization_alias='https://schema.org/clincalPharmacology'
    )
    labelDetails: Optional[Union[HttpUrl, List[HttpUrl]]] = Field(
        default=None,
        validation_alias=AliasChoices(
            'labelDetails',
            'https://schema.org/labelDetails'
        ),
        serialization_alias='https://schema.org/labelDetails'
    )
    availableStrength: Optional[Union["DrugStrength", List["DrugStrength"]]] = Field(
        default=None,
        validation_alias=AliasChoices(
            'availableStrength',
            'https://schema.org/availableStrength'
        ),
        serialization_alias='https://schema.org/availableStrength'
    )
    warning: Optional[Union[str, List[str], HttpUrl, List[HttpUrl]]] = Field(
        default=None,
        validation_alias=AliasChoices(
            'warning',
            'https://schema.org/warning'
        ),
        serialization_alias='https://schema.org/warning'
    )
    includedInHealthInsurancePlan: Optional[Union["HealthInsurancePlan", List["HealthInsurancePlan"]]] = Field(
        default=None,
        validation_alias=AliasChoices(
            'includedInHealthInsurancePlan',
            'https://schema.org/includedInHealthInsurancePlan'
        ),
        serialization_alias='https://schema.org/includedInHealthInsurancePlan'
    )
    drugClass: Optional[Union["DrugClass", List["DrugClass"]]] = Field(
        default=None,
        validation_alias=AliasChoices(
            'drugClass',
            'https://schema.org/drugClass'
        ),
        serialization_alias='https://schema.org/drugClass'
    )
    pregnancyCategory: Optional[Union["DrugPregnancyCategory", List["DrugPregnancyCategory"]]] = Field(
        default=None,
        validation_alias=AliasChoices(
            'pregnancyCategory',
            'https://schema.org/pregnancyCategory'
        ),
        serialization_alias='https://schema.org/pregnancyCategory'
    )
    prescriptionStatus: Optional[Union["DrugPrescriptionStatus", List["DrugPrescriptionStatus"], str, List[str]]] = Field(
        default=None,
        validation_alias=AliasChoices(
            'prescriptionStatus',
            'https://schema.org/prescriptionStatus'
        ),
        serialization_alias='https://schema.org/prescriptionStatus'
    )
    nonProprietaryName: Optional[Union[str, List[str]]] = Field(
        default=None,
        validation_alias=AliasChoices(
            'nonProprietaryName',
            'https://schema.org/nonProprietaryName'
        ),
        serialization_alias='https://schema.org/nonProprietaryName'
    )
    dosageForm: Optional[Union[str, List[str]]] = Field(
        default=None,
        validation_alias=AliasChoices(
            'dosageForm',
            'https://schema.org/dosageForm'
        ),
        serialization_alias='https://schema.org/dosageForm'
    )
    drugUnit: Optional[Union[str, List[str]]] = Field(
        default=None,
        validation_alias=AliasChoices(
            'drugUnit',
            'https://schema.org/drugUnit'
        ),
        serialization_alias='https://schema.org/drugUnit'
    )
