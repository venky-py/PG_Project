from shapely.geometry import Point, Polygon

geofence = [(37.7749, -122.4194), (37.7755, -122.4180), (37.7760, -122.4190)]

def is_inside_geofence(lat, lon):
    polygon = Polygon(geofence)
    return polygon.contains(Point(lat, lon))

lat, lon = 37.7750, -122.4185
if is_inside_geofence(lat, lon):
    print("Drone is inside geofence. Proceeding with mission.")
else:
    print("WARNING: Drone is outside geofence! Returning home.")
