from typing import Literal
from pydantic import Field
from schemaorg_models.create_action import CreateAction


class FilmAction(CreateAction):
    """
The act of capturing sound and moving images on film, video, or digitally.
    """
    class_: Literal['https://schema.org/FilmAction'] = Field(default='https://schema.org/FilmAction', alias='http://www.w3.org/2000/01/rdf-schema#Class', serialization_alias='http://www.w3.org/2000/01/rdf-schema#Class') # type: ignore
