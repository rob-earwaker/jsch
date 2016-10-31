[![Build Status](https://travis-ci.org/rob-earwaker/jsch.svg?branch=master)]
(https://travis-ci.org/rob-earwaker/jsch)
[![Coverage Status]
(https://coveralls.io/repos/github/rob-earwaker/jsch/badge.svg?branch=master)]
(https://coveralls.io/github/rob-earwaker/jsch?branch=master)

# jsch
Define classes that conform to a [JSON schema](http://json-schema.org/), with
built-in validation and schema generation.

## Creating a schema object
A `Schema` object represents a validated JSON schema. Any recognised
JSON schema field can be passed as a keyword argument when initialising a
`Schema` object:

```python
>>> from jsch.schema import Schema
>>>
>>> Schema()
<jsch.schema.Schema object at 0x...>
>>>
>>> schema = Schema(title='First name', type='string', max_length=32)
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

A `SchemaValidationError` will be raised on initialisation if any
[JSON schema validation]
(http://json-schema.org/latest/json-schema-validation.html) rules are breached:

```python
>>> from jsch.schema import Schema
>>>
>>> Schema(title='Luggage', type='array', max_items=0.5)
Traceback (most recent call last):
  ...
jsch.schema.SchemaValidationError: 'max_items' must be an int
>>>
>>> Schema(title='Height', type='object', required=[])
Traceback (most recent call last):
  ...
jsch.schema.SchemaValidationError: 'required' list must not be empty
>>>
```

The schema validation rules in the JSON schema specification go a long way
towards ensuring a schema is valid, but there are still some gaps, especially
around inter-keyword validation. For more strict validation when creating a
schema object, use the `SchemaStrict` class instead:

```python
>>> # not yet implemented
>>> 
```

## Accessing the JSON schema
The JSON schema can be accessed as either a `dict` or a JSON string:

```python
>>> from jsch.schema import Schema
>>>
>>> schema = Schema(
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
>>> from jsch.schema import Schema
>>>
>>> schema = Schema(title='Height', type='number')
>>>
>>> json = schema.asjson(pretty=True, root=True)
>>> print(json)
{
    "$schema": "http://json-schema.org/draft-04/schema#",
    "title": "Height",
    "type": "number"
}
>>>
>>> dict = schema.asdict(root=True, schema='http://jsch.org/custom-schema#')
>>> import pprint
>>> pprint.pprint(dict)
{'$schema': 'http://jsch.org/custom-schema#',
 'title': 'Height',
 'type': 'number'}
>>>
```

## Simplifying schema object creation
For convenience, a class is provided for each of the primitive JSON schema
types, to save specifying the `type` keyword:

```python
>>> from jsch.schema import Array, Integer, String
>>>
>>> schema = String(pattern='^[0-9]{4}$')
>>> json = schema.asjson(pretty=True)
>>> print(json)
{
    "pattern": "^[0-9]{4}$",
    "type": "string"
}
>>>
>>> schema = Array(items=Integer(), min_items=1)
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