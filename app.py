import requests

def fetch_data():
    url = "https://example.com"
    response = request.get(url)
    print("Response status:", response.status_code)

if __name__ == "__main__":
    fetch_data()
