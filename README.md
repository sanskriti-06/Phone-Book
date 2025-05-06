# **Phone Book Management System**
## **Overview**
This project is a **simple command-line phone book** built using Python. It allows users to:
- **Add contacts** with names and phone numbers.
- **Delete contacts** from the phone book.
- **View all saved contacts**, sorted alphabetically.
- **Exit the program** when finished.

## **Features**
- Stores contacts in a **dictionary** for quick lookups.
- **Validates phone numbers** (ensures they are 10 digits long).
- **Sorted contact list** for better readability.

## **Prerequisites**
Ensure you have:
- **Python 3.x** installed.

## **Installation & Execution**
1. **Clone the repository**:
   ```sh
   git clone https://github.com/your-repo/phone-book.git
   cd phone-book
   ```
2. **Run the script**:
   ```sh
   python phone_book.py
   ```

## **How It Works**
1. Users **add, delete, or view contacts** using the menu.
2. The program ensures:
   - **No duplicate names** in the phone book.
   - **Only valid 10-digit numbers** are stored.
   - **Contacts are displayed in a sorted order**.

## **Example Output**
```
WELCOME TO OUR PHONE BOOK
Menu:
1. Add Number
2. Delete Number
3. Show All Numbers
4. Exit

Enter your choice: 1
Enter name: John
Enter number: 9876543210
Contact added!

Enter your choice: 3
1. John: 9876543210
```

## **Future Enhancements**
- Save contacts **permanently** using a file or database.
- Allow **search functionality** to find contacts easily.
- Introduce **GUI support** with Tkinter for better user experience.

## **License**
This project is open-source and free to use.
