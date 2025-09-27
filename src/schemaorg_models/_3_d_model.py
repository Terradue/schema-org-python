from typing import Literal
from pydantic import Field
from schemaorg_models.media_object import MediaObject


class _3DModel(MediaObject):
    """
A 3D model represents some kind of 3D content, which may have [[encoding]]s in one or more [[MediaObject]]s. Many 3D formats are available (e.g. see [Wikipedia](https://en.wikipedia.org/wiki/Category:3D_graphics_file_formats)); specific encoding formats can be represented using the [[encodingFormat]] property applied to the relevant [[MediaObject]]. For the
case of a single file published after Zip compression, the convention of appending '+zip' to the [[encodingFormat]] can be used. Geospatial, AR/VR, artistic/animation, gaming, engineering and scientific content can all be represented using [[3DModel]].
    """
    class_: Literal['https://schema.org/_3DModel'] = Field(default='https://schema.org/_3DModel', alias='class', serialization_alias='class') # type: ignore
