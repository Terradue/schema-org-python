from typing import Literal
from pydantic import AliasChoices, Field
from schemaorg_models.creative_work import CreativeWork


class Code(CreativeWork):
    """
Computer programming source code. Example: Full (compile ready) solutions, code snippet samples, scripts, templates.
    """
    type_: Literal['https://schema.org/Code'] = Field('class', alias=AliasChoices('@type', 'https://schema.org/Code'),serialization_alias='class') # type: ignore
