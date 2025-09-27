from typing import Literal
from pydantic import Field
from schemaorg_models.enumeration import Enumeration


class PhysicalActivityCategory(Enumeration):
    """
Categories of physical activity, organized by physiologic classification.
    """
    class_: Literal['https://schema.org/PhysicalActivityCategory'] = Field(default='https://schema.org/PhysicalActivityCategory', alias='http://www.w3.org/2000/01/rdf-schema#Class', serialization_alias='http://www.w3.org/2000/01/rdf-schema#Class') # type: ignore
