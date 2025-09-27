from typing import Literal
from pydantic import Field
from schemaorg_models.organization import Organization


class WorkersUnion(Organization):
    """
A Workers Union (also known as a Labor Union, Labour Union, or Trade Union) is an organization that promotes the interests of its worker members by collectively bargaining with management, organizing, and political lobbying.
    """
    type_: Literal['https://schema.org/WorkersUnion'] = Field(default='https://schema.org/WorkersUnion', alias='@type', serialization_alias='http://www.w3.org/2000/01/rdf-schema#/Class') # type: ignore
