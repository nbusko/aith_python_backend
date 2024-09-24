import json
from urllib.parse import parse_qs
import uvicorn

from calculations import calculate_factorial, calculate_fibonacci, calculate_mean

async def factorial(n_values : list):
    if not n_values or len(n_values) != 1:
        status_code = 422
        response_body = json.dumps({"error": "Missing or invalid 'n' parameter"})
    else:
        try:
            n = int(n_values[0])
            if n < 0:
                status_code = 400
                response_body = json.dumps({"error": "n must be a non-negative integer"})
            else:
                result = calculate_factorial(n)
                status_code = 200
                response_body = json.dumps({"result": result})
        except ValueError:
            status_code = 422
            response_body = json.dumps({"error": "'n' must be an integer"})
    return status_code, response_body

async def fibonacci(path : int):
    try:
        n = int(path.split('/')[-1])
        if n < 0:
            status_code = 400
            response_body = json.dumps({"error": "n must be a non-negative integer"})
        else:
            result = calculate_fibonacci(n)
            status_code = 200
            response_body = json.dumps({"result": result})
    except ValueError:
        status_code = 422
        response_body = json.dumps({"error": "'n' must be a valid integer"})
    return status_code, response_body

async def mean(body : list):
    try:
        numbers = json.loads(body)
        if not isinstance(numbers, list) or not all(isinstance(num, (int, float)) for num in numbers):
            status_code = 422
            response_body = json.dumps({"error": "All elements must be valid floats"})
        elif not numbers:
            status_code = 400
            response_body = json.dumps({"error": "Array cannot be empty"})
        else:
            result = calculate_mean(numbers)
            status_code = 200
            response_body = json.dumps({"result": result})
    except json.JSONDecodeError:
        status_code = 422
        response_body = json.dumps({"error": "Invalid JSON format"})
    return status_code, response_body

async def app(scope, receive, send):
    assert scope['type'] == 'http'
    method = scope['method']
    path = scope['path']

    status_code = 404
    response_body = json.dumps({"error": "Not Found"})

    if path == '/factorial' and method == 'GET':
        query_string = scope['query_string'].decode()
        query_params = parse_qs(query_string)
        n_values = query_params.get('n')
        status_code, response_body = await factorial(n_values)

    elif path.startswith('/fibonacci/') and method == 'GET':
        status_code, response_body = await fibonacci(path)
    
    elif path == '/mean' and method == 'GET':
        body = await receive_body(receive)
        status_code, response_body = await mean(body)
    
    await send({
        'type': 'http.response.start',
        'status': status_code,
        'headers': [(b'content-type', b'application/json')],
    })

    await send({
        'type': 'http.response.body',
        'body': response_body.encode(),
    })

async def receive_body(receive):
    body = b''
    more_body = True
    while more_body:
        message = await receive()
        body += message.get('body', b'')
        more_body = message.get('more_body', False)
    return body