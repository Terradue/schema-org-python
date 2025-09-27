from typing import Literal
from pydantic import Field
from schemaorg_models.intangible import Intangible


class ComputerLanguage(Intangible):
    """
This type covers computer programming languages such as Scheme and Lisp, as well as other language-like computer representations. Natural languages are best represented with the [[Language]] type.
    """
    class_: Literal['https://schema.org/ComputerLanguage'] = Field('class', alias='class', serialization_alias='class') # type: ignore
