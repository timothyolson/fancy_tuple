# Fancy Tuple
Python class that creates a tuple from a list of items and adds each item as a method, raises attribute error when item not found and provides length of tuple.
Script is based on a HackerRank challenge with the following requirements:

- Constructor must take a maximum of five parameters `FancyTuple("item1".."item5")
`
- Constructor must contain methods to access items *e.g.* `FancyTuple("dog","cat").second` must be equal to `2`.
- `len(FancyTuple("cat","dog"))` must return the number of items passed, in this example `2`.
- AttributeErrors are raised if attribute does not exist.