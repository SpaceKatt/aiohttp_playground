# Auth

### Register a user

#### Request
```
POST /auth/register

Headers:
{
    Content-Type: application/json
}

Body:
{
    username: <USER>,
    email: <EMAIL>,
    password: <PASSWORD>
}
```

#### Response
```
HTTP/1.1 201 Created
```
