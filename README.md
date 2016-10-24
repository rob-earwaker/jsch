[![Build Status](https://travis-ci.org/rob-earwaker/jschema.svg?branch=master)]
(https://travis-ci.org/rob-earwaker/jschema)

# jschema
Define classes that conform to a JSON schema, with built-in validation and
schema generation.

## The JSchema Class
A `JSchema` object represents an unvalidated JSON schema. Any recognised JSON
schema field can be passed as a keyword argument when constructing a `JSchema`
object.

```python
>>> import jschema
>>>
>>> jschema.JSchema()
<jschema.JSchema object at 0x...>
>>>
>>> jschema.JSchema(
...     title="First name",
...     type="string",
...     max_length=32
... )
<jschema.JSchema object at 0x...>
>>>
```

Keywords are provided in the underscored format rather than the camel case
format used by the JSON schema definition, i.e. `max_length` rather than
`maxLength`. This is done to conform to the [PEP8 Style Guide](
https://www.python.org/dev/peps/pep-0008/).

The JSON schema can be accessed as either a `dict` or as a JSON string.

```python
>>> import jschema
>>>
>>> schema = jschema.JSchema(
...     description="Age",
...     type="integer",
...     minimum=0
... )
>>>
>>> import pprint
>>> pprint.pprint(schema.asdict())
{'description': 'Age', 'minimum': 0, 'type': 'integer'}
>>>
>>> print(schema.asjson())
{"description":"Age","minimum":0,"type":"integer"}

>>> print(schema.asjson(pretty=True))
{
    "description": "Age",
    "minimum": 0,
    "type": "integer"
}
>>>
```