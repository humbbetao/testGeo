import os
import requests

item_id = "20161218_101700_0e0d"
item_type = "PSScene4Band"
asset_type = "PSOrthoTile"

# setup auth
session = requests.Session()
session.auth = ("0ad9f1f36f204248aaac09a0ecc4dace", '')

# request an item
item = \
  session.get(
    ("https://api.planet.com/data/v1/item-types/" +
    "{}/items/{}/assets/").format(item_type, item_id))

# extract the activation url from the item for the desired asset
item_activation_url = item.json()[asset_type]["_links"]["activate"]

# request activation
response = session.post(item_activation_url)

print response.status_code
