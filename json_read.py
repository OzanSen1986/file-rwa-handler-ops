import typing
import datetime
import json

# read from a json string
json_string = '''[{
"name":"PROD1",
"price": 9.99,
"type": "Cleaning-Materials",
"in_stock":true
},
{
"name":"PROD2",
"price": 10.99,
"type": "Beauty-Care",
"in_stock":false
},
{
"name":"PROD3",
"price": null,
"type": "Fresh-Products",
"in_stock":false
}
]'''

def read_json_string():
    try:
        result = json.loads(json_string)
    except TypeError as e:
        return f'Type Error: {e}'
    finally:
        for row in result:
            print(row)

# read a json from a file.

file_to_read = "json-sample.json"

def read_json() -> None:
    with open(file_to_read, "r") as file:
        result = json.load(file)
    
    id = result["user"]['id']
    username = result['user']['username']
    street = result["user"]["profile"]["address"]["street"]
    orders = result["user"]["orders"]
    for order in orders:
        print(order)

def main():
    read_json_string()
    # read_json()

if __name__ == "__main__":
    main()


