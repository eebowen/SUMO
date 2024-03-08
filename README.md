# SUMO

More instructions here:
[Notion](https://luxuriant-shoulder-522.notion.site/SUMO-741e2017f4d04560a0279fe24dc47b53?pvs=4)

## 1. Download the map

go to `/SUMO_HOME/tools`

python `osmWebWizard.py`

downloaded map will be in tools folder 

## 2. Converting from p1t2 simulation network road.geojson

convert road.geojson —> .OSM —> .osm.xml —> save it in the folder —> add sumo config file.

[https://github.com/tyrasd/geojsontoosm](https://github.com/tyrasd/geojsontoosm)

```bash
export NODE_OPTIONS="--max-old-space-size=8192"
geojsontoosm road.geojson > road.osm

netconvert --osm-files road.osm -o baseline.net.xml

```

## 3. generate start and stop points from GPS locations.

[Duarouter](https://sumo.dlr.de/docs/duarouter.html) to generate trips 

1. Convert start and end gps locations to edges and exact positions on edges.
    
    python `gps_edges_pos.py`
    
2. Edit `trips_GEO.xml` with `departPos` and `arrivalPos` to determine the exact location on a network edge.  

```xml
<routes xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance" xsi:noNamespaceSchemaLocation="http://sumo.dlr.de/xsd/routes_file.xsd">
    <vType id="veh_passenger" vClass="passenger"/>
    <trip id="veh0" type="veh_passenger" depart="0.00" departLane="best" fromLonLat="-119.857028,34.416692" toLonLat="-119.865243,34.413587" departPos="10" arrivalPos="10"/>
</routes>
```

`duarouter --trip-files trips_GEO.xml --net-file osm.net.xml --output-file trip_geo_output.rou.xml`

## 4. Add waypoints (Optional):

[https://sumo.dlr.de/docs/Definition_of_Vehicles,_Vehicle_Types,_and_Routes.html#stops_and_waypoints](https://sumo.dlr.de/docs/Definition_of_Vehicles,_Vehicle_Types,_and_Routes.html#stops_and_waypoints)

```xml
<routes xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance" xsi:noNamespaceSchemaLocation="http://sumo.dlr.de/xsd/routes_file.xsd">
    <vType id="veh_passenger" vClass="passenger"/>
    <vehicle id="veh0" type="veh_passenger" depart="0.00" departLane="best">
        <route edges="88142688 396935402 396935399 1060013921 992135723 958186198#0 958186198#1 958186198#2 88142690#0 88142690#2 88142690#4 255330035#3 706545922#0 706545922#3 1050287139#0 1050287139#1 706545923#1 -224384010#1 -87376675#0 -598020852#1 -598020852#0 -598020855#1 -598020854#0 -263819574#1 -263819574#0 -598020853#1 -87376703#0 -514675663 -406580281#1 -406580281#0 87376669#0 87376669#1 416877246 28808425#1 28808425#2 517260068#0 517260068#1 -146155465#7 -146155465#6 -146155465#4 -146155465#3 -146155465#2 -146155465#1 28808560#2 28808539#0 28808539#1 28808539#2 28808539#3 28808543#0 28808543#1 -28808543#1"/>
        <stop lane="958186198#1_0" until="100"/>
        <stop lane="958186198#1_0" duration="100"/>
    </vehicle>
</routes>
```

## 5. Build config file: (baseline example)

```xml
<configuration>
    <input>
        <net-file value="baseline.net.xml"/>
        <route-files value="baseline.rou.xml"/>
    </input>
    <gui_only>
        <start value="false"/>
    </gui_only>
</configuration>
```

## 6. Output to file

`sumo -c osm.sumocfg --fcd-output fcdOutputGeo.xml --fcd-output.geo`