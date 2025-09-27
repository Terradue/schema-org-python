from typing import Literal
from pydantic import Field
from schemaorg_models.local_business import LocalBusiness


class DryCleaningOrLaundry(LocalBusiness):
    """
A dry-cleaning business.
    """
    class_: Literal['https://schema.org/DryCleaningOrLaundry'] = Field('class', alias='class', serialization_alias='class') # type: ignore
