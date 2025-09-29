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
    from .drug_pregnancy_category import DrugPregnancyCategory
    from .drug_class import DrugClass
    from .medical_enumeration import MedicalEnumeration
    from .maximum_dose_schedule import MaximumDoseSchedule
    from .dose_schedule import DoseSchedule
    from .health_insurance_plan import HealthInsurancePlan
    from .drug_legal_status import DrugLegalStatus
    from .drug_prescription_status import DrugPrescriptionStatus

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
            'genre',
            'https://schema.org/genre'
        ),
        serialization_alias='https://schema.org/genre'
    )
    legalStatus: Optional[Union['DrugLegalStatus', List['DrugLegalStatus'], 'MedicalEnumeration', List['MedicalEnumeration'], str, List[str]]] = Field(
        default=None,
        validation_alias=AliasChoices(
            'genre',
            'https://schema.org/genre'
        ),
        serialization_alias='https://schema.org/genre'
    )
    proprietaryName: Optional[Union[str, List[str]]] = Field(
        default=None,
        validation_alias=AliasChoices(
            'genre',
            'https://schema.org/genre'
        ),
        serialization_alias='https://schema.org/genre'
    )
    mechanismOfAction: Optional[Union[str, List[str]]] = Field(
        default=None,
        validation_alias=AliasChoices(
            'genre',
            'https://schema.org/genre'
        ),
        serialization_alias='https://schema.org/genre'
    )
    interactingDrug: Optional[Union['Drug', List['Drug']]] = Field(
        default=None,
        validation_alias=AliasChoices(
            'genre',
            'https://schema.org/genre'
        ),
        serialization_alias='https://schema.org/genre'
    )
    isAvailableGenerically: Optional[Union[bool, List[bool]]] = Field(
        default=None,
        validation_alias=AliasChoices(
            'genre',
            'https://schema.org/genre'
        ),
        serialization_alias='https://schema.org/genre'
    )
    isProprietary: Optional[Union[bool, List[bool]]] = Field(
        default=None,
        validation_alias=AliasChoices(
            'genre',
            'https://schema.org/genre'
        ),
        serialization_alias='https://schema.org/genre'
    )
    maximumIntake: Optional[Union['MaximumDoseSchedule', List['MaximumDoseSchedule']]] = Field(
        default=None,
        validation_alias=AliasChoices(
            'genre',
            'https://schema.org/genre'
        ),
        serialization_alias='https://schema.org/genre'
    )
    prescribingInfo: Optional[Union[HttpUrl, List[HttpUrl]]] = Field(
        default=None,
        validation_alias=AliasChoices(
            'genre',
            'https://schema.org/genre'
        ),
        serialization_alias='https://schema.org/genre'
    )
    doseSchedule: Optional[Union['DoseSchedule', List['DoseSchedule']]] = Field(
        default=None,
        validation_alias=AliasChoices(
            'genre',
            'https://schema.org/genre'
        ),
        serialization_alias='https://schema.org/genre'
    )
    foodWarning: Optional[Union[str, List[str]]] = Field(
        default=None,
        validation_alias=AliasChoices(
            'genre',
            'https://schema.org/genre'
        ),
        serialization_alias='https://schema.org/genre'
    )
    administrationRoute: Optional[Union[str, List[str]]] = Field(
        default=None,
        validation_alias=AliasChoices(
            'genre',
            'https://schema.org/genre'
        ),
        serialization_alias='https://schema.org/genre'
    )
    overdosage: Optional[Union[str, List[str]]] = Field(
        default=None,
        validation_alias=AliasChoices(
            'genre',
            'https://schema.org/genre'
        ),
        serialization_alias='https://schema.org/genre'
    )
    activeIngredient: Optional[Union[str, List[str]]] = Field(
        default=None,
        validation_alias=AliasChoices(
            'genre',
            'https://schema.org/genre'
        ),
        serialization_alias='https://schema.org/genre'
    )
    rxcui: Optional[Union[str, List[str]]] = Field(
        default=None,
        validation_alias=AliasChoices(
            'genre',
            'https://schema.org/genre'
        ),
        serialization_alias='https://schema.org/genre'
    )
    pregnancyWarning: Optional[Union[str, List[str]]] = Field(
        default=None,
        validation_alias=AliasChoices(
            'genre',
            'https://schema.org/genre'
        ),
        serialization_alias='https://schema.org/genre'
    )
    relatedDrug: Optional[Union['Drug', List['Drug']]] = Field(
        default=None,
        validation_alias=AliasChoices(
            'genre',
            'https://schema.org/genre'
        ),
        serialization_alias='https://schema.org/genre'
    )
    clinicalPharmacology: Optional[Union[str, List[str]]] = Field(
        default=None,
        validation_alias=AliasChoices(
            'genre',
            'https://schema.org/genre'
        ),
        serialization_alias='https://schema.org/genre'
    )
    breastfeedingWarning: Optional[Union[str, List[str]]] = Field(
        default=None,
        validation_alias=AliasChoices(
            'genre',
            'https://schema.org/genre'
        ),
        serialization_alias='https://schema.org/genre'
    )
    clincalPharmacology: Optional[Union[str, List[str]]] = Field(
        default=None,
        validation_alias=AliasChoices(
            'genre',
            'https://schema.org/genre'
        ),
        serialization_alias='https://schema.org/genre'
    )
    labelDetails: Optional[Union[HttpUrl, List[HttpUrl]]] = Field(
        default=None,
        validation_alias=AliasChoices(
            'genre',
            'https://schema.org/genre'
        ),
        serialization_alias='https://schema.org/genre'
    )
    availableStrength: Optional[Union['DrugStrength', List['DrugStrength']]] = Field(
        default=None,
        validation_alias=AliasChoices(
            'genre',
            'https://schema.org/genre'
        ),
        serialization_alias='https://schema.org/genre'
    )
    warning: Optional[Union[str, List[str], HttpUrl, List[HttpUrl]]] = Field(
        default=None,
        validation_alias=AliasChoices(
            'genre',
            'https://schema.org/genre'
        ),
        serialization_alias='https://schema.org/genre'
    )
    includedInHealthInsurancePlan: Optional[Union['HealthInsurancePlan', List['HealthInsurancePlan']]] = Field(
        default=None,
        validation_alias=AliasChoices(
            'genre',
            'https://schema.org/genre'
        ),
        serialization_alias='https://schema.org/genre'
    )
    drugClass: Optional[Union['DrugClass', List['DrugClass']]] = Field(
        default=None,
        validation_alias=AliasChoices(
            'genre',
            'https://schema.org/genre'
        ),
        serialization_alias='https://schema.org/genre'
    )
    pregnancyCategory: Optional[Union['DrugPregnancyCategory', List['DrugPregnancyCategory']]] = Field(
        default=None,
        validation_alias=AliasChoices(
            'genre',
            'https://schema.org/genre'
        ),
        serialization_alias='https://schema.org/genre'
    )
    prescriptionStatus: Optional[Union['DrugPrescriptionStatus', List['DrugPrescriptionStatus'], str, List[str]]] = Field(
        default=None,
        validation_alias=AliasChoices(
            'genre',
            'https://schema.org/genre'
        ),
        serialization_alias='https://schema.org/genre'
    )
    nonProprietaryName: Optional[Union[str, List[str]]] = Field(
        default=None,
        validation_alias=AliasChoices(
            'genre',
            'https://schema.org/genre'
        ),
        serialization_alias='https://schema.org/genre'
    )
    dosageForm: Optional[Union[str, List[str]]] = Field(
        default=None,
        validation_alias=AliasChoices(
            'genre',
            'https://schema.org/genre'
        ),
        serialization_alias='https://schema.org/genre'
    )
    drugUnit: Optional[Union[str, List[str]]] = Field(
        default=None,
        validation_alias=AliasChoices(
            'genre',
            'https://schema.org/genre'
        ),
        serialization_alias='https://schema.org/genre'
    )
