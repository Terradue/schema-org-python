from typing import List, Literal, Optional, Union
from pydantic import AliasChoices, Field
from schemaorg_models.structured_value import StructuredValue

from schemaorg_models.warranty_scope import WarrantyScope
from schemaorg_models.quantitative_value import QuantitativeValue

class WarrantyPromise(StructuredValue):
    """
A structured value representing the duration and scope of services that will be provided to a customer free of charge in case of a defect or malfunction of a product.
    """
    class_: Literal['https://schema.org/WarrantyPromise'] = Field(default='https://schema.org/WarrantyPromise', alias='@type', serialization_alias='@type') # type: ignore
    warrantyScope: Optional[Union[WarrantyScope, List[WarrantyScope]]] = Field(default=None, validation_alias=AliasChoices('warrantyScope', 'https://schema.org/warrantyScope'), serialization_alias='https://schema.org/warrantyScope')
    durationOfWarranty: Optional[Union[QuantitativeValue, List[QuantitativeValue]]] = Field(default=None, validation_alias=AliasChoices('durationOfWarranty', 'https://schema.org/durationOfWarranty'), serialization_alias='https://schema.org/durationOfWarranty')
