from typing import Literal
from pydantic import Field
from schemaorg_models.organization import Organization


class Cooperative(Organization):
    """
An organization that is a joint project of multiple organizations or persons.
    """
    class_: Literal['https://schema.org/Cooperative'] = Field('class', alias='class', serialization_alias='class') # type: ignore
