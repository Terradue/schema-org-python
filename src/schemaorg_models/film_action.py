from typing import Literal
from pydantic import Field
from schemaorg_models.create_action import CreateAction


class FilmAction(CreateAction):
    """
The act of capturing sound and moving images on film, video, or digitally.
    """
    class_: Literal['https://schema.org/FilmAction'] = Field(default='https://schema.org/FilmAction', alias='class', serialization_alias='class') # type: ignore
