from typing import Literal
from pydantic import Field
from schemaorg_models.intangible import Intangible


class ComputerLanguage(Intangible):
    """
This type covers computer programming languages such as Scheme and Lisp, as well as other language-like computer representations. Natural languages are best represented with the [[Language]] type.
    """
    type_: Literal['https://schema.org/ComputerLanguage'] = Field(default='https://schema.org/ComputerLanguage', alias='@type', serialization_alias='http://www.w3.org/2000/01/rdf-schema#/Class') # type: ignore
