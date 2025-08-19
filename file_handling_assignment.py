def file_read_write():
    try:
        # Ask user for filename
        filename = input("Enter the filename to read: ")

        # Try opening the file
        with open(filename, "r") as file:
            content = file.read()

        # Modify the content (example: make all text uppercase)
        modified_content = content.upper()

        # Write to a new file
        new_filename = "modified_" + filename
        with open(new_filename, "w") as new_file:
            new_file.write(modified_content)

        print(f"✅ File has been modified and saved as '{new_filename}'.")

    except FileNotFoundError:
        print("❌ Error: The file does not exist.")
    except PermissionError:
        print("❌ Error: You don’t have permission to read this file.")
    except Exception as e:
        print(f"⚠️ An unexpected error occurred: {e}")


# Run the function
if __name__ == "__main__":
    file_read_write()
