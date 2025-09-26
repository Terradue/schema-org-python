from typing import Union, List, Optional
from pydantic import field_serializer, AliasChoices, Field, HttpUrl
from schemaorg_models.local_business import LocalBusiness


class FinancialService(LocalBusiness):
    """
Financial services business.
    """
    feesAndCommissionsSpecification: Optional[Union[str, List[str], HttpUrl, List[HttpUrl]]] = Field(default=None,validation_alias=AliasChoices('feesAndCommissionsSpecification', 'https://schema.org/feesAndCommissionsSpecification'),serialization_alias='https://schema.org/feesAndCommissionsSpecification')
    @field_serializer('feesAndCommissionsSpecification')
    def feesAndCommissionsSpecification2str(self, val) -> str:
        if isinstance(val, HttpUrl): ### This magic! If isinstance(val, HttpUrl) - error
            return str(val)
        return val

