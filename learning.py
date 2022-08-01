#tips to work with json data
import json
response = {"entries": [  { "id" : "yy"}, {"id" : "xx"} ]} #dict

print(type(response))

print("---entries list--")
entries_list =response['entries']
print(entries_list)

print(type(entries_list)) #list

for entry in entries_list:
    print(entry['id']) #dict


#String to json
emp = '{"name": "Maha", "id": 1, "city": "yy"}' #string
emp_json = json.loads(emp)
print(emp_json)
print(type(emp_json)) #dict

#json to string
payload = {'aa': 3} #dict
string_output = json.dumps(payload)
print(type(string_output)) #string
print(string_output)
