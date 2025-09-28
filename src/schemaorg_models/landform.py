from __future__ import annotations

from .place import Place    

from pydantic import (
    Field
)
from typing import (
    Literal
)

class Landform(Place):
    """
A landform or physical feature.  Landform elements include mountains, plains, lakes, rivers, seascape and oceanic waterbody interface features such as bays, peninsulas, seas and so forth, including sub-aqueous terrain features such as submersed mountain ranges, volcanoes, and the great ocean basins.
    """
    class_: Literal['https://schema.org/Landform'] = Field( # type: ignore
        default='https://schema.org/Landform',
        alias='@type',
        serialization_alias='@type'
    )
