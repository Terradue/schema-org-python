from typing import Literal
from pydantic import Field
from schemaorg_models.create_action import CreateAction


class PhotographAction(CreateAction):
    """
The act of capturing still images of objects using a camera.
    """
    type_: Literal['https://schema.org/PhotographAction'] = Field(default='https://schema.org/PhotographAction', alias='@type', serialization_alias='http://www.w3.org/2000/01/rdf-schema#/Class') # type: ignore
