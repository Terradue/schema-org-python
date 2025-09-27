from typing import Literal
from pydantic import Field
from schemaorg_models.local_business import LocalBusiness


class DryCleaningOrLaundry(LocalBusiness):
    """
A dry-cleaning business.
    """
    class_: Literal['https://schema.org/DryCleaningOrLaundry'] = Field(default='https://schema.org/DryCleaningOrLaundry', alias='http://www.w3.org/2000/01/rdf-schema#Class', serialization_alias='http://www.w3.org/2000/01/rdf-schema#Class') # type: ignore
