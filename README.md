# Fast-JSON-API
📘 "stand on the shoulders of a man standing on the shoulders of giants"

[![Code style: black](https://img.shields.io/badge/code%20style-black-000000.svg)](https://github.com/psf/black)
[![Imports: isort](https://img.shields.io/badge/%20imports-isort-%231674b1?style=flat&labelColor=ef8336)](https://pycqa.github.io/isort/)

Ever felt short of documentations on error handling in FastAPI?

FastAPI provides a easy and efficient API setup right off the bat.<br>
However, when it comes to exception handling, there are multiple handlers taking care of errors,<br>
making it difficult to turn all the error output formats into a custom format.


**Ex.** 

- In plain FastAPI, errors will return by default,

```
422 Unprocessable Entity
{
  "detail": [
    {
      "loc": [
        "body",
        0
      ],
      "msg": "Expecting value: line 1 column 1 (char 0)",
      "type": "value_error.jsondecode",
      "ctx": {
        "msg": "Expecting value",
        "doc": "]",
        "pos": 0,
        "lineno": 1,
        "colno": 1
      }
    }
  ]
}
```

- Want to change it into the following?

```
406 Not acceptable
{
  "code": "NOT_ACCEPTABLE",
  "message": "Either content-type or the body is not in a valid 'application/json' form."
}
```

**Key features**

 - A simple wrapper: Use all the existing features of FastAPI
 - Distiguish error types by HTTP status codes
 - Customizable error output format
 - Focuses on JSON-in/JSON-out APIs

Any modifications and suggestions are welcome!


## Notes

[FastAPI](https://github.com/tiangolo/fastapi) / [Starlette](https://www.starlette.io/middleware/) handles errors in the following architecture

- Middleware
  - ServerErrorMiddleware
  - TrustedHostMiddleware
  - HTTPSRedirectMiddleware
  - ExceptionMiddleware
- Routing
- Endpoint

## Examples

```
❯ curl --request POST 'http://localhost:8882/v1/post/sort' \
       --header 'Content-Type: application/json' \
       --data-raw '{"intArr":[1,2,5,7,3,11,8,9,10]}'
200 OK
{
  "result":[1,2,3,5,7,8,9,10,11]
}

❯ curl --request POST 'http://localhost:8882/v1/post/sort' \
       --header 'Content-Type: application/json' \
       --data-raw '{"intArr":[1,2,5,7,3,11,8,9,10], "method": "stalin"}'
200 OK
{
  "result":[1,2,5,7,11]
}


❯ curl --request POST 'http://localhost:8882/v1/post/sort' \
       --header 'Content-Type: application/json' \
       --data-raw '{"arrInt":[1,2,5,7,3,11,8,9,10]}'
422 Error
{
  "code":"INVALID_PARAMETER_VALUE",
  "message":"body.intArr: field required"
}


❯ curl --request POST 'http://localhost:8882/v1/post/sort' \
       --header 'Content-Type: application/json' \
       --data-raw '{"intArr":[1,2,5,7,3,11,8,9,10], "q": "hello"}'
422 Error
{
  "code":"INVALID_PARAMETER_VALUE",
  "message":"body.q: extra fields not permitted"
}


❯ curl --request POST 'http://localhost:8882/v1/post/sort' \
       --header 'Content-Type: application/json' \
       --data-raw '{"intArr":[1,2,5,7,3,11,8,9,10], "method": "stailn"}'
422 Error
{
  "code":"INVALID_PARAMETER_VALUE",
  "message":"body.method: value is not a valid enumeration member; permitted: 'merge', 'stalin'"
}


❯ curl --request POST 'http://localhost:8882/v1/post/sort' \
       --header 'Content-Type: application/json' \
       --data-raw '}'
400 Error
{
  "code":"BAD_REQUEST",
  "message":"Invalid input payload: 'NoneType' object has no attribute 'intArr'"
}
```
