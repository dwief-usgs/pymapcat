"""Methods to assist in building of data catalogs for use in terria based maps.

Author is using USGS Maps instance of terria.
Related terria documentation can be found at
https://docs.terria.io/guide/connecting-to-data/ .

"""
# import needed packages
import json

# set default variables
us_bounds = {"west": -178.5,
             "south": 13,
             "east": -64.5,
             "north": 71.5
             }


class BuildCatalogJson:
    """Class to build general catalog components."""

    def __init__(self, bounding_box=us_bounds, mode="2d"):
        """Initialize catalog object.

        Build catalog JSON based on TerriaMap specs.
        See https://docs.terria.io/guide/connecting-to-data/ for more detail.
        https://docs.terria.io/guide/customizing/initialization-files/
        homeCamera: where the camera goes when you click the "home" button

        Parameters
        ----------
        bounding_box: dict
            example below
            -> {"north": -8,
                "east": 158,
                "south": -45,
                "west": 109
                }
        mode: str
            Options inlcue
                '2d' two dimensional
                '3d' three dimensional

        """
        self.catalog = {"homeCamera": bounding_box,
                        "initialCamera": bounding_box,
                        "initialViewerMode": mode.lower(),
                        "catalog": []}

    def update_init_view(self, bounding_box=us_bounds):
        """If initial map view is different then home camera.

        initialCamera: the location when the map first displays.

        Parameters
        ----------
        bounding_box: dict
            example below
            -> {"north": -8,
                "east": 158,
                "south": -45,
                "west": 109
                }

        """
        self.catalog["initialCamera"] = bounding_box

    def add_group(self, group):
        """Add group to catalog."""
        self.catalog["catalog"].append(group)


class BuildGroup:
    """Class to build group for a catalog."""

    def __init__(self, name, description, is_open=False):
        """Initialize group obj.

        Build catalog JSON based on TerriaMap specs.
        See https://docs.terria.io/guide/connecting-to-data/ for more detail.

        Parameters
        ----------
        name: str
            Name of Catalog
        description: str
            Describes item, recommend sentence form
        is_open: str
            'true' catalog is expanded
            'false' catalog is collaposed

        """
        self.group = {"name": name,
                      "description": description,
                      "type": "group",
                      "isOpen": is_open,
                      "preserveOrder": True,
                      "items": []
                      }

    def add_item(self, item):
        """Add item to group."""
        self.group["items"].append(item)


class BuildItem:
    """Class to build item for a catalog."""

    def __init__(self, name, description, data_source_url, is_open=False):
        """Initialize item obj.

        Build catalog JSON based on TerriaMap specs.
        See https://docs.terria.io/guide/connecting-to-data/ for more detail.

        Parameters
        ----------
        name: str
            Name of Catalog
        description: str
            Describes item, recommend sentence form
        source_url: str
            url of where content was discovered
        is_open: str
            'true' catalog is expanded
            'false' catalog is collaposed

        """
        self.item = {"name": name,
                     "description": description,
                     "dataSourceUrl": data_source_url,
                     "isOpen": is_open,
                     "type": 'csv',
                     "metadataUrl": data_source_url,
                     #  "isMappable": False,
                     "initialMessage": {"title": "No Visual Representation.",
                                        "content": "This product has no spatial representation. See metadataUrl in catalog view for more information."
                                        }
                     }

    def add_data_custodian(self, custodian):
        """Add custodian to item.

        Parameters
        ----------
        custodian: str
            Name of individual or organization taking care of data

        """
        self.item["dataCustodian"] = str(custodian)

    def add_vis(self, vis_type, vis_url):
        """Add data information.

        Parameters
        ----------
        custodian: str
            Name of individual or organization taking care of data

        """
        # Can expand this list
        # https://docs.terria.io/guide/connecting-to-data/catalog-items/

        valid_vis = [
            'wms', 'wfs', 'esri-mapServer', 'esri-featureServer',
            'csv', 'geojson'
            ]

        if vis_type in valid_vis:
            self.item["type"] = vis_type
            self.item["url"] = vis_url
            self.item["useStyleInformationFromService"] = True
            self.item["isMappable"] = True

            del self.item["initialMessage"]


def export_json(name, data):
    """Export data to JSON file.

    Parameters
    name: str
        format 'directory/file_name.json'
    data: JSON

    """
    with open(name, 'w') as outfile:
        json.dump(data, outfile)
