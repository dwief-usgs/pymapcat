========
pymapcat
========


.. image:: https://readthedocs.org/projects/pymapcat/badge/?version=latest
        :target: https://pymapcat.readthedocs.io/en/latest/?badge=latest
        :alt: Documentation Status




Python methods to assist in (TerriaJS based) map catalog development.


* Free software: unlicense
* Documentation: https://pymapcat.readthedocs.io.

Contacts
--------
* Daniel Wieferich (dwieferich@usgs.gov)

Purpose
-------
Python methods to assist in (TerriaJS based) map catalog development.

Requirements
------------
Requirements.txt shows condensed version of packages, while requirements_dev shows a full list of packages used in development.

Getting Started
---------------
Install the package

* pip install git+https://github.com/dwief-usgs/pymapcat.git

**Example 1** First build a catalog.

.. code-block:: python
	
	# Import packages
	from pymapcat import pymapcat

        # Create item for group
        item_name = "item name"
        item_desc = "item description."
        source_url = "https://sourceurl.com"
        visual_type = "esri-mapServer"
        visual_url = "https://test.gov/arcgis/rest/services/t/MapServer"

        item = pymapcat.BuildItem(item_name, item_desc, source_url, is_open=False)
        item.add_vis(visual_type, visual_url)

        # Create group for catalog, add item
        group_name = "Group Name Here"
        group_desc = "Group description here."
        group = pymapcat.BuildGroup(group_name, group_desc, is_open=True)
        group.add_item(item.item)

        # Create catalog
        catalog = pymapcat.BuildCatalogJson()
        catalog.add_group(group.group)

        # Display catalog  - see example 1 results
        catalog.catalog

**Example 1 results** shows catalog item.

.. code-block::

        {'homeCamera': {'west': -178.5, 'south': 13, 'east': -64.5, 'north': 71.5}, 
        'initialCamera': {'west': -178.5, 'south': 13, 'east': -64.5, 'north': 71.5}, 
        'initialViewerMode': '2d', 
        'catalog': [
                {'name': 
                'Group Name Here', 'description': 
                'Group description here.', 
                'type': 'group', 
                'isOpen': True, 
                'preserveOrder': True, 
                'items': [
                        {'name': 'item name', 
                        'description': 'item description', 
                        'dataSourceUrl': 'https://sourceurl.com', 
                        'isOpen': False, 'type': 'esri-mapServer', 
                        'metadataUrl': 'https://sourceurl.com', 
                        'url': 'https://test.gov/arcgis/rest/services/t/Maperver', 
                        'useStyleInformationFromService': True, 
                        'isMappable': True
                        }
                ]}
        ]}


Copyright and License
---------------------
This USGS product is considered to be in the U.S. public domain, and is licensed under unlicense_

.. _unlicense: https://unlicense.org/

This software is preliminary or provisional and is subject to revision. It is being provided to meet the need for timely best science. The software has not received final approval by the U.S. Geological Survey (USGS). No warranty, expressed or implied, is made by the USGS or the U.S. Government as to the functionality of the software and related material nor shall the fact of release constitute any such warranty. The software is provided on the condition that neither the USGS nor the U.S. Government shall be held liable for any damages resulting from the authorized or unauthorized use of the software.

Credits
-------

This package was created with Cookiecutter_ and the `audreyr/cookiecutter-pypackage`_ project template.

.. _Cookiecutter: https://github.com/audreyr/cookiecutter
.. _`audreyr/cookiecutter-pypackage`: https://github.com/audreyr/cookiecutter-pypackage
