# Python Data Types

Python provides several built-in data types that are used to store different kinds of values.

---

# 1. Numeric Types

Numeric data types are used to store numbers.

## Integer (`int`)

Integers are whole numbers without decimal points.

### Example

```python
x = 10
y = -5
z = 0

print(type(x))
```

### Output

```python
<class 'int'>
```

---

## Float (`float`)

Floats are numbers with decimal points.

### Example

```python
pi = 3.14159
temperature = -12.5

print(type(pi))
```

### Output

```python
<class 'float'>
```

---

## Complex (`complex`)

Complex numbers contain a real and imaginary part.

### Example

```python
z = 2 + 3j

print(type(z))
```

### Output

```python
<class 'complex'>
```

---

# 2. String Type

## String (`str`)

Strings are used to store text.

### Example

```python
name = "Alice"
message = 'Hello World'

print(type(name))
```

### Output

```python
<class 'str'>
```

---

## Common String Operations

```python
first = "Hello"
second = "World"

# Concatenation
print(first + " " + second)

# Length
print(len(first))

# Uppercase
print(first.upper())

# Lowercase
print(second.lower())
```

---

# 3. Sequence Types

Sequence types store multiple values in an ordered manner.

---

## List (`list`)

Lists are ordered and mutable collections.

### Example

```python
fruits = ["apple", "banana", "orange"]

print(type(fruits))
```

### Output

```python
<class 'list'>
```

### List Operations

```python
fruits.append("grape")
fruits.remove("banana")

print(fruits)
print(fruits[0])
```

---

## Tuple (`tuple`)

Tuples are ordered but immutable collections.

### Example

```python
coordinates = (10, 20)

print(type(coordinates))
```

### Output

```python
<class 'tuple'>
```

---

## Range (`range`)

The `range()` function generates a sequence of numbers.

### Example

```python
numbers = range(5)

for n in numbers:
    print(n)
```

### Output

```python
0
1
2
3
4
```

---

# 4. Mapping Type

## Dictionary (`dict`)

Dictionaries store key-value pairs.

### Example

```python
student = {
    "name": "John",
    "age": 21,
    "grade": "A"
}

print(type(student))
```

### Output

```python
<class 'dict'>
```

### Accessing Dictionary Values

```python
print(student["name"])
print(student.get("age"))
```

### Adding New Values

```python
student["city"] = "Kathmandu"

print(student)
```

---

# 5. Set Types

Set types store unique values.

---

## Set (`set`)

Sets are unordered collections of unique items.

### Example

```python
colors = {"red", "green", "blue"}

print(type(colors))
```

### Output

```python
<class 'set'>
```

### Set Operations

```python
colors.add("yellow")
colors.remove("green")

print(colors)
```

---

## Frozen Set (`frozenset`)

A `frozenset` is an immutable version of a set.

### Example

```python
frozen = frozenset([1, 2, 3])

print(type(frozen))
```

### Output

```python
<class 'frozenset'>
```

---

# 6. Boolean Type

## Boolean (`bool`)

Boolean values represent either `True` or `False`.

### Example

```python
is_logged_in = True
has_permission = False

print(type(is_logged_in))
```

### Output

```python
<class 'bool'>
```

---

# 7. Binary Types

Binary data types are used to work with binary data.

---

## Bytes (`bytes`)

Bytes are immutable binary sequences.

### Example

```python
data = b"Hello"

print(type(data))
```

### Output

```python
<class 'bytes'>
```

---

## Bytearray (`bytearray`)

Bytearrays are mutable binary sequences.

### Example

```python
data = bytearray(5)

print(type(data))
```

### Output

```python
<class 'bytearray'>
```

---

## Memoryview (`memoryview`)

Memoryview objects allow access to internal memory.

### Example

```python
data = memoryview(bytes(5))

print(type(data))
```

### Output

```python
<class 'memoryview'>
```

---

# 8. None Type

## None (`NoneType`)

`None` represents the absence of a value.

### Example

```python
result = None

print(type(result))
```

### Output

```python
<class 'NoneType'>
```

---

# Type Checking in Python

Use the `type()` function to check a variable's data type.

### Example

```python
x = 10
print(type(x))
```

---

# Type Conversion

Python allows converting one data type into another.

## Example

```python
x = "100"

number = int(x)
decimal = float(x)
text = str(number)

print(number)
print(decimal)
print(text)
```

---

# Mutable vs Immutable Types

## Mutable Types

Mutable objects can be changed after creation.

Examples:

- list
- dict
- set
- bytearray

### Example

```python
numbers = [1, 2, 3]
numbers.append(4)

print(numbers)
```

---

## Immutable Types

Immutable objects cannot be changed after creation.

Examples:

- int
- float
- tuple
- str
- frozenset

### Example

```python
name = "Alice"

# Creates a new string
name = name + " Smith"

print(name)
```

---

# Summary Table

| Data Type | Description | Example |
|---|---|---|
| int | Whole numbers | `10` |
| float | Decimal numbers | `3.14` |
| complex | Complex numbers | `2 + 3j` |
| str | Text/string values | `"Hello"` |
| list | Ordered mutable collection | `[1, 2, 3]` |
| tuple | Ordered immutable collection | `(1, 2, 3)` |
| range | Sequence of numbers | `range(5)` |
| dict | Key-value pairs | `{"a": 1}` |
| set | Unique unordered values | `{1, 2, 3}` |
| frozenset | Immutable set | `frozenset([1,2])` |
| bool | Boolean values | `True` |
| bytes | Immutable binary data | `b"abc"` |
| bytearray | Mutable binary data | `bytearray(5)` |
| memoryview | Memory access object | `memoryview(bytes(5))` |
| NoneType | Absence of value | `None` |

---



