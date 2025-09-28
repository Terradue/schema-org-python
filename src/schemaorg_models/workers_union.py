from __future__ import annotations
from pydantic import (
    Field
)
from typing import (
    Literal
)
from .organization import Organization

class WorkersUnion(Organization):
    """
A Workers Union (also known as a Labor Union, Labour Union, or Trade Union) is an organization that promotes the interests of its worker members by collectively bargaining with management, organizing, and political lobbying.
    """
    class_: Literal['https://schema.org/WorkersUnion'] = Field( # type: ignore
        default='https://schema.org/WorkersUnion',
        alias='@type',
        serialization_alias='@type'
    )
