from typing import Literal
from pydantic import Field
from schemaorg_models.quantity import Quantity


class Distance(Quantity):
    """
Properties that take Distances as values are of the form '&lt;Number&gt; &lt;Length unit of measure&gt;'. E.g., '7 ft'.
    """
    class_: Literal['https://schema.org/Distance'] = Field('class', alias='class', serialization_alias='class') # type: ignore
