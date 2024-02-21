import json
dataset ='''{
  "person1": {
    "name": "John",
    "age": 32,
    "city": "London",
    "occupation": "Engineer"
  },
  "person2": {
    "name": "Alice",
    "age": 27,
    "city": "Tokyo",
    "occupation": "Teacher"
  },
  "person3": {
    "name": "Bob",
    "age": 41,
    "city": "New York",
    "occupation": "Artist"
  }
}'''

dict = json.loads(dataset)
string = str(dataset)
print("Developed by Milan Kumawat\n")
print("\nDataset:"+dataset)
print("\nDictionary:",dict)
print("Type:",type(dict))
print("\nString:",string)
print("Type:",type(string))
