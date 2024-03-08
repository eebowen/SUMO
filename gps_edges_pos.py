
import os
import sys

# Make sure the environment variable for SUMO_HOME is set
if 'SUMO_HOME' in os.environ:
    tools = os.path.join(os.environ['SUMO_HOME'], 'tools')
    sys.path.append(tools)
else:
    sys.exit("Please declare the environment variable 'SUMO_HOME'")

from sumolib import net  # Import the necessary module from sumolib
from sumolib.geomhelper import polygonOffsetWithMinimumDistanceToPoint

# Load your network
# network = net.readNet('../24sb/osm.net.xml')
network = net.readNet('../24sb/bowen_l3harris/l3harris.net.xml')


# Example GPS coordinate
# lon, lat = -122.473025, 37.779730

lon, lat = -122.402758, 37.774416
lon, lat = -122.45517, 37.768165
x, y = network.convertLonLat2XY(lon, lat)
edge = network.getNeighboringEdges(x, y, r=50)

# print(nearest_edge_list)
sorted_edges_by_distance = sorted(edge, key=lambda edge_distance: edge_distance[1])
# print(sorted_edges_by_distance)
nearest_edge = sorted_edges_by_distance[0][0]
print(f"The nearest edge ID to the GPS coordinate is: {sorted_edges_by_distance[0]}")


pos = polygonOffsetWithMinimumDistanceToPoint((x, y), nearest_edge.getShape())

print(pos)
# print(nearest_edge.getShape())