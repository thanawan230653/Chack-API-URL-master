import requests
import json
import argparse
import sys

def parse_headers(header_list):
    headers = {}
    if header_list:
        for item in header_list:
            try:
                key, value = item.split(":", 1)
                headers[key.strip()] = value.strip()
            except ValueError:
                print(f"[!] Invalid header format: {item}")
                sys.exit(1)
    return headers

def fetch_api(url, headers=None, timeout=10, proxy=None, save_file=None):
    try:
        proxies = {"http": proxy, "https": proxy} if proxy else None

        response = requests.get(
            url,
            headers=headers,
            timeout=timeout,
            proxies=proxies
        )

        response.raise_for_status()

        try:
            data = response.json()
            formatted = json.dumps(data, indent=4, ensure_ascii=False)
            print("\n===== JSON RESPONSE =====\n")
            print(formatted)
        except ValueError:
            formatted = response.text
            print("\n===== RAW RESPONSE =====\n")
            print(formatted)

        if save_file:
            with open(save_file, "w", encoding="utf-8") as f:
                f.write(formatted)
            print(f"\n[+] Response saved to {save_file}")

    except requests.exceptions.RequestException as e:
        print(f"\n[ERROR] {e}")

def main():
    parser = argparse.ArgumentParser(description="Simple API Fetcher Tool")

    parser.add_argument("url", nargs="?", help="API URL")
    parser.add_argument("--header", action="append", help="Custom header (Key: Value)")
    parser.add_argument("--timeout", type=int, default=10, help="Request timeout (seconds)")
    parser.add_argument("--proxy", help="Proxy URL (e.g. http://127.0.0.1:8080)")
    parser.add_argument("--save", help="Save response to file")

    args = parser.parse_args()

    if not args.url:
        args.url = input("Enter API URL: ").strip()

    headers = parse_headers(args.header)

    fetch_api(
        url=args.url,
        headers=headers,
        timeout=args.timeout,
        proxy=args.proxy,
        save_file=args.save
    )

if __name__ == "__main__":
    main()
