from typing import Literal
from pydantic import Field
from schemaorg_models.local_business import LocalBusiness


class Library(LocalBusiness):
    """
A library.
    """
    class_: Literal['https://schema.org/Library'] = Field('class', alias='class', serialization_alias='class') # type: ignore
