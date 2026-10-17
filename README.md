# AI Engineer Workspace

My hands-on code from a self-study path toward becoming an AI Engineer: Python foundations first, then data, ML, LLM applications, RAG, and agents.

## Module 00: Python Foundations

- `module-00/average.py`: computes the average of a list of numbers without using `sum`, and returns `None` for an empty list.
- `module-00/word_count.py`: counts how many times each word appears in a text, using a `dict` (word → count).

## How to run

Requires Python 3.11 or newer. From the repository root:

```
python module-00/average.py
python module-00/word_count.py
```

## What I learned

- Reading a traceback from the bottom up, and the difference between a `SyntaxError` (caught before running) and runtime errors such as `ZeroDivisionError`, `KeyError` and `TypeError`.
- Variable scope: assigning to a name inside a function makes it a new local variable, which is why I got an `UnboundLocalError`.
- Using a `dict` as a key-value lookup to count items in a single pass, instead of rescanning the text.
- Working with Git and GitHub: `add`, `commit`, `push`, and writing clear commit messages.
