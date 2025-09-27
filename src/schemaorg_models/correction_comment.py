from typing import Literal
from pydantic import AliasChoices, Field
from schemaorg_models.comment import Comment


class CorrectionComment(Comment):
    """
A [[comment]] that corrects [[CreativeWork]].
    """
    type_: Literal['https://schema.org/CorrectionComment'] = Field('class', alias=AliasChoices('@type', 'https://schema.org/CorrectionComment'),serialization_alias='class') # type: ignore
