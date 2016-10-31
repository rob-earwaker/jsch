[![Build Status](https://travis-ci.org/rob-earwaker/jschema.svg?branch=master)]
(https://travis-ci.org/rob-earwaker/jschema)
[![Coverage Status]
(https://coveralls.io/repos/github/rob-earwaker/jschema/badge.svg?branch=master)]
(https://coveralls.io/github/rob-earwaker/jschema?branch=master)

# jschema
Define classes that conform to a [JSON schema](http://json-schema.org/), with
built-in validation and schema generation.

## Creating a schema object
A `jschema.JSchema` object represents a validated JSON schema. Any recognised
JSON schema field can be passed as a keyword argument when initialising a
`jschema.JSchema` object:

```python
>>> import jschema
>>>
>>> jschema.JSchema()
<jschema.JSchema object at 0x...>
>>>
>>> schema = jschema.JSchema(title='First name', type='string', max_length=32)
>>> schema.max_length
32
>>> schema.title
'First name'
>>>
```

Keywords are provided in the underscored format rather than the camel case
format used by the JSON schema definition, i.e. `max_length` rather than
`maxLength`. This is done to conform to the [PEP8 Style Guide]
(https://www.python.org/dev/peps/pep-0008/).

A `jschema.SchemaValidationError` will be raised on initialisation if any
[JSON schema validation]
(http://json-schema.org/latest/json-schema-validation.html) rules are breached:

```python
>>> import jschema
>>>
>>> jschema.JSchema(
...     title='Luggage',
...     type='array',
...     max_items=0.5
... )
Traceback (most recent call last):
  ...
jschema.SchemaValidationError: 'max_items' must be an int
>>>
>>> jschema.JSchema(
...     title='Height',
...     type='object',
...     required=[]
... )
Traceback (most recent call last):
  ...
jschema.SchemaValidationError: 'required' list must not be empty
>>>
```

The schema validation rules in the JSON schema specification go a long way
towards ensuring a schema is valid, but there are still some gaps, especially
around inter-keyword validation. For more strict validation when creating a
schema object, use the `jschema.JSchemaStrict` class instead:

```python
>>> # not yet implemented
>>> 
```

## Accessing the JSON schema
The JSON schema can be accessed as either a `dict` or a JSON string:

```python
>>> import jschema
>>>
>>> schema = jschema.JSchema(
...     title='Approximate Age',
...     type='integer',
...     minimum=0,
...     multiple_of=10
... )
>>>
>>> dict = schema.asdict()
>>> import pprint
>>> pprint.pprint(dict)
{'minimum': 0, 'multipleOf': 10, 'title': 'Approximate Age', 'type': 'integer'}
>>>
>>> json = schema.asjson()
>>> print(json)
{"minimum":0,"multipleOf":10,"title":"Approximate Age","type":"integer"}
>>>
>>> pretty_json = schema.asjson(pretty=True)
>>> print(pretty_json)
{
    "minimum": 0,
    "multipleOf": 10,
    "title": "Approximate Age",
    "type": "integer"
}
>>>
```

If the schema is intended to be a root schema, specify the `root` flag with an 
optional `$schema` string when converting to a `dict` or a JSON string:

```python
>>> import jschema
>>>
>>> schema = jschema.JSchema(title='Height', type='number')
>>>
>>> json = schema.asjson(pretty=True, root=True)
>>> print(json)
{
    "$schema": "http://json-schema.org/draft-04/schema#",
    "title": "Height",
    "type": "number"
}
>>>
>>> dict = schema.asdict(root=True, schema='http://jschema.org/custom-schema#')
>>> import pprint
>>> pprint.pprint(dict)
{'$schema': 'http://jschema.org/custom-schema#',
 'title': 'Height',
 'type': 'number'}
>>>
```

## Simplifying schema object creation
For convenience, a class is provided for each of the primitive JSON schema
types, to save specifying the `type` keyword:

```python
>>> import jschema
>>>
>>> schema = jschema.String(pattern='^[0-9]{4}$')
>>> json = schema.asjson(pretty=True)
>>> print(json)
{
    "pattern": "^[0-9]{4}$",
    "type": "string"
}
>>>
>>> schema = jschema.Array(items=jschema.Integer(), min_items=1)
>>> json = schema.asjson(pretty=True)
>>> print(json)
{
    "items": {
        "type": "integer"
    },
    "minItems": 1,
    "type": "array"
}
>>>
```