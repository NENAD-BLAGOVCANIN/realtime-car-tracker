import geocoder
from firebase import update_location

g = geocoder.ip('me')
print(g.latlng)

update_location(g.latlng[0], g.latlng[1])