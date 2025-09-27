from typing import Literal
from pydantic import Field
from schemaorg_models.comment import Comment


class CorrectionComment(Comment):
    """
A [[comment]] that corrects [[CreativeWork]].
    """
    class_: Literal['https://schema.org/CorrectionComment'] = Field('class', alias='class', serialization_alias='class') # type: ignore
