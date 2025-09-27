from typing import Literal
from pydantic import AliasChoices, Field
from schemaorg_models.action import Action


class FindAction(Action):
    """
The act of finding an object.\
\
Related actions:\
\
* [[SearchAction]]: FindAction is generally lead by a SearchAction, but not necessarily.
    """
    type_: Literal['https://schema.org/FindAction'] = Field('class', alias=AliasChoices('@type', 'https://schema.org/FindAction'),serialization_alias='class') # type: ignore
