# Contact Book API
This project provides a RESTful API to manage a contact book. The API is built using Flask and Flask-RESTful.

## Requirements
To run this project, you need to have Python 3 installed on your system.

## Installation
1. Clone the repository:
`git clone https://github.com/<username>/contact-book-api.git`

2. Install the required packages:
`pip install -r requirements.txt`

3. Run the application:
`flask run`

## Requirements
To run this project, you need to have Python 3 installed on your system.

## Installation
1. Clone the repository:
`git clone https://github.com/<username>/contact-book-api.git`

2. Install the required packages:
`pip install -r requirements.txt`

3. Run the application:
`flask run`

## API Endpoints
The following endpoints are available

| Endpoints  | Method | Description                     |
|------------|--------|---------------------------------|
| /contacts  | GET    | Retrieve a list of contacts     |
| /contacts  | POST   | Create a new contact            |
| /contacts/ | GET    | Retrieve a single contact by ID |
| /contacts/ | PUT    | Update a single contact by ID   |
| /contacts/ | DELETE | Update a single contact by ID   |


## Exception Handling
In case of any errors, the API returns a JSON response with the following format:
`{
    "message": "Error while retrieving the contact",
    "error": str(e),
    "status": 500,
}`

## Contribute
If you would like to contribute to this project, please fork the repository and create a pull request.

## License
This project is licensed under the MIT License.