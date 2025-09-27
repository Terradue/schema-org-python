from typing import List, Literal, Optional, Union
from pydantic import AliasChoices, Field
from schemaorg_models.action import Action


class SearchAction(Action):
    """
The act of searching for an object.\
\
Related actions:\
\
* [[FindAction]]: SearchAction generally leads to a FindAction, but not necessarily.
    """
    class_: Literal['https://schema.org/SearchAction'] = Field('class', alias='class', serialization_alias='class') # type: ignore
    query: Optional[Union[str, List[str]]] = Field(default=None,validation_alias=AliasChoices('query', 'https://schema.org/query'), serialization_alias='https://schema.org/query')
