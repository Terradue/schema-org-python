from typing import Literal
from pydantic import Field
from schemaorg_models.comment import Comment


class CorrectionComment(Comment):
    """
A [[comment]] that corrects [[CreativeWork]].
    """
    type_: Literal['https://schema.org/CorrectionComment'] = Field(default='https://schema.org/CorrectionComment', alias='@type', serialization_alias='@type') # type: ignore
