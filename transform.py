import urllib2
import json
import requests
import time

json_str = '''{
"geometryType" : "esriGeometryPoint",
"geometries" : []
}'''
url = "http://tasks.arcgisonline.com/ArcGIS/rest/services/Geometry/GeometryServer/project?inSR=3945&outSR=4326&f=pjson&geometries="

f = open("geoloc.csv","r")
tree_geo = {}
for line in f.readlines():
	geo_obj = json.loads(json_str)
	points = line.split(",")
	points_dic = {"x":float(points[0]),"y":float(points[1].replace("\n",""))}
	geo_obj["geometries"].append(points_dic)
	geo_str = json.dumps(geo_obj)
	new_url = url + geo_str
	r = requests.get(new_url)
	result = json.loads(r.content)
	print r.content
	tree_geo[points[2].replace("\n","")] = result["geometries"][0]

f = open("geoloc_result","w")
f.write(json.dumps(tree_geo))
f.close()

print "ended"
