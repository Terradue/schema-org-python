from typing import Literal
from pydantic import Field
from schemaorg_models.insert_action import InsertAction


class AppendAction(InsertAction):
    """
The act of inserting at the end if an ordered collection.
    """
    class_: Literal['https://schema.org/AppendAction'] = Field(default='https://schema.org/AppendAction', alias='http://www.w3.org/2000/01/rdf-schema#Class', serialization_alias='http://www.w3.org/2000/01/rdf-schema#Class') # type: ignore
