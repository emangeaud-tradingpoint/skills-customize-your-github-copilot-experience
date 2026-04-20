# 📘 Assignment: REST APIs with FastAPI

## 🎯 Objective

Build a small REST API using the FastAPI framework to practice route creation, request handling, and JSON responses. You will create endpoints that return data and accept new input in a clear, structured format.

## 📝 Tasks

### 🛠️	Create the API Endpoints

#### Description
Use FastAPI to build a basic application with endpoints for checking that the API is running and for listing available items. Start from the provided starter code and complete the missing route behavior.

#### Requirements
Completed program should:

- Create a FastAPI application instance.
- Add a `GET /` endpoint that returns a welcome message in JSON format.
- Add a `GET /items` endpoint that returns a list of items.
- Return responses as valid JSON objects or arrays.


### 🛠️	Handle New Data with POST Requests

#### Description
Extend the API so users can send new item data to the server. Your application should accept a request body, add the new item to the in-memory list, and return the created result.

#### Requirements
Completed program should:

- Add a `POST /items` endpoint that accepts item data.
- Validate that each new item includes a name.
- Store new items in an in-memory Python list.
- Return the newly created item as JSON.
- Allow the `GET /items` endpoint to show items added during the current run of the program.