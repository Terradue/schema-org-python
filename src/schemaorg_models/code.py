from typing import Literal
from pydantic import Field
from schemaorg_models.creative_work import CreativeWork


class Code(CreativeWork):
    """
Computer programming source code. Example: Full (compile ready) solutions, code snippet samples, scripts, templates.
    """
    type_: Literal['https://schema.org/Code'] = Field(default='https://schema.org/Code', alias='@type', serialization_alias='http://www.w3.org/2000/01/rdf-schema#/Class') # type: ignore
