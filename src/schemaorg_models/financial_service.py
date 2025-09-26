from typing import Union, List, Optional
from pydantic import AliasChoices, Field, HttpUrl
from schemaorg_models.local_business import LocalBusiness


class FinancialService(LocalBusiness):
    """
Financial services business.
    """
    feesAndCommissionsSpecification: Optional[Union[str, List[str], HttpUrl, List[HttpUrl]]] = Field(default=None,validation_alias=AliasChoices('feesAndCommissionsSpecification', 'https://schema.org/feesAndCommissionsSpecification'),serialization_alias='https://schema.org/feesAndCommissionsSpecification')
