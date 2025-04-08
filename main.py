import click
import json
import os

library_file = 'library.json'
library = []

def load_library():
    global library
    if os.path.exists(library_file):
        with open(library_file,'r') as f:
            library = json.load(f)

def save_library():
    with open(library_file,'w') as f:
        json.dump(library,f)

@click.command()
def add():
    """Add a new book"""
    title = click.prompt("Enter Book Title")
    author = click.prompt("Enter Book Author")
    library.append({"title": title, "author": author})
    save_library()  # Save the library after adding a book
    click.echo(f"Book added: {title} by {author}")


@click.command()
def remove():
    """Remove Your Existing Book"""
    title = click.prompt("Enter the Title of the Book to Remove")
    for book in library:
        if book['title'].lower() == title.lower():
            library.remove(book)
            save_library()  # Save the library after removing a book
            click.echo(f"❌ Book removed: {title}")
            return
    click.echo(f"❌ {title} Book not Found")

@click.command()
def search():
    """Search Your Book"""
    title = click.prompt("Enter Title to search")
    for book in library:
        if title.lower() in book["title"].lower():
            click.echo(f"Found: {book['title']} by {book['author']}")
            return
    click.echo("❌ No matching Book Found")

@click.command()
def display():
    """Display all books"""
    if not library:
        click.echo("📚 No books in the library.")
    else:
        click.echo("📚 Your Library:")
        for book in library:
            click.echo(f"{book['title']} by {book['author']}")

@click.command()
def main():
    load_library()  # Load the library at the start
    while True:
        click.echo("\n📖 Welcome to your Personal Library Manager!")
        click.echo("1. Add a book")
        click.echo("2. Remove a book")
        click.echo("3. Search for a book")
        click.echo("4. Display all books")
        click.echo("5. Exit")
        choice = click.prompt("Enter Your Choice", type=int)

        if choice == 1:
            add()
        elif choice == 2:
            remove()
        elif choice == 3:
            search()
        elif choice == 4:
            display()
        elif choice == 5:
            click.echo("Exiting the library manager. Goodbye!")
            break
        else:
            click.echo("❌ Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
