from typing import Literal
from pydantic import Field
from schemaorg_models.creative_work import CreativeWork


class Atlas(CreativeWork):
    """
A collection or bound volume of maps, charts, plates or tables, physical or in media form illustrating any subject.
    """
    class_: Literal['https://schema.org/Atlas'] = Field('class', alias='class', serialization_alias='class') # type: ignore
