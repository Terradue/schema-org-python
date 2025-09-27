from typing import Literal
from pydantic import Field
from schemaorg_models.creative_work import CreativeWork


class Statement(CreativeWork):
    """
A statement about something, for example a fun or interesting fact. If known, the main entity this statement is about can be indicated using mainEntity. For more formal claims (e.g. in Fact Checking), consider using [[Claim]] instead. Use the [[text]] property to capture the text of the statement.
    """
    type_: Literal['https://schema.org/Statement'] = Field(default='https://schema.org/Statement', alias='@type', serialization_alias='@type') # type: ignore
