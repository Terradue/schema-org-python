from typing import Literal
from pydantic import Field
from schemaorg_models.action import Action


class FindAction(Action):
    """
The act of finding an object.\
\
Related actions:\
\
* [[SearchAction]]: FindAction is generally lead by a SearchAction, but not necessarily.
    """
    class_: Literal['https://schema.org/FindAction'] = Field(default='https://schema.org/FindAction', alias='class', serialization_alias='class') # type: ignore
