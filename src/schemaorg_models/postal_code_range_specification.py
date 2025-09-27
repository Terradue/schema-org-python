from typing import List, Literal, Optional, Union
from pydantic import AliasChoices, Field
from schemaorg_models.structured_value import StructuredValue


class PostalCodeRangeSpecification(StructuredValue):
    """
Indicates a range of postal codes, usually defined as the set of valid codes between [[postalCodeBegin]] and [[postalCodeEnd]], inclusively.
    """
    class_: Literal['https://schema.org/PostalCodeRangeSpecification'] = Field(default='https://schema.org/PostalCodeRangeSpecification', alias='http://www.w3.org/2000/01/rdf-schema#Class', serialization_alias='http://www.w3.org/2000/01/rdf-schema#Class') # type: ignore
    postalCodeBegin: Optional[Union[str, List[str]]] = Field(default=None, validation_alias=AliasChoices('postalCodeBegin', 'https://schema.org/postalCodeBegin'), serialization_alias='https://schema.org/postalCodeBegin')
    postalCodeEnd: Optional[Union[str, List[str]]] = Field(default=None, validation_alias=AliasChoices('postalCodeEnd', 'https://schema.org/postalCodeEnd'), serialization_alias='https://schema.org/postalCodeEnd')
