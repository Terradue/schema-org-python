from typing import Literal
from pydantic import Field
from schemaorg_models.place import Place


class Landform(Place):
    """
A landform or physical feature.  Landform elements include mountains, plains, lakes, rivers, seascape and oceanic waterbody interface features such as bays, peninsulas, seas and so forth, including sub-aqueous terrain features such as submersed mountain ranges, volcanoes, and the great ocean basins.
    """
    class_: Literal['https://schema.org/Landform'] = Field(default='https://schema.org/Landform', alias='http://www.w3.org/2000/01/rdf-schema#Class', serialization_alias='http://www.w3.org/2000/01/rdf-schema#Class') # type: ignore
