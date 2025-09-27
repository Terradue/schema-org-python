from typing import Literal
from pydantic import AliasChoices, Field
from schemaorg_models.local_business import LocalBusiness


class DryCleaningOrLaundry(LocalBusiness):
    """
A dry-cleaning business.
    """
    type_: Literal['https://schema.org/DryCleaningOrLaundry'] = Field('class', alias=AliasChoices('@type', 'https://schema.org/DryCleaningOrLaundry'),serialization_alias='class') # type: ignore
