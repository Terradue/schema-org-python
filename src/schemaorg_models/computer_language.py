from typing import Literal
from pydantic import AliasChoices, Field
from schemaorg_models.intangible import Intangible


class ComputerLanguage(Intangible):
    """
This type covers computer programming languages such as Scheme and Lisp, as well as other language-like computer representations. Natural languages are best represented with the [[Language]] type.
    """
    type_: Literal['https://schema.org/ComputerLanguage'] = Field('class', alias=AliasChoices('@type', 'https://schema.org/ComputerLanguage'),serialization_alias='class') # type: ignore
