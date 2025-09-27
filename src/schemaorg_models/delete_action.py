from typing import Literal
from pydantic import Field
from schemaorg_models.update_action import UpdateAction


class DeleteAction(UpdateAction):
    """
The act of editing a recipient by removing one of its objects.
    """
    class_: Literal['https://schema.org/DeleteAction'] = Field(default='https://schema.org/DeleteAction', alias='http://www.w3.org/2000/01/rdf-schema#Class', serialization_alias='http://www.w3.org/2000/01/rdf-schema#Class') # type: ignore
