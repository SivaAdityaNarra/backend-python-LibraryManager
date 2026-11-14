# backend-python-LibraryManager
Backend Python Library Manager Assignment

Run with `python3 main.py` (on Windows: `python main.py`). Console output of the final run is in `output.txt`.

## Reflection

**1. Why is LibraryItem abstract, and what happens if DVD forgets to write late_fee()?**
`LibraryItem` is only a general idea of an item, so it should never be created directly; it exists to define what every item must have. Marking `late_fee()` with `@abstractmethod` forces every child class to provide its own version. If `DVD` forgot to write `late_fee()`, Python would raise a `TypeError` as soon as we tried to create a `DVD` object.

**2. What happens when you read item.__available from outside the class, and why do we use is_available() instead?**
Reading `item.__available` from outside raises an `AttributeError`, because Python name-mangles double-underscore attributes to `_LibraryItem__available`. This protects the internal state so outside code cannot read or change it carelessly. `is_available()` is the public, controlled way to read the value, and only `mark_borrowed()` / `mark_returned()` can change it.

**3. What is the difference between LibraryItem.total_items and self.title?**
`LibraryItem.total_items` is a class attribute: there is one shared copy for the whole class, so it counts every item created. `self.title` is an instance attribute: each object has its own separate value. Changing one book's title does not affect any other item, but `total_items` is the same for all of them.
