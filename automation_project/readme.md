# Innovative Solution Development with Python, Django, and Robot Framework

This project is a solution to the recruitment challenge that involves creating a system to execute Robot Framework tests via an API endpoint using Python and Django.

## Objective

The core objective of this project is to develop an application that exposes an API endpoint. This endpoint should accept a POST request with a JSON payload containing test cases and execute the provided test steps using the Robot Framework. The project should then return the test output as the API response.

## Technologies Used

- Python
- Django
- Robot Framework

## Installation

1. Clone the repository:
- [Repository Link](https://github.com/MithunGJ7/recruitment_challenge.git)

2. Navigate to the project directory:
- cd project-repo

3. Install the required dependencies(All the dependencies are specified inside): 
- pip install -r dependencies.txt

## Usage

1. Start the Django development server:
- python manage.py runserver

2. Send a POST request to `http://127.0.0.1:8000/testai/tests/v1/execute` with the following JSON payload:

```json
{
    "tests" : [
        {
            "title": "Open google.com",
            "steps":[   
                "Open Browser  browser='chrome'",
                "Go To  url='https://google.com'"
            ]
        }
    ]
}
```

The API will execute the provided test steps using the Robot Framework and return the test output in the response.

## API Specification
- Endpoint: http://127.0.0.1:8000/testai/tests/v1/execute
- Method: POST
- Headers: Content-Type: application/json
- Request Body:
    - The request body should be a JSON payload containing an array of test cases under the tests key.
    - Each test case should have a title and an array of steps.
    - Each step is a command to be executed by the Robot Framework, such as opening a browser or navigating to a URL.

## Contributing
Feel free to use or modify this version according to your preferences! If you need further assistance or have any questions, just let me know.

## Thank You!!!
## Happy Learning.
