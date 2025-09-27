from typing import Literal
from pydantic import AliasChoices, Field
from schemaorg_models.organization import Organization


class WorkersUnion(Organization):
    """
A Workers Union (also known as a Labor Union, Labour Union, or Trade Union) is an organization that promotes the interests of its worker members by collectively bargaining with management, organizing, and political lobbying.
    """
    type_: Literal['https://schema.org/WorkersUnion'] = Field('class', alias=AliasChoices('@type', 'https://schema.org/WorkersUnion'),serialization_alias='class') # type: ignore
