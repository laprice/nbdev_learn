"""imports folium and sets up defaults so that it shows a view centered on Oregon"""

# AUTOGENERATED! DO NOT EDIT! File to edit: ../nbs/oregon_map.ipynb.

# %% auto 0
__all__ = ['basemap', 'overlay', 'Map']

# %% ../nbs/oregon_map.ipynb 3
def basemap(URI):
    # accepts the uri of a tileserver or static basemap.
    # returns a template url and bounding box and extra geometry
    pass

def overlay(DSN):
    # accepts a data source name
    pass


def Map():
    # default location https://www.openstreetmap.org/#map=7/43.942/-120.553
    m = folium.Map((43.942,-120.533),tiles="Esri.WorldPhysical",zoom_start=7)
    return m
