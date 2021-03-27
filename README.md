## Run

### Activate venv
- `sudo apt-get install python3-venv`
- `python3 -m venv .venv`
- `source .venv/bin/activate`

### Test
- `python -m unittest discover`

### Execute
- `python solutions.py`
- **Sample**
```bash
Type 1 or 2 or 3 to execute solution and 0 to exit: 1
key1 1
key2 1
key3 2
key4 2
key5 3

Type 1 or 2 or 3 to execute solution and 0 to exit: 2
key1 1
key2 1
key3 2
key4 2
key5 3
user 3
first_name 4
last_name 4
father 4
first_name 5
last_name 5
father 5

Type 1 or 2 or 3 to execute solution and 0 to exit: 3
lca of 6 7: 3
lca of 3 7: 3

Type 1 or 2 or 3 to execute solution and 0 to exit: 0
```

## Runtime and Memory requirements

1. **Problem One**
   - Runtime
     - O(n) where n is the number of nodes.
   - Memory
     - O(log(n)) since each recursive call creating new variable of depth.
     - I declare results to store result which is not neccessary. It added for test purpose.

2. **Problem Two**
    - Runtime and Memory complexity as same as **Problem One**
3. **Problem Three**
   - Runtime
     - O(log(n)) Where n is the number of nodes.
     - To mark nodes for the first value we are traversing tail to root which take at most log(n).
     - And to find first marked node again we traversing tail to root which take at most log(n)
     - In Big O we can eliminate content value O(2 * log(n)) => O(log(n))
   - Memory
     - O(log(n)) since we store all child values for the first node.

