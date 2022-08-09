# AUTOGENERATED! DO NOT EDIT! File to edit: ../notebooks/00_grids.ipynb.

# %% auto 0
__all__ = ['SquareGridBoundary', 'SquareGridGenerator', 'H3GridGenerator', 'BingTileGridGenerator']

# %% ../notebooks/00_grids.ipynb 4
import logging
from typing import List, Tuple, Union

import h3
import morecantile
import numpy as np
from fastcore.basics import patch
from geopandas import GeoDataFrame
from pandas import DataFrame
from pyproj import Transformer
from shapely.geometry import Polygon, shape
from shapely.prepared import prep

logger = logging.getLogger(__name__)

# %% ../notebooks/00_grids.ipynb 5
class SquareGridBoundary:
    """Reusing Boundary. x_min, y_min, x_max, and y_max are in the the target crs"""

    def __init__(self, x_min: float, y_min: float, x_max: float, y_max: float):
        self.x_min = x_min
        self.y_min = y_min
        self.x_max = x_max
        self.y_max = y_max

    def get_range_subset(
        self, x_min: float, y_min: float, x_max: float, y_max: float, cell_size: float
    ) -> Tuple[float, List[float], float, List[float]]:
        """Returns a subset of grids from the orginal boundary based on the boundary and a grid size"""
        xrange = np.arange(self.x_min, self.x_max, cell_size)
        yrange = np.arange(self.y_min, self.y_max, cell_size)
        # Add cell_size buffer to catch cases where the bounds of the polygon are slightly outside
        # the bounds. This might happen to do floating point after reprojection/unary_union
        x_mask = (xrange >= (x_min - cell_size)) & (xrange <= (x_max + cell_size))
        y_mask = (yrange >= (y_min - cell_size)) & (yrange <= (y_max + cell_size))
        x_idx = np.flatnonzero(x_mask)
        x_idx_offset = None if len(x_idx) == 0 else x_idx[0]
        y_idx = np.flatnonzero(y_mask)
        y_idx_offset = None if len(y_idx) == 0 else y_idx[0]
        return (
            x_idx_offset,
            xrange[x_mask],
            y_idx_offset,
            yrange[y_mask],
        )

# %% ../notebooks/00_grids.ipynb 6
class SquareGridGenerator:
    def __init__(
        self,
        cell_size: float,  # height and width of a square cell in meters
        grid_projection: str = "EPSG:3857",  # projection of grid output
        boundary: Union[SquareGridBoundary, List[float]] = None,  # original boundary
    ):
        self.cell_size = cell_size
        self.grid_projection = grid_projection
        self.boundary = boundary

# %% ../notebooks/00_grids.ipynb 7
@patch
def create_cell(
    self: SquareGridGenerator,
    x: float,  # x coord of top left
    y: float,  # y coord of top left
) -> Polygon:
    """Create a square cell based on the top left coordinates and cell_size"""
    return Polygon(
        [
            (x, y),
            (x + self.cell_size, y),
            (x + self.cell_size, y + self.cell_size),
            (x, y + self.cell_size),
        ]
    )

# %% ../notebooks/00_grids.ipynb 8
@patch
def create_grid_for_polygon(self: SquareGridGenerator, boundary, geometry):
    x_idx_offset, xrange, y_idx_offset, yrange = boundary.get_range_subset(
        *geometry.bounds, cell_size=self.cell_size
    )
    cells = {}
    prepared_geometry = prep(geometry)
    for x_idx, x in enumerate(xrange):
        for y_idx, y in enumerate(yrange):
            x_col = x_idx + x_idx_offset
            y_col = y_idx + y_idx_offset
            cell = self.create_cell(x, y)
            if prepared_geometry.intersects(cell):
                cells.update(
                    {(x_col, y_col): {"x": x_col, "y": y_col, "geometry": cell}}
                )
    return cells

# %% ../notebooks/00_grids.ipynb 9
@patch
def generate_grid(self: SquareGridGenerator, gdf: GeoDataFrame) -> GeoDataFrame:
    reprojected_gdf = gdf.to_crs(self.grid_projection)
    if self.boundary is None:
        boundary = SquareGridBoundary(*reprojected_gdf.total_bounds)
    elif isinstance(self.boundary, SquareGridBoundary):
        boundary = self.boundary
    else:
        transformer = Transformer.from_crs(gdf.crs, reprojected_gdf.crs, always_xy=True)
        x_min, y_min = transformer.transform(self.boundary[0], self.boundary[1])
        x_max, y_max = transformer.transform(self.boundary[2], self.boundary[3])
        boundary = SquareGridBoundary(x_min, y_min, x_max, y_max)

    polygons = {}
    unary_union = reprojected_gdf.unary_union
    if isinstance(unary_union, Polygon):
        polygons.update(self.create_grid_for_polygon(boundary, unary_union))
    else:
        for geom in unary_union.geoms:
            polygons.update(self.create_grid_for_polygon(boundary, geom))
    if polygons:
        dest = GeoDataFrame(
            list(polygons.values()), geometry="geometry", crs=self.grid_projection
        )
        dest.to_crs(gdf.crs, inplace=True)
        return dest
    else:
        return GeoDataFrame(
            {"x": [], "y": [], "geometry": []}, geometry="geometry", crs=gdf.crs
        )

