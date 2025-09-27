from typing import Literal
from pydantic import Field
from schemaorg_models.local_business import LocalBusiness


class InternetCafe(LocalBusiness):
    """
An internet cafe.
    """
    type_: Literal['https://schema.org/InternetCafe'] = Field(default='https://schema.org/InternetCafe', alias='@type', serialization_alias='@type') # type: ignore
