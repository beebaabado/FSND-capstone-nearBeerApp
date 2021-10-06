# Beer Server API documentation (NOT COMPLETE)
The beer server application provides access to information on beers (venues, breweries, ratings, ABV, and more)in certain localities.  It utilizes the untappd api.

This is a REST API that returns encoded JSON responses and uses standard HTTP response codes (success and error codes) and verbs (GET, POST, and DELETE).  You may create, retrieve, and delete API objects through this simple interface.  
>Note:  Update of API objects is not currently supported.
This documentation will take you through each end point providing the following information:  

- Endpoint description
- A sample curl statement to call the endpoint with necessary parameters
- Returned encoded JSON response

It is a REST API that returns 
## General Information

### Base URL
This project has been deployed on HEROKU at the following address:   `[https://capstone-nearbeer-app.herokuapp.com/](https://capstone-nearbeer-app.herokuapp.com/)` 

The backend is hosted locally at the following default address:

http://localhost:5000

http://127.0.0.1:5000


## Error handling - HTTP error codes

HTTP status/error codes and messages. This API returns the following status codes. Supported status and error handling includes 200 for successful requests and 4xx error codes for malformed requests to resource not available events.

Attributes

- success: Boolean. Returns False for all error codes.
- error: HTTP status code
- message: Human readable message with details about the error
  
### Status and Error codes

- 200 "OK": request was succesful.
  - response: varies, see documentation for specific endpoint

- 422 "unprocessable": request was not valid or server could not process the request

  - response
  ```json 
    {
        "success": False, 
        "error": 422,
        "message": "unprocessable"
    }
    ```

- 404 "resource not found": request was valid but the resouce was not found

  - response
  ```json
    {
    "success": False, 
    "error": 404,
    "message": "resource not found"
    }
  ```

- 400 "bad request": request was not formatted correctly

  - response
  ```json
    {
    "success": False, 
    "error": 400,
    "message": "bad request"
    }
   ```

- 405 "method not allowed": request specified unsupported method for request

  - response
  ```json
    {
    "success": False, 
    "error": 405,
    "message": "method not all0wed"
    }
  ```

- 500 "Internal Server Error": The server encountered an unexpected condition which prevented it from fulfilling the request.

  - response
  ```json
    {
    "success": False, 
    "error": 500,
    "message": "internal server error"
    }
  ```

- AuthError Generic error handler for Auth0 authorization error - returned by auth.py api

 - response
```json
    {
        "success": False,
        "error": error code returned by auth.py api
        "message": error message returned by auth.py api
    }
```
 

### AUTH0 ROLE BASED Authentication/access control necessary to access endpoints

Role: Brewer  
Description: Admin for Near Beer site.  Able to view/add/delete/update beers, styles, user ratings
Permissions:

- get:beer-details	Retrieve info for one beer
- get:beers	Retrieve list of beers
- get:styles	Retrieve list of beer styles
- patch:beer-user-rating	Update user rating for one beer
- post:beers	Add a new beer	
- view:simple	Simple table view for admin use


Role: Beer-lover  
Description: Beer enthusiast can view beers and update user ratings on beers.
Permissions: 

- get:beer-details	Retrieve info for one beer	
- get:beers	Retrieve list of beers
- patch:beer-user-rating	Update user rating for one beer 


## Endpoints

### GET beers/template  
Retrieves a listing of beers for given city / no authorization

- Request Arguments: city
- method: HTTP request method is GET (by default)
- Returns: table of beers for city as html template (jinja2)


### GET /beers  
Retrieves of listing of beers for given city.  Returns json / no authorization

- Request Arguments: city
- method: HTTP request method is GET (by default)
- Returns: list of beers in json format


### GET /
Retrives listing of all beers.  Returns json.  Requires authorization.
  
### GET /beers/<city>/  
Retrieves listing of beers by city.  Returns json.  Requires authorization.


### GET /beer-details/  
Retrieves details for beer id.  Returns json.  Requires authorization.
  
  
### GET /styles/
  @requires_auth('get:styles')
  
    return jsonify({
      "status_code": 200,
      "success": True,
      "style_count": len(formatted_styles),
      "styles": formatted_styles
      })

### POST /beers/

  @requires_auth('post:beers')

      return jsonify({
        "status_code": 200,
        "success": True,
        "created": new_beer.id
        }), 200
    except:
      abort(422, "Was not able to insert new beer record!")

### PATCH /rating/
  @requires_auth('patch:beer-user-rating')
  
      return jsonify({
        "status_code": 200,
        "success": True,
        "modified": beer.id
        }), 200
    except:
      abort(422)

### DELETE /beers/<int:beer_id>/
  @requires_auth('delete:beers')
  return jsonify({
        "status_code": 200,
        "success": True,
        "deleted": beer_id
        }), 200