from __future__ import annotations
from datetime import (
    date,
    datetime,
    time
)
from pydantic import (
    field_serializer,
    field_validator,
    AliasChoices,
    BaseModel,
    ConfigDict,
    Field,
    HttpUrl
)
from typing import (
    List,
    Literal,
    Optional,
    Union
)
from .creative_work import CreativeWork
from typing import TYPE_CHECKING
if TYPE_CHECKING:
    from .distance import Distance
    from .mass import Mass
    from .quantitative_value import QuantitativeValue
    from .person import Person

class VisualArtwork(CreativeWork):
    '''
    A work of art that is primarily visual in character.

    Attributes:
        weight: The weight of the product or person.
        artworkSurface: The supporting materials for the artwork, e.g. Canvas, Paper, Wood, Board, etc.
        colorist: The individual who adds color to inked drawings.
        artist: The primary artist for a work
    	in a medium other than pencils or digital line art--for example, if the
    	primary artwork is done in watercolors or digital paints.
        penciler: The individual who draws the primary narrative artwork.
        depth: The depth of the item.
        surface: A material used as a surface in some artwork, e.g. Canvas, Paper, Wood, Board, etc.
        artEdition: The number of copies when multiple copies of a piece of artwork are produced - e.g. for a limited edition of 20 prints, 'artEdition' refers to the total number of copies (in this example "20").
        width: The width of the item.
        artMedium: The material used. (E.g. Oil, Watercolour, Acrylic, Linoprint, Marble, Cyanotype, Digital, Lithograph, DryPoint, Intaglio, Pastel, Woodcut, Pencil, Mixed Media, etc.)
        artform: e.g. Painting, Drawing, Sculpture, Print, Photograph, Assemblage, Collage, etc.
        inker: The individual who traces over the pencil drawings in ink after pencils are complete.
        letterer: The individual who adds lettering, including speech balloons and sound effects, to artwork.
        height: The height of the item.
    '''
    class_: Literal['https://schema.org/VisualArtwork'] = Field( # type: ignore
        default='https://schema.org/VisualArtwork',
        alias='@type',
        serialization_alias='@type'
    )
    weight: Optional[Union['QuantitativeValue', List['QuantitativeValue'], 'Mass', List['Mass']]] = Field(
        default=None,
        validation_alias=AliasChoices(
            'weight',
            'https://schema.org/weight'
        ),
        serialization_alias='https://schema.org/weight'
    )
    artworkSurface: Optional[Union[str, List[str], HttpUrl, List[HttpUrl]]] = Field(
        default=None,
        validation_alias=AliasChoices(
            'artworkSurface',
            'https://schema.org/artworkSurface'
        ),
        serialization_alias='https://schema.org/artworkSurface'
    )
    colorist: Optional[Union['Person', List['Person']]] = Field(
        default=None,
        validation_alias=AliasChoices(
            'colorist',
            'https://schema.org/colorist'
        ),
        serialization_alias='https://schema.org/colorist'
    )
    artist: Optional[Union['Person', List['Person']]] = Field(
        default=None,
        validation_alias=AliasChoices(
            'artist',
            'https://schema.org/artist'
        ),
        serialization_alias='https://schema.org/artist'
    )
    penciler: Optional[Union['Person', List['Person']]] = Field(
        default=None,
        validation_alias=AliasChoices(
            'penciler',
            'https://schema.org/penciler'
        ),
        serialization_alias='https://schema.org/penciler'
    )
    depth: Optional[Union['Distance', List['Distance'], 'QuantitativeValue', List['QuantitativeValue']]] = Field(
        default=None,
        validation_alias=AliasChoices(
            'depth',
            'https://schema.org/depth'
        ),
        serialization_alias='https://schema.org/depth'
    )
    surface: Optional[Union[str, List[str], HttpUrl, List[HttpUrl]]] = Field(
        default=None,
        validation_alias=AliasChoices(
            'surface',
            'https://schema.org/surface'
        ),
        serialization_alias='https://schema.org/surface'
    )
    artEdition: Optional[Union[str, List[str], int, List[int]]] = Field(
        default=None,
        validation_alias=AliasChoices(
            'artEdition',
            'https://schema.org/artEdition'
        ),
        serialization_alias='https://schema.org/artEdition'
    )
    width: Optional[Union['QuantitativeValue', List['QuantitativeValue'], 'Distance', List['Distance']]] = Field(
        default=None,
        validation_alias=AliasChoices(
            'width',
            'https://schema.org/width'
        ),
        serialization_alias='https://schema.org/width'
    )
    artMedium: Optional[Union[str, List[str], HttpUrl, List[HttpUrl]]] = Field(
        default=None,
        validation_alias=AliasChoices(
            'artMedium',
            'https://schema.org/artMedium'
        ),
        serialization_alias='https://schema.org/artMedium'
    )
    artform: Optional[Union[HttpUrl, List[HttpUrl], str, List[str]]] = Field(
        default=None,
        validation_alias=AliasChoices(
            'artform',
            'https://schema.org/artform'
        ),
        serialization_alias='https://schema.org/artform'
    )
    inker: Optional[Union['Person', List['Person']]] = Field(
        default=None,
        validation_alias=AliasChoices(
            'inker',
            'https://schema.org/inker'
        ),
        serialization_alias='https://schema.org/inker'
    )
    letterer: Optional[Union['Person', List['Person']]] = Field(
        default=None,
        validation_alias=AliasChoices(
            'letterer',
            'https://schema.org/letterer'
        ),
        serialization_alias='https://schema.org/letterer'
    )
    height: Optional[Union['Distance', List['Distance'], 'QuantitativeValue', List['QuantitativeValue']]] = Field(
        default=None,
        validation_alias=AliasChoices(
            'height',
            'https://schema.org/height'
        ),
        serialization_alias='https://schema.org/height'
    )
