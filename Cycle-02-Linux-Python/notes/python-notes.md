# Python Notes — Cycle 02

> Written in my own words with my own examples.  
> Covers: Data Types · Loops · Functions · File Handling

---

## 1. Data Types

Python figures out the type of a variable automatically — you don't declare it like in C or Java.

### Integers (`int`)
Whole numbers, positive or negative.

```python
age = 21
year = 2025
negative = -5

print(type(age))   # <class 'int'>
print(age + year)  # 2046
```

### Floats (`float`)
Numbers with a decimal point.

```python
temperature = 36.6
pi = 3.14159

# Watch out for floating-point precision
print(0.1 + 0.2)   # 0.30000000000000004  ← classic gotcha
```

### Strings (`str`)
Text, wrapped in single or double quotes.

```python
name = "Alice"
greeting = 'Hello, World!'

# f-strings make formatting easy (Python 3.6+)
user = "Bob"
port = 8080
print(f"Connecting to {user} on port {port}")  # Connecting to Bob on port 8080

# Useful string methods
ip = "  192.168.1.1  "
print(ip.strip())          # remove whitespace → "192.168.1.1"
print(ip.strip().split("."))  # split on dot → ['192', '168', '1', '1']
```

### Booleans (`bool`)
Only two values: `True` or `False`.

```python
is_open   = True
is_logged = False

print(type(is_open))   # <class 'bool'>

# Comparisons return booleans
port = 80
print(port == 80)   # True
print(port > 443)   # False
```

### Lists
Ordered, mutable collection. Can hold mixed types.

```python
open_ports = [22, 80, 443, 8080]
open_ports.append(3306)       # add to end
open_ports.remove(8080)       # remove by value
print(open_ports[0])          # 22  (zero-indexed)
print(len(open_ports))        # 4
```

### Dictionaries (`dict`)
Key → value pairs. Like a lookup table.

```python
port_services = {
    22:  "SSH",
    80:  "HTTP",
    443: "HTTPS",
}

print(port_services[80])        # HTTP
print(port_services.get(9999, "Unknown"))  # Unknown (safe lookup)

# Loop through key-value pairs
for port, service in port_services.items():
    print(f"Port {port} → {service}")
```

### Tuples
Like a list but **immutable** (can't change after creation). Good for fixed data.

```python
coordinates = (28.6139, 77.2090)  # lat, lon of New Delhi
print(coordinates[0])             # 28.6139
# coordinates[0] = 0  ← this would raise a TypeError
```

---

## 2. Loops

### `for` loop
Iterates over a sequence — list, range, string, dict, etc.

```python
# Loop over a range of port numbers
for port in range(1, 6):       # 1, 2, 3, 4, 5  (6 is excluded)
    print(f"Scanning port {port}")

# Loop over a list
targets = ["192.168.1.1", "192.168.1.2", "10.0.0.5"]
for ip in targets:
    print(f"Pinging {ip}...")

# Loop over a string character by character
password = "S3cur3!"
for char in password:
    print(char)
```

### `while` loop
Keeps running as long as a condition is `True`. Useful when you don't know how many iterations you need.

```python
# Retry logic — keep trying until success or max attempts reached
attempts = 0
max_attempts = 3

while attempts < max_attempts:
    password = input("Enter password: ")
    if password == "secret":
        print("Access granted!")
        break              # exit the loop early
    else:
        attempts += 1
        print(f"Wrong! {max_attempts - attempts} attempt(s) left.")

if attempts == max_attempts:
    print("Account locked.")
```

### `break` and `continue`

```python
# break → stop the loop entirely
for port in range(1, 1025):
    if port == 5:
        print("Found target port, stopping.")
        break

# continue → skip this iteration, go to next
for num in range(1, 11):
    if num % 2 == 0:   # skip even numbers
        continue
    print(num)         # prints 1, 3, 5, 7, 9
```

---

## 3. Functions

Functions let you package reusable code. Define once, call many times.

### Basic function

```python
def greet(name):
    print(f"Hello, {name}!")

greet("Alice")   # Hello, Alice!
greet("Bob")     # Hello, Bob!
```

### Function with return value

```python
def add(a, b):
    return a + b

result = add(10, 25)
print(result)   # 35
```

### Default parameters

```python
def scan_ports(target, start=1, end=1024):
    print(f"Scanning {target} ports {start}–{end}")

scan_ports("192.168.1.1")              # uses defaults
scan_ports("10.0.0.1", end=100)        # override just end
scan_ports("172.16.0.1", 8000, 9000)   # override both
```

### Functions calling functions

```python
import string
import random

def generate_password(length=12):
    """Generate a random password of given length."""
    chars = string.ascii_letters + string.digits + "!@#$%"
    return "".join(random.choice(chars) for _ in range(length))

def show_passwords(count=5, length=12):
    """Print multiple generated passwords."""
    for i in range(1, count + 1):
        pwd = generate_password(length)   # calls the other function
        print(f"  #{i}: {pwd}")

show_passwords(count=3, length=16)
```

### Docstrings
Always document what your function does — your future self will thank you.

```python
def is_port_open(host, port, timeout=1):
    """
    Check if a TCP port is open on the given host.

    Args:
        host    (str): IP address or hostname
        port    (int): TCP port number
        timeout (float): seconds to wait before giving up

    Returns:
        bool: True if open, False if closed or timed out
    """
    import socket
    try:
        s = socket.socket()
        s.settimeout(timeout)
        s.connect_ex((host, port))
        s.close()
        return True
    except socket.error:
        return False
```

---

## 4. File Handling

Python can read and write files. The `with` statement is the safest way — it automatically closes the file even if an error occurs.

### Reading a file

```python
# Read the entire file as one big string
with open("targets.txt", "r") as f:
    content = f.read()
    print(content)

# Read line by line (better for large files)
with open("targets.txt", "r") as f:
    for line in f:
        ip = line.strip()   # remove newline characters
        print(f"Target: {ip}")
```

### Writing a file

```python
results = ["Port 22 - OPEN", "Port 80 - OPEN", "Port 443 - CLOSED"]

# "w" mode overwrites the file. Use "a" to append.
with open("scan-results.txt", "w") as f:
    for line in results:
        f.write(line + "\n")

print("Results saved!")
```

### Appending to a file

```python
with open("scan-results.txt", "a") as f:
    f.write("Port 3306 - OPEN\n")
```

### Checking if a file exists (avoid crashes)

```python
import os

filename = "config.txt"

if os.path.exists(filename):
    with open(filename, "r") as f:
        print(f.read())
else:
    print(f"[!] {filename} not found.")
```

### Reading a file into a list of lines

```python
with open("wordlist.txt", "r") as f:
    words = f.read().splitlines()   # splits on newlines, removes the \n

print(f"Loaded {len(words)} words")
print(words[:5])   # preview first 5
```

---

## Quick Reference

| Concept | One-liner |
|---------|-----------|
| Check type | `type(variable)` |
| Length of list/string | `len(x)` |
| Range of numbers | `range(start, stop, step)` |
| Add to list | `mylist.append(item)` |
| Dict lookup (safe) | `mydict.get(key, default)` |
| Read file safely | `with open("f", "r") as f:` |
| Write file | `with open("f", "w") as f: f.write(...)` |
| f-string | `f"Value is {variable}"` |
| Define function | `def name(params): return value` |

---

*Next up: os, sys, socket libraries — used in the port scanner and system info tools.*
