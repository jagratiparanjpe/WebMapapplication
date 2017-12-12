# Generate WebMap for Public Schools in Sydney based on the cordinates. Layer control is also added to the map based on type of school(Fully Selective, Not Selective, partially Selective )

import folium
import pandas

# colour generator based on selective school type
def colourGenerator(selective):
    if selective == 'Not Selective':
        print('Orange')
        return 'Orange'
    else:
        print('Green')
        return 'Green'

map = folium.Map(location=[-37.482772, 155.190084], zoom_start=6)
fg_school = folium.FeatureGroup("Schools")
fg_selective_school = folium.FeatureGroup("Selective Schools")
fg_partially_school = folium.FeatureGroup("Partially Selective Schools")


data = pandas.read_csv("out_p1.csv")
school_name = list(data["School_name"])
print(school_name)
lat = list(data["Latitude"])
lon = list(data["Longitude"])
selective = list(data["Selective_school"])
print("selective = " + str(selective))
for la,lo,name,sel in zip(lat, lon, school_name, selective):
    if sel == 'Fully Selective':
        fg_selective_school.add_child(
            folium.Marker(location=[la, lo], popup=str(name), icon=folium.Icon(icon='university', color='green')))
    elif sel == 'Partially Selective':
        fg_partially_school.add_child(
            folium.Marker(location=[la, lo], popup=str(name), icon=folium.Icon(color='orange')))
    else:
        fg_school.add_child(
            folium.Marker(location=[la, lo], popup=str(name), icon=folium.Icon(color='yellow')))

    print(la,lo,name, sel)
map.add_child(fg_selective_school)
map.add_child(fg_partially_school)
map.add_child(fg_school)
map.add_child(folium.LayerControl())
map.save("map2.html")

