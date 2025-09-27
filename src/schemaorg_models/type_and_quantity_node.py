from typing import List, Literal, Optional, Union
from pydantic import field_serializer, AliasChoices, Field, HttpUrl
from schemaorg_models.structured_value import StructuredValue

from schemaorg_models.business_function import BusinessFunction
from schemaorg_models.product import Product
from schemaorg_models.service import Service

class TypeAndQuantityNode(StructuredValue):
    """
A structured value indicating the quantity, unit of measurement, and business function of goods included in a bundle offer.
    """
    class_: Literal['https://schema.org/TypeAndQuantityNode'] = Field(default='https://schema.org/TypeAndQuantityNode', alias='http://www.w3.org/2000/01/rdf-schema#Class', serialization_alias='http://www.w3.org/2000/01/rdf-schema#Class') # type: ignore
    amountOfThisGood: Optional[Union[float, List[float]]] = Field(default=None, validation_alias=AliasChoices('amountOfThisGood', 'https://schema.org/amountOfThisGood'), serialization_alias='https://schema.org/amountOfThisGood')
    unitText: Optional[Union[str, List[str]]] = Field(default=None, validation_alias=AliasChoices('unitText', 'https://schema.org/unitText'), serialization_alias='https://schema.org/unitText')
    businessFunction: Optional[Union[BusinessFunction, List[BusinessFunction]]] = Field(default=None, validation_alias=AliasChoices('businessFunction', 'https://schema.org/businessFunction'), serialization_alias='https://schema.org/businessFunction')
    typeOfGood: Optional[Union[Product, List[Product], Service, List[Service]]] = Field(default=None, validation_alias=AliasChoices('typeOfGood', 'https://schema.org/typeOfGood'), serialization_alias='https://schema.org/typeOfGood')
    unitCode: Optional[Union[HttpUrl, List[HttpUrl], str, List[str]]] = Field(default=None, validation_alias=AliasChoices('unitCode', 'https://schema.org/unitCode'), serialization_alias='https://schema.org/unitCode')
    @field_serializer('unitCode')
    def unitCode2str(self, val) -> str | List[str]:
        def _to_str(value):
            if isinstance(value, HttpUrl):
                return str(value)
            return value

        if isinstance(val, list):
            return [_to_str(i) for i in val]
        return _to_str(val)

