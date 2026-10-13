# Library Management Mini-Project

A beginner-friendly command-line app for practicing Python fundamentals and
object-oriented programming. It uses only the Python standard library.

## Run it

From the repository root, run:

```text
python3 PythonPractice/MiniProject/library_management.py
```

Choose a menu number and follow the prompts. Add books or magazines, register
members, borrow and return items, search the catalog, and save before exiting.
The app writes its saved data to `library_data.json` in this folder. The file is
created the first time you choose **Save and exit**.

## OOP concepts in the project

- **Classes and objects:** `Book`, `Magazine`, `LibraryMember`, and `Library`.
- **Encapsulation:** IDs, titles, availability, and borrowed-item IDs are held
  inside objects. Properties provide controlled access and validate titles.
- **Abstraction:** `LibraryItem` is an abstract base class. It requires each
  child class to provide its type, details, and loan period.
- **Inheritance:** `Book` and `Magazine` inherit shared behavior from
  `LibraryItem`.
- **Polymorphism:** the library treats both child types as `LibraryItem`
  objects; each supplies its own details and loan period.
- **Instance methods:** borrow, return, search, and other object behavior.
- **Class method:** `Library.load()` creates a library from saved JSON data.
- **Static method:** `Library.normalize_text()` cleans text for searching.
- **Properties:** `LibraryItem.title` validates values when a title is changed.
- **Dunder methods / operator overloading:** `__str__`, `__repr__`, `__eq__`,
  `__len__`, `__iter__`, `__contains__`, and `__getitem__` support readable
  display, `==`, `len(library)`, loops, `in`, and `library[item_id]`.
- **Composition:** a `Library` contains items and members.

## Python basics in the project

- Variables and common data types: text, numbers, booleans, lists, tuples,
  sets, and dictionaries.
- Functions, arguments, return values, and f-strings.
- `if` / `elif` / `else` decisions and a `while` loop for the menu.
- `for` loops for displaying and searching items.
- Comparisons and boolean conditions.
- Input validation and exception handling with `try` / `except`.
- File handling and JSON serialization for saving and loading data.
- Imports, modules, and the `if __name__ == "__main__"` entry point.

## Try this example

1. Choose **2** and enter book ID `B101`, title `Python Basics`, and author
   `Alex Writer`.
2. Choose **4** and register member ID `M101` with name `Sam`.
3. Choose **5** and enter item ID `B101` and member ID `M101`.
4. Choose **1** to see that the book is borrowed.
5. Choose **0** to save and exit. Run the app again to see the saved data load.
