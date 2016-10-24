[![Build Status](https://travis-ci.org/rob-earwaker/jschema.svg?branch=master)]
(https://travis-ci.org/rob-earwaker/jschema)

# `jschema`
Define classes that conform to a JSON schema, with built-in validation and
schema generation.

## The `JSchema` Class
A `JSchema` object represents an unvalidated JSON schema. Any recognised JSON
schema field can be passed as a keyword argument when constructing a `JSchema`
object.

```
>>> import jschema
>>>
>>> jschema.JSchema(
...     description="JSchema object example",
...     type="string",
...     max_length=32
... )
<jschema.JSchema object at 0x...>

```
