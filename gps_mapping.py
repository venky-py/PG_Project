from dronekit import connect
import folium

vehicle = connect('/dev/ttyAMA0', baud=57600, wait_ready=True)
lat = vehicle.location.global_frame.lat
lon = vehicle.location.global_frame.lon

map_ = folium.Map(location=[lat, lon], zoom_start=15)
folium.Marker([lat, lon], popup="Drone Location").add_to(map_)
map_.save("drone_location.html")
print("Map saved: Open drone_location.html in your browser.")
