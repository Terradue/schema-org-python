from typing import Literal
from pydantic import Field
from schemaorg_models.action import Action


class AssessAction(Action):
    """
The act of forming one's opinion, reaction or sentiment.
    """
    type_: Literal['https://schema.org/AssessAction'] = Field(default='https://schema.org/AssessAction', alias='@type', serialization_alias='http://www.w3.org/2000/01/rdf-schema#/Class') # type: ignore
