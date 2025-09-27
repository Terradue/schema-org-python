from typing import Literal
from pydantic import Field
from schemaorg_models.local_business import LocalBusiness


class InternetCafe(LocalBusiness):
    """
An internet cafe.
    """
    type_: Literal['https://schema.org/InternetCafe'] = Field(default='https://schema.org/InternetCafe', alias='@type', serialization_alias='http://www.w3.org/2000/01/rdf-schema#/Class') # type: ignore
