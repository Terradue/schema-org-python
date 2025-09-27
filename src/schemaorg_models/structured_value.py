from typing import Literal
from pydantic import AliasChoices, Field
from schemaorg_models.intangible import Intangible


class StructuredValue(Intangible):
    """
Structured values are used when the value of a property has a more complex structure than simply being a textual value or a reference to another thing.
    """
    type_: Literal['https://schema.org/StructuredValue'] = Field('class', alias=AliasChoices('@type', 'https://schema.org/StructuredValue'),serialization_alias='class') # type: ignore
