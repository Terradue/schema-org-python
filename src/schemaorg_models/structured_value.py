from typing import Literal
from pydantic import Field
from schemaorg_models.intangible import Intangible


class StructuredValue(Intangible):
    """
Structured values are used when the value of a property has a more complex structure than simply being a textual value or a reference to another thing.
    """
    class_: Literal['https://schema.org/StructuredValue'] = Field('class', alias='class', serialization_alias='class') # type: ignore
