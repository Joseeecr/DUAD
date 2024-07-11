list_to_avoid_keys = [
    "access_level",
    "age",
]
employee = {
    "name": "Jose",
    "age": 22,
    "Email": "jose.blanco@corp.com",
    "access_level" : 5,
}

for deleted_key in list_to_avoid_keys:
    if deleted_key in employee:
        del employee[deleted_key]
print(employee)