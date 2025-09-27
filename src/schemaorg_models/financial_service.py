from typing import List, Literal, Optional, Union
from pydantic import field_serializer, AliasChoices, Field, HttpUrl
from schemaorg_models.local_business import LocalBusiness


class FinancialService(LocalBusiness):
    """
Financial services business.
    """
    class_: Literal['https://schema.org/FinancialService'] = Field('class', alias='class', serialization_alias='class') # type: ignore
    feesAndCommissionsSpecification: Optional[Union[str, List[str], HttpUrl, List[HttpUrl]]] = Field(default=None,validation_alias=AliasChoices('feesAndCommissionsSpecification', 'https://schema.org/feesAndCommissionsSpecification'), serialization_alias='https://schema.org/feesAndCommissionsSpecification')
    @field_serializer('feesAndCommissionsSpecification')
    def feesAndCommissionsSpecification2str(self, val) -> str | List[str]:
        def _to_str(value):
            if isinstance(value, HttpUrl):
                return str(value)
            return value

        if isinstance(val, list):
            return [_to_str(i) for i in val]
        return _to_str(val)

