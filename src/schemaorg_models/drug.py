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
from .substance import Substance
from typing import TYPE_CHECKING
if TYPE_CHECKING:
    from .drug_strength import DrugStrength
    from .maximum_dose_schedule import MaximumDoseSchedule
    from .medical_enumeration import MedicalEnumeration
    from .drug_pregnancy_category import DrugPregnancyCategory
    from .drug_legal_status import DrugLegalStatus
    from .drug_class import DrugClass
    from .drug_prescription_status import DrugPrescriptionStatus
    from .dose_schedule import DoseSchedule
    from .health_insurance_plan import HealthInsurancePlan

class Drug(Substance):
    '''
    A chemical or biologic substance, used as a medical therapy, that has a physiological effect on an organism. Here the term drug is used interchangeably with the term medicine although clinical knowledge makes a clear difference between them.

    Attributes:
        alcoholWarning: Any precaution, guidance, contraindication, etc. related to consumption of alcohol while taking this drug.
        legalStatus: The drug or supplement's legal status, including any controlled substance schedules that apply.
        proprietaryName: Proprietary name given to the diet plan, typically by its originator or creator.
        mechanismOfAction: The specific biochemical interaction through which this drug or supplement produces its pharmacological effect.
        interactingDrug: Another drug that is known to interact with this drug in a way that impacts the effect of this drug or causes a risk to the patient. Note: disease interactions are typically captured as contraindications.
        isAvailableGenerically: True if the drug is available in a generic form (regardless of name).
        isProprietary: True if this item's name is a proprietary/brand name (vs. generic name).
        maximumIntake: Recommended intake of this supplement for a given population as defined by a specific recommending authority.
        prescribingInfo: Link to prescribing information for the drug.
        doseSchedule: A dosing schedule for the drug for a given population, either observed, recommended, or maximum dose based on the type used.
        foodWarning: Any precaution, guidance, contraindication, etc. related to consumption of specific foods while taking this drug.
        administrationRoute: A route by which this drug may be administered, e.g. 'oral'.
        overdosage: Any information related to overdose on a drug, including signs or symptoms, treatments, contact information for emergency response.
        activeIngredient: An active ingredient, typically chemical compounds and/or biologic substances.
        rxcui: The RxCUI drug identifier from RXNORM.
        pregnancyWarning: Any precaution, guidance, contraindication, etc. related to this drug's use during pregnancy.
        relatedDrug: Any other drug related to this one, for example commonly-prescribed alternatives.
        clinicalPharmacology: Description of the absorption and elimination of drugs, including their concentration (pharmacokinetics, pK) and biological effects (pharmacodynamics, pD).
        breastfeedingWarning: Any precaution, guidance, contraindication, etc. related to this drug's use by breastfeeding mothers.
        clincalPharmacology: Description of the absorption and elimination of drugs, including their concentration (pharmacokinetics, pK) and biological effects (pharmacodynamics, pD).
        labelDetails: Link to the drug's label details.
        availableStrength: An available dosage strength for the drug.
        warning: Any FDA or other warnings about the drug (text or URL).
        includedInHealthInsurancePlan: The insurance plans that cover this drug.
        drugClass: The class of drug this belongs to (e.g., statins).
        pregnancyCategory: Pregnancy category of this drug.
        prescriptionStatus: Indicates the status of drug prescription, e.g. local catalogs classifications or whether the drug is available by prescription or over-the-counter, etc.
        nonProprietaryName: The generic name of this drug or supplement.
        dosageForm: A dosage form in which this drug/supplement is available, e.g. 'tablet', 'suspension', 'injection'.
        drugUnit: The unit in which the drug is measured, e.g. '5 mg tablet'.
    '''
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
    legalStatus: Optional[Union['DrugLegalStatus', List['DrugLegalStatus'], 'MedicalEnumeration', List['MedicalEnumeration'], str, List[str]]] = Field(
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
    interactingDrug: Optional[Union['Drug', List['Drug']]] = Field(
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
    maximumIntake: Optional[Union['MaximumDoseSchedule', List['MaximumDoseSchedule']]] = Field(
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
    doseSchedule: Optional[Union['DoseSchedule', List['DoseSchedule']]] = Field(
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
    relatedDrug: Optional[Union['Drug', List['Drug']]] = Field(
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
    availableStrength: Optional[Union['DrugStrength', List['DrugStrength']]] = Field(
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
    includedInHealthInsurancePlan: Optional[Union['HealthInsurancePlan', List['HealthInsurancePlan']]] = Field(
        default=None,
        validation_alias=AliasChoices(
            'includedInHealthInsurancePlan',
            'https://schema.org/includedInHealthInsurancePlan'
        ),
        serialization_alias='https://schema.org/includedInHealthInsurancePlan'
    )
    drugClass: Optional[Union['DrugClass', List['DrugClass']]] = Field(
        default=None,
        validation_alias=AliasChoices(
            'drugClass',
            'https://schema.org/drugClass'
        ),
        serialization_alias='https://schema.org/drugClass'
    )
    pregnancyCategory: Optional[Union['DrugPregnancyCategory', List['DrugPregnancyCategory']]] = Field(
        default=None,
        validation_alias=AliasChoices(
            'pregnancyCategory',
            'https://schema.org/pregnancyCategory'
        ),
        serialization_alias='https://schema.org/pregnancyCategory'
    )
    prescriptionStatus: Optional[Union['DrugPrescriptionStatus', List['DrugPrescriptionStatus'], str, List[str]]] = Field(
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
