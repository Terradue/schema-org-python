from typing import Literal
from pydantic import Field
from schemaorg_models.church import Church


class CatholicChurch(Church):
    """
A Catholic church.
    """
    class_: Literal['https://schema.org/CatholicChurch'] = Field(default='https://schema.org/CatholicChurch', alias='http://www.w3.org/2000/01/rdf-schema#Class', serialization_alias='http://www.w3.org/2000/01/rdf-schema#Class') # type: ignore
