# Write and Append Data to a File

## 📌 Project Description
This Python program demonstrates how to write data into a file and append additional data without deleting the existing content.

## 🎯 Objective
- To learn file handling in Python.
- To write data into a text file.
- To append new data to an existing file.
- To understand file modes (`w` and `a`).

## 🛠️ Technologies Used
- Python
- File Handling
- VS Code

## 💻 Source Code
```python
# Write data to a file
with open("data.txt", "w") as file:
    file.write("Hello, World!\n")

# Append data to the file
with open("data.txt", "a") as file:
    file.write("This is appended data.\n")

print("Data written and appended successfully!")
```

## ▶️ Output
```text
Data written and appended successfully!
```

## 📂 Project Files
- `main.py` – Python source code.
- `README.md` – Project documentation.
- `data.txt` – Output text file (created when the program runs).

## 📝 Conclusion
This project helps us understand Python file handling, especially how to write and append data to a text file.

## 👨‍🎓 Student Information
- **Name:** Jariab Noor Salam
- **Roll:** 356537
- **Department:** Computer Technology
- **Semester:** 3rd
- **Institute:** National Institute of Technology
