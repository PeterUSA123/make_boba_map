from geopandas import GeoDataFrame
import pandas as pd
import geocoder
import googlemaps
from shapely.geometry import Point
from geojsonio import display


class BubbleTea(object):
    def __init__(self, filename):
        self.data = pd.read_csv(filename)

    def calc_coords(self):
        self.data['Lat'] = self.data['Address'].apply(
            geocoder.google).apply(lambda x: x.lat)
        self.data['Lng'] = self.data['Address'].apply(
            geocoder.google).apply(lambda x: x.lng)
        self.data['Coordinates'] = [
            Point(xy) for xy in zip(self.data.Lng, self.data.Lat)]

    def get_geo(self):
        return(list(self.boba['Coordinates']))

    def get_names(self):
        return(self.boba['Name'])

    def get_gdf(self):
        crs = {'init': 'epsg:4326'}
        return(GeoDataFrame(self.get_names(), crs=crs, geometry=list(self.calc_coords()))

    def visualize(self):
        updated=self.get_gdf()
        display(updated.to_json())
