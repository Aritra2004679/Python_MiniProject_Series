import csv
from gmplot import gmplot

# Create Google Map Object
gmap = gmplot.GoogleMapPlotter(23.0225, 72.5714, 5)

# Marker Style
gmap.coloricon = "http://www.googlemapsmarkers.com/v1/%s/"

# Lists to store route coordinates
latitude_list = []
longitude_list = []

with open('route.txt', 'r') as f:

    reader = csv.reader(f)

    first_point = True

    for row in reader:

        lat = float(row[0])
        long = float(row[1])

        # Store coordinates
        latitude_list.append(lat)
        longitude_list.append(long)

        # Starting Point
        if first_point:
            gmap.marker(lat, long, 'yellow')
            first_point = False

        # Intermediate Points
        else:
            gmap.marker(lat, long, 'blue')

# Final Destination Marker
gmap.marker(lat, long, 'red')

# Draw Route Line
gmap.plot(latitude_list, longitude_list,
          'blue', edge_width=2.5)

# Generate HTML Map
gmap.draw("mymap.html")

print("GPS Route Map Generated Successfully!")