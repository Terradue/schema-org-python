from typing import List, Literal, Optional, Union
from pydantic import AliasChoices, Field
from schemaorg_models.add_action import AddAction

from schemaorg_models.place import Place

class InsertAction(AddAction):
    """
The act of adding at a specific location in an ordered collection.
    """
    class_: Literal['https://schema.org/InsertAction'] = Field(default='https://schema.org/InsertAction', alias='class', serialization_alias='class') # type: ignore
    toLocation: Optional[Union[Place, List[Place]]] = Field(default=None, validation_alias=AliasChoices('toLocation', 'https://schema.org/toLocation'), serialization_alias='https://schema.org/toLocation')
