#
# Call webservice through HTTP/HTTPS
#
import requests


def main():
    print("Hello world")

    print(
        "=== Simple HTTP GET example ==================================================================="
    )
    payload = {"key1": "value1", "key2": "value2"}
    result = requests.get("https://httpbin.org/get", params=payload)
    print(result.url)
    print(f"Status code: {result.status_code}")
    print(f"Encoding: {result.encoding}")
    print(f"Text: {result.text}")


if __name__ == "__main__":
    main()
