📚 Personal Library Manager (CLI App)
A simple and interactive Command Line Interface (CLI) application built using Python and Click. This tool allows you to manage your personal library by adding, removing, searching, and displaying books — all saved persistently in a library.json file.

🚀 Features
✅ Add a new book with title and author.

❌ Remove a book by its title.

🔍 Search books by title (case-insensitive).

📖 Display all books in the library.

💾 Books are stored and loaded from a JSON file (library.json) for persistent data.

🛠️ Tech Stack
Language: Python 3.x

CLI Framework: Click

Storage: JSON file (library.json)

📦 Installation
Clone the Repository

bash
Copy
Edit
git clone https://github.com/your-username/personal-library-manager.git
cd personal-library-manager
Install Dependencies

bash
Copy
Edit
pip install click
Run the App

bash
Copy
Edit
python your_script_name.py
(Replace your_script_name.py with your actual file name, e.g., library.py)

📋 Usage
Once the app is running, you'll see a menu like this:

text
Copy
Edit
📖 Welcome to your Personal Library Manager!
1. Add a book
2. Remove a book
3. Search for a book
4. Display all books
5. Exit
Enter your choice as a number (1–5) and follow the prompts.

The library data is automatically saved to library.json.

📁 File Structure
bash
Copy
Edit
├── library.py               # Main application file
├── library.json             # JSON file that stores book data
├── README.md                # Project documentation
✅ Example
bash
Copy
Edit
📖 Welcome to your Personal Library Manager!
1. Add a book
2. Remove a book
3. Search for a book
4. Display all books
5. Exit
Enter Your Choice: 1

Enter Book Title: Clean Code
Enter Book Author: Robert C. Martin
Book added: Clean Code by Robert C. Martin
💡 Future Improvements
Add support for editing book details

Add support for categories or genres

Search by author

Export/Import book list

👨‍💻 Author
Abdul Moiz
💼 Web Developer | UI/UX Designer
🔗 GitHub | LinkedIn