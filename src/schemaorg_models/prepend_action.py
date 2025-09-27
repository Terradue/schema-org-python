from typing import Literal
from pydantic import AliasChoices, Field
from schemaorg_models.insert_action import InsertAction


class PrependAction(InsertAction):
    """
The act of inserting at the beginning if an ordered collection.
    """
    type_: Literal['https://schema.org/PrependAction'] = Field('class', alias=AliasChoices('@type', 'https://schema.org/PrependAction'),serialization_alias='class') # type: ignore
