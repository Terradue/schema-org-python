from typing import Literal
from pydantic import AliasChoices, Field
from schemaorg_models.create_action import CreateAction


class PhotographAction(CreateAction):
    """
The act of capturing still images of objects using a camera.
    """
    type_: Literal['https://schema.org/PhotographAction'] = Field('class', alias=AliasChoices('@type', 'https://schema.org/PhotographAction'),serialization_alias='class') # type: ignore
