<h1 align="center">
    <a>Generic Library</a>
</h1>
<p align="center"><small>Intended to create generic libraries which can facilitate boilerplate codes and functionalities with easy integrations with Python applications.</small></p>

<div align="center">
<br />
</div>

<details open="open">
<summary>Table of Contents</summary>

- [About](#about)
  - [Libraries](#libraries)
  - [Getting Started with progress_tracker](#getting-started)
    - [Input Parameters](#input-parameters)
    - [Usage](#usage)
      - [Outputs](#Outputs)

</details>

# About
Motivated from `functools` and `threading` in python

## Libraries
* progress_tracker

## Getting Started 
#### with `progress_tracker`
Library which tracks the progress of any long-running task (function) in Python program (best fit for Machine learning Model trainings).

Progress-tracker spawns a thread in the backend and monitors the progress of any user-defined function. 

## Input Parameters
`tracker` decorator takes two arguments.

* `max_timeout: int` <small>[Optional]</small> It's the time in seconds after which the progress tracker thread automatically times out. Set this value wisely, depends on how much time your function takes generally. Placing a higher timeout value is advisable if you're not sure about the usual run time of your function. **By default, this value is set to 18000 seconds (5 hour)**. However, it gets terminated along with your function, whichever time is lesser.
* `log_interval: int` <small>[Optional]</small> Pace at which progress will be logged. It's measured in seconds. **By default, it is set at 2 seconds interval**.


## Usage

```python
from generic_libs import Progress

prg = Progress()


@prg.tracker(max_timeout=20, log_interval=2)
def example():
  print("Function Started")
  # ...
  # some useful long running tasks
  return 0  # optional


# Invoke your function
example()
```

### Outputs
* When `max_timeout` is set a lower value than the user-defined function's execution time.

```python
import time
import datetime
from generic_libs import Progress

prg = Progress()


@prg.tracker(max_timeout=5, log_interval=2)
def example():
  print(f"Function Started at {datetime.datetime.now().__str__()[11:]}")
  # ...
  time.sleep(10)  # some useful long running tasks
  print(f"Function completed at {datetime.datetime.now().__str__()[11:]}")


# Invoke your function
example()
```
```
[example._is_running] - #
Function Started at 15:26:23.423851
[example._is_running] - ##
[tracker.is_terminated] - Progress Tracker Timed out! example is still running...
Function completed at 15:26:33.423860
```
* When `max_timeout` is set a larger value than the user-defined function's execution time.

```python
import time
import datetime
from generic_libs import Progress

prg = Progress()


@prg.tracker(max_timeout=50, log_interval=2)
def example():
  print(f"Function Started at {datetime.datetime.now().__str__()[11:]}")
  # ...
  time.sleep(10)  # some useful long running tasks
  print(f"Function completed at {datetime.datetime.now().__str__()[11:]}")


# Invoke your function
example()
```
```
[example._is_running] - #
Function Started at 15:30:47.848753
[example._is_running] - ##
[example._is_running] - ###
[example._is_running] - ####
[example._is_running] - #####
Function completed at 15:30:57.849750
[example._is_done] - #####!
```