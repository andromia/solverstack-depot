![depot](https://github.com/andromia/solverstack-depot/workflows/depot/badge.svg)

# solverstack-depot
Service for depot module.

## input

```
{
    "stack_id": integer,
    "nodes": [
        { "latitude": float, "longitude": float }
    ]
}
```

## output
_NOTE_: no id will return if auth is not valid (no CRUD)

```
{
    "stack_id": integer,
    "depots": [
        {   
            "id": integer,
            "latitude": float, 
            "longitude": float 
        }
    ]
}
```