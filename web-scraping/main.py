import re
import requests

URL = "https://books.toscrape.com/"

def get_data():
    """
    Fetches book URLs from the website and organizes them.

    Returns:
        list[str]: List of book identifiers.
    """
    try:
        response = requests.get(URL, timeout=10)
        response.raise_for_status()  
    except requests.exceptions.RequestException as e:
        print(f"Error during the web request: {e}")
        return []
    
    pattern = r"catalogue/[\w-]+_\d+/index.html"
    books = re.findall(pattern, response.text)

    final_result = sorted({
        book.replace("catalogue/", "").replace("/index.html", "")
        for book in books
    })

    return final_result

def save_data_to_txt(data, filename="data.txt"):
    """
    Writes the list of books to a text file.

    Args:
        data (list[str]): List of book identifiers.
        filename (str): Output file name.

    Returns:
        str: Status message.
    """
    if not data:
        return "No data to save."

    try:
        with open(filename, "w") as file:
            for count, book in enumerate(data, start=1):
                file.write(f"{count}- {book}\n")
        return f"Data has been written to {filename}."
    except Exception as e:
        return f"Error writing to file: {e}"


if __name__ == "__main__":
    data = get_data()
    message = save_data_to_txt(data)
    print(message)
