# HTTP Requests

## Ch2 HTTP

- Hypertext Transfer Protocol
  - Defines how a **client** communicates to a **server**
  - Client send a **HTTP request**
    - Request line
      - Specifies the method and what to request for
    - Request header
    - Message body
  - Server responds with a **HTTP response**
    - Status line
    - Response header
      - Content type
    - Message body
- `import requests`

## Ch3 REST API

- **Web API**
  - Access server via a provided **endpoint**
- **REST API**
  - REpresentational State Transfer
    - Statelessness
    - Cacheability
    - Layered System
    - Uniform interface

## Ch4 HTTP Protocols

- `GET` request
  - To **read** or **retrieve** a resource
  - Parameterise the request by `?param=value&more=params`
- `POST` request
  - To **create** and **add** new data
- `PUT` request
  - To **update** existing data
- `DELETE` request
  - To **delete** an existing resource

## Ch5 Advanced Topics

- **Authentication**
  - Gives **authorisation** to specific content
- **Sessions**
  - "Remembers" the information given
  - Passes **cookies** to the client
    - Client passes the cookie back to the server for further interactions
- `Django` more heavyweight than `Flask`
