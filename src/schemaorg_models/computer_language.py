from __future__ import annotations

from .intangible import Intangible    

from pydantic import (
    Field
)
from typing import (
    Literal
)

class ComputerLanguage(Intangible):
    """
This type covers computer programming languages such as Scheme and Lisp, as well as other language-like computer representations. Natural languages are best represented with the [[Language]] type.
    """
    class_: Literal['https://schema.org/ComputerLanguage'] = Field( # type: ignore
        default='https://schema.org/ComputerLanguage',
        alias='@type',
        serialization_alias='@type'
    )
