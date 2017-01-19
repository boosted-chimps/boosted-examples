# Homework 1

## Clone the boosted-examples project

You've probably already cloned this repository since we walked through
cloning and committing to the project. If you haven't cloned the
project, you can clone it by running:

```
eval "$(ssh-agent -s)"
ssh-add
cd ~
git clone git@github.com:boosted-chimps/boosted-examples.git
```

Cloning the repository will create a `boosted-examples` directory
within your home directory.

Move into `boosted-examples/homework/`. There is a github component to
the homework so we'll start working in this directory.

```
cd boosted-examples/homework/
```

## Assignment

1. Create a directory for yourself (e.g. `abutcher`) within `~/boosted-examples/homework`.

2. Within directory you just created, create a `homework1.py` file which will contain your work (e.g. `~/boosted-examples/homework/abutcher/homework1.py`).

3. Edit `homework1.py` and write the following functions:

Create a function which, given a string, will return `True` if the
string is a palindrome. The function must return `False` if the
provided string is not a palindrome. A palindrome is a word or
phrase that reads the same backward as forward such as `"racecar"`.
This function must ignore spaces in the string such that a phrase
like `"are we not drawn onward to new era"` will be recognized as a
palindrome.

Create a function that accepts a list of strings and prints out
which strings are palindromes (using the palindrome function).

```python
>>> palindromes(["racecar", "are we not drawn onward to new era", "malathar"])
racecar is a palindrome
are we not drawn onward to new era is a palindrome
```

4. Commit your `homework1.py` file using git and push your new file to github.
