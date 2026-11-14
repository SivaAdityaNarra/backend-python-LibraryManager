# main.py
from models import Book, Magazine, DVD, Member

book = Book("Python 101", 1, "A. Rao")
magazine = Magazine("Tech Today", 2, 42)
dvd = DVD("Inception", 3, 148)

alice = Member("Alice", 101)
bob = Member("Bob", 102, max_items=1)

# 1. Borrowing with error handling
try:
    alice.borrow(book)
    print("Alice borrowed:", book.describe())
    bob.borrow(book)  # should fail: already borrowed
except ValueError as e:
    print("Could not borrow:", e)

# 2. Trigger the borrow-limit error and the not-borrowed error, catching each
try:
    bob.borrow(magazine)
    print("Bob borrowed:", magazine.describe())
    bob.borrow(dvd)  # should fail: Bob's limit is 1
except ValueError as e:
    print("Could not borrow:", e)

try:
    bob.return_item(dvd)  # should fail: Bob never borrowed the DVD
except ValueError as e:
    print("Could not return:", e)

try:
    fee = alice.return_item(book, days_late=3)
    print("Alice returned", book.title, "- late fee: Rs", fee)
except ValueError as e:
    print("Could not return:", e)

print("Bob's borrowed titles:", bob.borrowed_titles())

# 3. Polymorphism: one loop, no type checks
items = [book, magazine, dvd]
for item in items:
    print(item.describe(), "-> late fee for 3 days: Rs", item.late_fee(3))

# 4. Class attribute shared by all objects
print("Total items created:", Book.total_items)

# 5. Encapsulation
try:
    print(dvd.__available)
except AttributeError as e:
    print("AttributeError:", e)
print("DVD available?", dvd.is_available())

# Abstract class check
try:
    from models import LibraryItem
    LibraryItem("x", 1)
except TypeError as e:
    print("TypeError:", e)
