import http.client
import json

# Simulating an API request
def make_api_request(method, path, body=None):
    conn = http.client.HTTPSConnection("api.example.com")
    headers = {'Content-type': 'application/json'}
    
    conn.request(method, path, body, headers)
    response = conn.getresponse()
    
    print(f"Status: {response.status} {response.reason}")
    print("Headers:", response.getheaders())
    
    data = response.read().decode()
    if data:
        print("Body:", json.loads(data))
    
    conn.close()

# GET request
print("GET Request:")
make_api_request("GET", "/api/resource")
# Expected output: Status, Headers, and Body of the GET response

# POST request
print("\nPOST Request:")
body = json.dumps({"key": "value"})
make_api_request("POST", "/api/resource", body)
# Expected output: Status, Headers, and Body of the POST response

# PUT request
print("\nPUT Request:")
body = json.dumps({"updated_key": "updated_value"})
make_api_request("PUT", "/api/resource/1", body)
# Expected output: Status, Headers, and Body of the PUT response

# DELETE request
print("\nDELETE Request:")
make_api_request("DELETE", "/api/resource/1")
# Expected output: Status, Headers, and Body (if any) of the DELETE response

# This code demonstrates:
# 1. Basic structure of HTTP requests and responses
# 2. Implementation of different HTTP methods (GET, POST, PUT, DELETE)
# 3. Handling of headers and body in requests and responses
# 4. Parsing of JSON data in responses


print('''
#Created by: Ayesha Noreen |Follow us on www.linkedin.com/in/khatoonintech | We love #AUGUSTHON 💕
    ''')
