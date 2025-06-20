import json
import requests
# Request the data from wspr.live
json_string = requests.get('http://db1.wspr.live/?query=SELECT * FROM wspr.rx LIMIT 50 format JSON')
# Parse the returned data into an object
python_object = json.loads(json_string.text)
# Print the values in the object
for i in range(len(python_object["data"])):
    print (python_object["data"][i]["rx_loc"], python_object["data"][i]["rx_lat"], python_object["data"][i]["rx_lon"])