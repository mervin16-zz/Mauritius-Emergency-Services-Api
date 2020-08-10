# Mauritius Emergency Services

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

**Available Languages**
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
            "icon": "https://www.icon.com/link_to_icon",
            "number": 999
        },
        {
            "identifier": "police-direct-line-2",
            "name": "Police Direct Line 2",
            "icon": "https://www.icon.com/link_to_icon",
            "number": 112
        }
    ],
    "message" : "",
    "success" : true
}
```

- `404 NOT FOUND` on failure
- 
```json
{
    "services": [],
    "message" : "An error occurred while processing your request.",
    "success" : false
}
```

### Get single service

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
            "icon": "https://www.icon.com/link_to_icon",
            "number": 999
        }
    ],
    "message" : "",
    "success" : true
}
```

- `404 NOT FOUND` if no services found
- 
```json
{
    "services": [],
    "message" : "No services found under this identifier.",
    "success" : false
}
```
