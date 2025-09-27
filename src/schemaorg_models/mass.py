from typing import Literal
from pydantic import AliasChoices, Field
from schemaorg_models.quantity import Quantity


class Mass(Quantity):
    """
Properties that take Mass as values are of the form '&lt;Number&gt; &lt;Mass unit of measure&gt;'. E.g., '7 kg'.
    """
    type_: Literal['https://schema.org/Mass'] = Field('class', alias=AliasChoices('@type', 'https://schema.org/Mass'),serialization_alias='class') # type: ignore
