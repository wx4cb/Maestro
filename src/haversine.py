"""
Calculate the great circle distance between two points 
on the earth (specified in decimal degrees)
"""
from math import radians, cos, sin, asin, sqrt

def haversine(lon1, lat1, lon2, lat2):
    # convert decimal degrees to radians 
    lon1, lat1, lon2, lat2 = map(radians, [lon1, lat1, lon2, lat2])

    # haversine formula 
    dlon = lon2 - lon1 
    dlat = lat2 - lat1 
    a = sin(dlat/2)**2 + cos(lat1) * cos(lat2) * sin(dlon/2)**2
    c = 2 * asin(sqrt(a)) 
    r = 3956 # 6371 Radius of earth in kilometers. Use 3956 for miles
    return c * r


#Lat/long pair for home position
home_lat = 29.16486
home_lon = -81.048550

# lat/long pair for uav
uav_lat = 29.72831
uav_lon = -82.93875


if __name__ == '__main__':
    try:
        print "Home Lat/Long: ", home_lat, home_lon
	print "UAV Lat/Long:  ", uav_lat, uav_lon
	bearing = haversine(home_lon, home_lat, uav_lon, uav_lat)

	print "Bearing: ", bearing % 360

    except KeyboardInterrupt:
        print 'Interrupted'
        sys.exit(0)
