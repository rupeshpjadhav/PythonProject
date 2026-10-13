"""A small command-line library app for practicing Python and OOP basics."""

from abc import ABC, abstractmethod
import json
from pathlib import Path


DATA_FILE = Path(__file__).with_name("library_data.json")


class LibraryItem(ABC):
    """Abstract parent class for every item that can be borrowed."""

    def __init__(self, item_id, title):
        # Double-underscore attributes are kept inside the object.
        self.__item_id = self._clean_text(item_id, "Item ID")
        self.title = title  # Uses the title property setter for validation.
        self.__is_available = True

    @staticmethod
    def _clean_text(value, label):
        """Check that a value is non-empty text and return its trimmed form."""
        if not isinstance(value, str) or not value.strip():
            raise ValueError(f"{label} cannot be empty.")
        return value.strip()

    @property
    def item_id(self):
        """Return the item's read-only ID."""
        return self.__item_id

    @property
    def title(self):
        """Return the title without exposing the private storage directly."""
        return self.__title

    @title.setter
    def title(self, value):
        """Validate a title whenever it is created or changed."""
        self.__title = self._clean_text(value, "Title")

    @property
    def is_available(self):
        return self.__is_available

    @property
    @abstractmethod
    def item_type(self):
        """Each child class must provide its own item type."""
        raise NotImplementedError

    @property
    @abstractmethod
    def loan_period_days(self):
        """Each child class chooses its own loan period."""
        raise NotImplementedError

    @property
    @abstractmethod
    def details(self):
        """Each child class provides details specific to that item type."""
        raise NotImplementedError

    def borrow(self):
        if not self.__is_available:
            raise ValueError(f'"{self.title}" is already borrowed.')
        self.__is_available = False

    def return_to_library(self):
        if self.__is_available:
            raise ValueError(f'"{self.title}" is already available.')
        self.__is_available = True

    def to_record(self):
        """Return common item data that can be written to a JSON file."""
        return {
            "type": self.item_type,
            "item_id": self.item_id,
            "title": self.title,
            "is_available": self.is_available,
        }

    def __str__(self):
        return f"{self.title} ({self.item_type}) - {self.details}"

    def __repr__(self):
        return (
            f"{type(self).__name__}(item_id={self.item_id!r}, "
            f"title={self.title!r})"
        )

    def __eq__(self, other):
        # Overload == so two items compare by type and unique ID.
        if not isinstance(other, LibraryItem):
            return NotImplemented
        return type(self) is type(other) and self.item_id == other.item_id


class Book(LibraryItem):
    """A book has an author and a two-week loan period."""

    def __init__(self, item_id, title, author):
        super().__init__(item_id, title)
        self.author = self._clean_text(author, "Author")

    @property
    def item_type(self):
        return "book"

    @property
    def loan_period_days(self):
        return 14

    @property
    def details(self):
        return f"by {self.author}"

    def to_record(self):
        record = super().to_record()
        record["author"] = self.author
        return record


class Magazine(LibraryItem):
    """A magazine has an issue label and a one-week loan period."""

    def __init__(self, item_id, title, issue):
        super().__init__(item_id, title)
        self.issue = self._clean_text(issue, "Issue")

    @property
    def item_type(self):
        return "magazine"

    @property
    def loan_period_days(self):
        return 7

    @property
    def details(self):
        return f"issue {self.issue}"

    def to_record(self):
        record = super().to_record()
        record["issue"] = self.issue
        return record


class LibraryMember:
    """A member stores their ID, name, and borrowed item IDs."""

    def __init__(self, member_id, name):
        self.__member_id = LibraryItem._clean_text(member_id, "Member ID")
        self.__name = LibraryItem._clean_text(name, "Member name")
        self.__borrowed_item_ids = set()

    @property
    def member_id(self):
        return self.__member_id

    @property
    def name(self):
        return self.__name

    @property
    def borrowed_item_ids(self):
        # Return a tuple so callers cannot change the private set directly.
        return tuple(sorted(self.__borrowed_item_ids))

    def _record_borrow(self, item_id):
        self.__borrowed_item_ids.add(item_id)

    def _record_return(self, item_id):
        self.__borrowed_item_ids.discard(item_id)

    def to_record(self):
        return {
            "member_id": self.member_id,
            "name": self.name,
            "borrowed_item_ids": list(self.borrowed_item_ids),
        }

    def __str__(self):
        return f"{self.name} (ID: {self.member_id})"


