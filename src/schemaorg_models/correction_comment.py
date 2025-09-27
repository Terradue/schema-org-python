from typing import Literal
from pydantic import Field
from schemaorg_models.comment import Comment


class CorrectionComment(Comment):
    """
A [[comment]] that corrects [[CreativeWork]].
    """
    class_: Literal['https://schema.org/CorrectionComment'] = Field(default='https://schema.org/CorrectionComment', alias='http://www.w3.org/2000/01/rdf-schema#Class', serialization_alias='http://www.w3.org/2000/01/rdf-schema#Class') # type: ignore
