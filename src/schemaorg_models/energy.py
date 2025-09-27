from typing import Literal
from pydantic import Field
from schemaorg_models.quantity import Quantity


class Energy(Quantity):
    """
Properties that take Energy as values are of the form '&lt;Number&gt; &lt;Energy unit of measure&gt;'.
    """
    class_: Literal['https://schema.org/Energy'] = Field(default='https://schema.org/Energy', alias='http://www.w3.org/2000/01/rdf-schema#Class', serialization_alias='http://www.w3.org/2000/01/rdf-schema#Class') # type: ignore