class Library:
    """Manage items and members; save and restore them as JSON."""

    DEFAULT_NAME = "Community Library"  # A class variable shared by libraries.

    def __init__(self, name=None):
        self.name = name or self.DEFAULT_NAME
        self._items = {}
        self._members = {}

    @classmethod
    def load(cls, file_path=DATA_FILE):
        """Create a library and fill it with saved data, if a file exists."""
        library = cls()
        path = Path(file_path)
        if not path.exists():
            return library

        with path.open("r", encoding="utf-8") as data_file:
            data = json.load(data_file)

        for record in data.get("items", []):
            item_type = record.get("type")
            if item_type == "book":
                item = Book(
                    record["item_id"], record["title"], record["author"]
                )
            elif item_type == "magazine":
                item = Magazine(
                    record["item_id"], record["title"], record["issue"]
                )
            else:
                raise ValueError(f"Unknown item type: {item_type}")

            if not record.get("is_available", True):
                item.borrow()
            library.add_item(item)

        for record in data.get("members", []):
            member = LibraryMember(record["member_id"], record["name"])
            library.register_member(member)
            for item_id in record.get("borrowed_item_ids", []):
                member._record_borrow(item_id)

        return library

    @staticmethod
    def normalize_text(value):
        """Make searches ignore letter case and surrounding spaces."""
        return value.strip().casefold()

    @property
    def members(self):
        return tuple(self._members.values())

    def add_item(self, item):
        if not isinstance(item, LibraryItem):
            raise TypeError("Only LibraryItem objects can be added.")
        if item.item_id in self._items:
            raise ValueError(f"Item ID {item.item_id} is already in use.")
        self._items[item.item_id] = item

    def register_member(self, member):
        if not isinstance(member, LibraryMember):
            raise TypeError("Expected a LibraryMember object.")
        if member.member_id in self._members:
            raise ValueError(
                f"Member ID {member.member_id} is already in use."
            )
        self._members[member.member_id] = member

    def borrow_item(self, item_id, member_id):
        item = self[item_id]
        try:
            member = self._members[member_id]
        except KeyError as error:
            raise KeyError(f"No member with ID {member_id}.") from error

        item.borrow()
        member._record_borrow(item_id)
        return item

    def return_item(self, item_id, member_id):
        item = self[item_id]
        try:
            member = self._members[member_id]
        except KeyError as error:
            raise KeyError(f"No member with ID {member_id}.") from error

        if item_id not in member.borrowed_item_ids:
            raise ValueError("This member did not borrow that item.")
        item.return_to_library()
        member._record_return(item_id)
        return item

    def search(self, query):
        search_text = self.normalize_text(query)
        if not search_text:
            return []
        return [
            item
            for item in self
            if search_text in self.normalize_text(
                f"{item.title} {item.details}"
            )
        ]

    def save(self, file_path=DATA_FILE):
        """Save all items and members to a human-readable JSON file."""
        data = {
            "items": [item.to_record() for item in self],
            "members": [member.to_record() for member in self.members],
        }
        path = Path(file_path)
        with path.open("w", encoding="utf-8") as data_file:
            json.dump(data, data_file, indent=2)

    def __len__(self):
        return len(self._items)

    def __iter__(self):
        return iter(self._items.values())

    def __contains__(self, item_id):
        return item_id in self._items

    def __getitem__(self, item_id):
        try:
            return self._items[item_id]
        except KeyError as error:
            raise KeyError(f"No item with ID {item_id}.") from error

    def __str__(self):
        return f"{self.name}: {len(self)} item(s)"


def display_menu():
    """Print the available actions."""
    print("\n1. List items")
    print("2. Add a book")
    print("3. Add a magazine")
    print("4. Register a member")
    print("5. Borrow an item")
    print("6. Return an item")
    print("7. Search items")
    print("8. List members")
    print("0. Save and exit")


def ask_for_text(prompt):
    """Read and validate one non-empty text value from the user."""
    value = input(prompt).strip()
    if not value:
        raise ValueError("Please enter a value; it cannot be empty.")
    return value


def list_items(library):
    if not library:
        print("The library has no items yet.")
        return

    for item in library:
        status = "Available" if item.is_available else "Borrowed"
        print(f"{item} | ID: {item.item_id} | {status}")


def main(storage_path=DATA_FILE):
    """Run the text-menu app. Pass a path to choose where JSON is stored."""
    try:
        library = Library.load(storage_path)
    except (OSError, ValueError, KeyError, TypeError) as error:
        print(f"Could not load saved library data: {error}")
        return

    print(f"Welcome to {library.name}!")
    while True:
        display_menu()
        choice = input("Choose an option: ").strip()

        try:
            if choice == "1":
                list_items(library)
            elif choice == "2":
                item = Book(
                    ask_for_text("Item ID: "),
                    ask_for_text("Book title: "),
                    ask_for_text("Author: "),
                )
                library.add_item(item)
                print("Book added.")
            elif choice == "3":
                item = Magazine(
                    ask_for_text("Item ID: "),
                    ask_for_text("Magazine title: "),
                    ask_for_text("Issue: "),
                )
                library.add_item(item)
                print("Magazine added.")
            elif choice == "4":
                member = LibraryMember(
                    ask_for_text("Member ID: "),
                    ask_for_text("Member name: "),
                )
                library.register_member(member)
                print("Member registered.")
            elif choice == "5":
                item = library.borrow_item(
                    ask_for_text("Item ID: "),
                    ask_for_text("Member ID: "),
                )
                print(
                    f'"{item.title}" borrowed for '
                    f"{item.loan_period_days} days."
                )
            elif choice == "6":
                item = library.return_item(
                    ask_for_text("Item ID: "),
                    ask_for_text("Member ID: "),
                )
                print(f'"{item.title}" returned.')
            elif choice == "7":
                results = library.search(ask_for_text("Search for: "))
                if results:
                    for item in results:
                        print(item)
                else:
                    print("No matching items found.")
            elif choice == "8":
                if library.members:
                    for member in library.members:
                        print(
                            f"{member} | Borrowed items: "
                            f"{len(member.borrowed_item_ids)}"
                        )
                else:
                    print("There are no registered members yet.")
            elif choice == "0":
                library.save(storage_path)
                print(f"Saved {library} to {storage_path}.")
                break
            else:
                print("Choose one of the listed options.")
        except (ValueError, KeyError, TypeError, OSError) as error:
            # Handle invalid input and expected app errors without a crash.
            print("Error:", error)


if __name__ == "__main__":
    main()
