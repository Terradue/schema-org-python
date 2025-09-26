from typing import Union, List, Optional
from pydantic import AliasChoices, Field
from schemaorg_models.structured_value import StructuredValue


class PostalCodeRangeSpecification(StructuredValue):
    """
Indicates a range of postal codes, usually defined as the set of valid codes between [[postalCodeBegin]] and [[postalCodeEnd]], inclusively.
    """
    postalCodeBegin: Optional[Union[str, List[str]]] = Field(default=None,validation_alias=AliasChoices('postalCodeBegin', 'https://schema.org/postalCodeBegin'),serialization_alias='https://schema.org/postalCodeBegin')
    postalCodeEnd: Optional[Union[str, List[str]]] = Field(default=None,validation_alias=AliasChoices('postalCodeEnd', 'https://schema.org/postalCodeEnd'),serialization_alias='https://schema.org/postalCodeEnd')
