# Mauritius Emergency Services

Mauritius Emergency Services is an API that provides a list of emergency phone services in Mauritius.

## Installation

To run the API, install the following dependencies:

`pip install flask`

`pip install flask-restful`

## Base URL

`https://mauritius-emergency-services.herokuapp.com/`

## Usage

All responses will have the form

```json
{
    "services": "A JSON list of all available emergency services",
    "message" : "A description of what happened",
    "success" : "A boolean value to whether request succeeded or failed"
}
```

### Get services by language

***Available Languages***

English: `GET /en/{other parameters}`

French: `GET /fr/{other parameters}`


### List all services

**Definition**
`GET /en/services`

***Responses***

- `200 OK` on success

```json
{
    "services": [
        {
            "identifier": "police-direct-line-1",
            "name": "Police Direct Line 1",
            "type": "SECURITY",
            "icon": "https://www.icon.com/link_to_icon",
            "number": 999
        },
        {
            "identifier": "police-direct-line-2",
            "name": "Police Direct Line 2",
            "type": "SECURITY",
            "icon": "https://www.icon.com/link_to_icon",
            "number": 112
        }
    ],
    "message" : "",
    "success" : true
}
```

- `404 NOT FOUND` on failure
  
```json
{
    "services": [],
    "message" : "An error occurred while processing your request.",
    "success" : false
}
```

### Get a single service

**Definition**
`GET /en/service/{identifier}`

***Responses***

- `200 OK` on success

```json
{
    "services": [
        {
            "identifier": "police-direct-line-1",
            "name": "Police Direct Line 1",
            "type": "SECURITY",
            "icon": "https://www.icon.com/link_to_icon",
            "number": 999
        }
    ],
    "message" : "",
    "success" : true
}
```

- `404 NOT FOUND` if no services found
  
```json
{
    "services": [],
    "message" : "No services found under this identifier.",
    "success" : false
}
```

## License

```
Copyright Mervin Hemaraju

```