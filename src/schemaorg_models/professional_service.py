from typing import Literal
from pydantic import Field
from schemaorg_models.local_business import LocalBusiness


class ProfessionalService(LocalBusiness):
    """
Original definition: "provider of professional services."\
\
The general [[ProfessionalService]] type for local businesses was deprecated due to confusion with [[Service]]. For reference, the types that it included were: [[Dentist]],
        [[AccountingService]], [[Attorney]], [[Notary]], as well as types for several kinds of [[HomeAndConstructionBusiness]]: [[Electrician]], [[GeneralContractor]],
        [[HousePainter]], [[Locksmith]], [[Plumber]], [[RoofingContractor]]. [[LegalService]] was introduced as a more inclusive supertype of [[Attorney]].
    """
    type_: Literal['https://schema.org/ProfessionalService'] = Field(default='https://schema.org/ProfessionalService', alias='@type', serialization_alias='@type') # type: ignore
