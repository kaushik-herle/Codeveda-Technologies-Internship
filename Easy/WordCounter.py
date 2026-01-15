def count_words_in_file(file_path):
    try:
        with open(file_path, 'r', encoding='utf-8') as file:
            content = file.read()
        
        words = content.split()
        word_count = len(words)
        
        print(f"The file '{file_path}' contains {word_count} words.")
        return word_count
    
    except FileNotFoundError:
        print(f"Error: The file '{file_path}' was not found.")
        return None
    except PermissionError:
        print(f"Error: Permission denied when trying to read '{file_path}'.")
        return None
    except IsADirectoryError:
        print(f"Error: '{file_path}' is a directory, not a file.")
        return None
    except UnicodeDecodeError:
        print(f"Error: Unable to decode the file '{file_path}' (possibly not a text file or wrong encoding).")
        return None
    except Exception as e:
        print(f"An unexpected error occurred: {e}")
        return None


if __name__ == "__main__":
    file_name = input("Enter the name of the file: ")
    count_words_in_file(file_name)
