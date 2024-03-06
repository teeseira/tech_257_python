import requests

post_codes_req = requests.get("https://api.postcodes.io/postcodes/se120nb")

print("Status code:", post_codes_req.status_code)
print("Headers:", post_codes_req.headers)
print("Json:", post_codes_req.json())
print("Type:", type(post_codes_req.json()))


# Find Key-value pair in a long dictionary

data_dict = post_codes_req.json()['result']
print(data_dict)
print(f"Parish: {data_dict['parish']}")