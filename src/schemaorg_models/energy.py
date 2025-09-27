from typing import Literal
from pydantic import Field
from schemaorg_models.quantity import Quantity


class Energy(Quantity):
    """
Properties that take Energy as values are of the form '&lt;Number&gt; &lt;Energy unit of measure&gt;'.
    """
    class_: Literal['https://schema.org/Energy'] = Field('class', alias='class', serialization_alias='class') # type: ignore
