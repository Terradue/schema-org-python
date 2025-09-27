from typing import Literal
from pydantic import AliasChoices, Field
from schemaorg_models.create_action import CreateAction


class FilmAction(CreateAction):
    """
The act of capturing sound and moving images on film, video, or digitally.
    """
    type_: Literal['https://schema.org/FilmAction'] = Field('class', alias=AliasChoices('@type', 'https://schema.org/FilmAction'),serialization_alias='class') # type: ignore
