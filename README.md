# Benchy

Benchy is a lightweight Python utility designed to help you measure the execution time of your functions easily. It provides two main features:

- **@timer Decorator:** A decorator that prints the execution time of any function it decorates.
- **measure_time Function:** A helper function that executes any function and returns a tuple containing the function’s return value and the elapsed time in seconds.

## Features

- **@timer Decorator:**  
  Simply add `@timer` above your function definition to automatically print its execution time whenever it is called.
  
- **measure_time Function:**  
  Use `measure_time(func, *args, **kwargs)` to execute any function and get both its return value and the time it took to run, which is especially useful for programmatically capturing performance data.

## Installation

### Clone the Repository
Clone the repository using Git:

```bash
git clone https://github.com/jessegresock/benchy.git
cd benchy
```
### Install the Module
Install Benchy using the provided setup.py. For development, you can install it in editable mode:

```bash
pip install .
```
## Usage
### Using the @timer Decorator
Import the timer decorator from benchy.decorators and apply it to any function:
```python
from benchy.decorators import timer

@timer
def compute_heavy_task(n):
    total = sum(i * i for i in range(n))
    return total

# When called, compute_heavy_task will print its execution time.
result = compute_heavy_task(1000000)
```

### Using the measure_time Function
Import the measure_time function from benchy.functions to time a function call and capture its output along with the execution time:
```python
from benchy.functions import measure_time

def compute_heavy_task(n):
    total = sum(i * i for i in range(n))
    return total

result, elapsed = measure_time(compute_heavy_task, 1000000)
print(f"Result: {result}, Time taken: {elapsed:.4f} seconds")
```
## Contributing
Contributions are welcome! Feel free to fork the repository, make changes, and submit pull requests if you have ideas for improvements or additional features.