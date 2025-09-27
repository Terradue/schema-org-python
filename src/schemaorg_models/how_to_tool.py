from typing import Literal
from pydantic import Field
from schemaorg_models.how_to_item import HowToItem


class HowToTool(HowToItem):
    """
A tool used (but not consumed) when performing instructions for how to achieve a result.
    """
    class_: Literal['https://schema.org/HowToTool'] = Field(default='https://schema.org/HowToTool', alias='http://www.w3.org/2000/01/rdf-schema#Class', serialization_alias='http://www.w3.org/2000/01/rdf-schema#Class') # type: ignore
