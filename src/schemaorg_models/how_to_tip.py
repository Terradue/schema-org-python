from typing import Literal
from pydantic import AliasChoices, Field
from schemaorg_models.creative_work import CreativeWork


class HowToTip(CreativeWork):
    """
An explanation in the instructions for how to achieve a result. It provides supplementary information about a technique, supply, author's preference, etc. It can explain what could be done, or what should not be done, but doesn't specify what should be done (see HowToDirection).
    """
    type_: Literal['https://schema.org/HowToTip'] = Field('class', alias=AliasChoices('@type', 'https://schema.org/HowToTip'),serialization_alias='class') # type: ignore
