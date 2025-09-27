from typing import Literal
from pydantic import Field
from schemaorg_models.quantity import Quantity


class Distance(Quantity):
    """
Properties that take Distances as values are of the form '&lt;Number&gt; &lt;Length unit of measure&gt;'. E.g., '7 ft'.
    """
    class_: Literal['https://schema.org/Distance'] = Field(default='https://schema.org/Distance', alias='http://www.w3.org/2000/01/rdf-schema#Class', serialization_alias='http://www.w3.org/2000/01/rdf-schema#Class') # type: ignore
