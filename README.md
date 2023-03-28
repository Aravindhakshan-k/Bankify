# Bankify

This is a simple Django API that provides information on bank branches in India. The API retrieves its data from a CSV file of bank branch information.

## Endpoints

### Get Bank List

Retrieves a list of banks with their respective branches and IFSC codes.

**URL:** `/bank-list/<int:limit>/`

**Method:** GET

**URL Params:**

- `limit=[integer]`: Specifies the maximum number of records to retrieve. Default is 20.

**Success Response:**

- Code: 200 OK
- Content: 

[
{
"bank_name": "State Bank of India",
"branch": "MAIN BRANCH, BANGALORE",
"ifsc": "SBIN0000848"
},
{
"bank_name": "State Bank of India",
"branch": "GANDHINAGAR, BANGALORE",
"ifsc": "SBIN0001109"
},
...
]


### Get Bank Branch Details

Retrieves detailed information on a specific bank branch.

**URL:** `/bank-details/<str:ifsc>/`

**Method:** GET

**URL Params:**

- `ifsc=[string]`: The IFSC code of the bank branch to retrieve.

**Success Response:**

- Code: 200 OK
- Content:

{
"result": {
"bank_name": "State Bank of India",
"branch": "MAIN BRANCH, BANGALORE",
"address": "65, ST MARKS ROAD BANGALORE-560001",
"city": "BANGALORE",
"district": "BANGALORE URBAN",
"state": "KARNATAKA"
},
"status": 200
}

## Dependencies

- Django
- pandas

## Data Source

The data is sourced from [here](https://github.com/snarayanank2/indian_banks) and is provided in 'bank_branches.csv' file.
