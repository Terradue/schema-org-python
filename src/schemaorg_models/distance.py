from typing import Literal
from pydantic import AliasChoices, Field
from schemaorg_models.quantity import Quantity


class Distance(Quantity):
    """
Properties that take Distances as values are of the form '&lt;Number&gt; &lt;Length unit of measure&gt;'. E.g., '7 ft'.
    """
    type_: Literal['https://schema.org/Distance'] = Field('class', alias=AliasChoices('@type', 'https://schema.org/Distance'),serialization_alias='class') # type: ignore
