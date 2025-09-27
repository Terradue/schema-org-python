from typing import Literal
from pydantic import Field
from schemaorg_models.use_action import UseAction


class WearAction(UseAction):
    """
The act of dressing oneself in clothing.
    """
    class_: Literal['https://schema.org/WearAction'] = Field(default='https://schema.org/WearAction', alias='http://www.w3.org/2000/01/rdf-schema#Class', serialization_alias='http://www.w3.org/2000/01/rdf-schema#Class') # type: ignore
