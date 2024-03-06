import requests, json

#constrct body of http request
# dumps allows us to put python diction and wrap it up
json_body = json.dumps({"postcodes":["PR3 0SG", "M45 6GN", "EX16 5BL"]})

print(type(json_body))

# Define custom headers
headers = {"Content-Type": "application/b_json"}

# Make the POST request with custom headers
post_multi_req = requests.post("https://api.postcodes.io/postcodes/", headers=headers, data=json_body)

# Print the JSON
print("JSON:", post_multi_req.json())
# Print the response status code
print("Response Status Code:", post_multi_req.status_code)


# Random
random_postcode = requests.get("https://api.postcodes.io/random/postcodes")
print("Random", random_postcode.json())