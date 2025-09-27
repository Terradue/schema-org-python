from typing import Literal
from pydantic import Field
from schemaorg_models.quantity import Quantity


class Mass(Quantity):
    """
Properties that take Mass as values are of the form '&lt;Number&gt; &lt;Mass unit of measure&gt;'. E.g., '7 kg'.
    """
    class_: Literal['https://schema.org/Mass'] = Field(default='https://schema.org/Mass', alias='class', serialization_alias='class') # type: ignore
