from typing import Literal
from pydantic import Field
from schemaorg_models.local_business import LocalBusiness


class DryCleaningOrLaundry(LocalBusiness):
    """
A dry-cleaning business.
    """
    type_: Literal['https://schema.org/DryCleaningOrLaundry'] = Field(default='https://schema.org/DryCleaningOrLaundry', alias='@type', serialization_alias='@type') # type: ignore
