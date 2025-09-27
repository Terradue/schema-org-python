from typing import Literal
from pydantic import Field
from schemaorg_models.audience import Audience


class Researcher(Audience):
    """
Researchers.
    """
    class_: Literal['https://schema.org/Researcher'] = Field('class', alias='class', serialization_alias='class') # type: ignore
