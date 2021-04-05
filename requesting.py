import requests
import json

# CREATING NEW CAR
resp = requests.post("http://localhost:5000/cars", data=json.dumps({"car": {"model": "test", "color": "test text"}}))
assert json.loads(resp.text) == {"model": "test", "color": "test text", "id": "1"}

# # CREATING ANOTHER CAR
# resp = requests.post("http://localhost:5000/cars", data=json.dumps({"model": "test2", "color": "another test text"}))
# assert json.loads(resp.text) == {"model": "test2", "color": "another test text", "id": "2"}
#
# # RETURNING ALL cars
# resp = requests.get("http://localhost:5000/cars")
# assert len(json.loads(resp.text)) == 2
#
# # FINDING CAR BY ID
# resp = requests.get("http://localhost:5000/cars/1")
# assert json.loads(resp.text) == {"model": "test", "color": "test text", "id": "1"}
#
# # FINDING CAR BY ID (CAR IS NOT FOUND)
# resp = requests.get("http://localhost:5000/cars/0")
# assert json.loads(resp.text) == {"error": "CAR NOT FOUND"}
#
# # UPDATING CAR BY ID
# resp = requests.put("http://localhost:5000/cars/1", data=json.dumps({"model": "test changed", "color": "test text changed"}))
# assert json.loads(resp.text) == {"model": "test changed", "color": "test text changed", "id": "1"}
#
# # CHECKING IF THROWS ERROR ON NOT FOUND
# resp = requests.put("http://localhost:5000/cars/0", data=json.dumps({"model": "test changed", "color": "test text changed"}))
# assert json.loads(resp.text) == {"error": "CAR NOT FOUND"}
#
# # REMOVING CAR BY ID
# resp = requests.delete("http://localhost:5000/cars/1")
# assert json.loads(resp.text) == {"message": "CAR WAS DELETED"}
#
# # RETURNING ALL cars
# resp = requests.get("http://localhost:5000/cars")
# assert len(json.loads(resp.text)) == 1
#
# # CHECKING IF THROWS ERROR ON NOT FOUND
# resp = requests.delete("http://localhost:5000/cars/1")
# assert json.loads(resp.text) == {"error": "CAR NOT FOUND"}
#
# # RETURNING ALL cars
# resp = requests.get("http://localhost:5000/cars")
# assert len(json.loads(resp.text)) == 1