# %% ../notebooks/00_grids.ipynb 10
class H3GridGenerator:
    def __init__(
        self,
        resolution: int,  # Resolution of hexagon. See: https://h3geo.org/docs/core-library/restable/ for more info
        return_geometry: bool = True,  # If geometry should be returned. Setting this to false will only return hex_ids
    ):
        self.resolution = resolution
        self.return_geometry = return_geometry

# %% ../notebooks/00_grids.ipynb 11
@patch
def get_hexes_for_polygon(self: H3GridGenerator, poly: Polygon):
    return h3.polyfill(
        poly.__geo_interface__,
        self.resolution,
        geo_json_conformant=True,
    )

# %% ../notebooks/00_grids.ipynb 12
@patch
def generate_grid(self: H3GridGenerator, gdf: GeoDataFrame) -> DataFrame:
    reprojected_gdf = gdf.to_crs("epsg:4326")  # h3 hexes are in epsg:4326 CRS
    hex_ids = set()
    unary_union = reprojected_gdf.unary_union
    if isinstance(unary_union, Polygon):
        hex_ids.update(self.get_hexes_for_polygon(unary_union))
    else:
        for geom in reprojected_gdf.unary_union.geoms:
            _hexes = self.get_hexes_for_polygon(geom)
            hex_ids.update(_hexes)
    df = DataFrame({"hex_id": list(hex_ids)})
    if self.return_geometry is False:
        return df
    hexes = df.hex_id.apply(
        lambda id: Polygon(h3.h3_to_geo_boundary(id, geo_json=True))
    )
    h3_gdf = GeoDataFrame(
        df,
        geometry=hexes,
        crs="epsg:4326",
    )
    return h3_gdf.to_crs(gdf.crs)

# %% ../notebooks/00_grids.ipynb 13
class BingTileGridGenerator:
    def __init__(
        self,
        zoom_level: int,  # Zoom level of tile. See: https://docs.microsoft.com/en-us/bingmaps/articles/bing-maps-tile-system for more info
        return_geometry: bool = True,  # If geometry should be returned. Setting this to false will only return quadkeys
    ):
        self.zoom_level = zoom_level
        self.return_geometry = return_geometry
        self.tms = morecantile.tms.get("WebMercatorQuad")

    def tile_to_polygon(self, tile: morecantile.Tile):
        """Concerts a tile to geometry"""
        return shape(self.tms.feature(tile)["geometry"])

    def get_tiles_for_polygon(
        self,
        polygon: Polygon,
        filter: bool = True,
    ):
        """Get the interseting tiles with polygon for a zoom level. Polygon should be in EPSG:4326"""
        x_min, y_min, x_max, y_max = polygon.bounds
        tiles = (
            (self.tms.quadkey(tile), self.tile_to_polygon(tile))
            for tile in self.tms.tiles(x_min, y_min, x_max, y_max, self.zoom_level)
        )
        # Return dict to make it easier to deduplicate
        if filter:
            tiles = {qk: geom for qk, geom in tiles if polygon.intersects(geom)}
        else:
            tiles = {qk: geom for qk, geom in tiles}
        return tiles

# %% ../notebooks/00_grids.ipynb 14
@patch
def generate_grid(self: BingTileGridGenerator, gdf: GeoDataFrame) -> DataFrame:
    reprojected_gdf = gdf.to_crs("epsg:4326")  # quadkeys hexes are in epsg:4326 CRS
    tiles = {}
    unary_union = reprojected_gdf.unary_union
    if isinstance(unary_union, Polygon):
        tiles.update(self.get_tiles_for_polygon(unary_union))
    else:
        for geom in reprojected_gdf.unary_union.geoms:
            _tiles = self.get_tiles_for_polygon(geom)
            tiles.update(_tiles)
    quadkey, geom = zip(*((k, v) for k, v in tiles.items()))

    if self.return_geometry is False:
        df = DataFrame({"quadkey": list(quadkey)})
        return df

    tiles_gdf = GeoDataFrame(
        {"quadkey": list(quadkey)},
        geometry=list(geom),
        crs="epsg:4326",
    )
    return tiles_gdf.to_crs(gdf.crs)
