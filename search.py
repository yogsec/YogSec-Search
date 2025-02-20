import requests
from bs4 import BeautifulSoup
import random
import time
import sys
from urllib.parse import urlparse

USER_AGENTS = [
    'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/122.0.0.0 Safari/537.36',
    'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36',
    'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv=110.0) Gecko/20100101 Firefox/110.0',
]

VERSION = "1.0"


def fetch_bing_results(query: str, max_results: int = 100) -> list:
    results = []
    seen_urls = set()
    results_per_page = 10
    max_pages = (max_results // results_per_page) + 1

    for page in range(1, max_pages + 1):
        first = (page - 1) * results_per_page + 1
        url = f"https://www.bing.com/search?q={query}&first={first}"

        headers = {
            'User-Agent': random.choice(USER_AGENTS),
            'Referer': 'https://www.bing.com/',
            'Accept-Language': 'en-US,en;q=0.9',
        }

        try:
            response = requests.get(url, headers=headers, timeout=10)

            if response.status_code != 200:
                print(f"Failed to retrieve results for page {page} (Status Code: {response.status_code})")
                continue

            soup = BeautifulSoup(response.text, 'html.parser')

            for result in soup.find_all('li', class_='b_algo'):
                title_tag = result.find('h2').find('a')
                url = title_tag['href'] if title_tag else None
                title = title_tag.get_text(strip=True) if title_tag else 'No title'

                # Skip Bing tracking URLs and duplicates
                if url and 'bing.com/ck/a' not in url and url not in seen_urls:
                    parsed_url = urlparse(url)
                    if parsed_url.netloc != 'www.bing.com':
                        seen_urls.add(url)
                        results.append({'title': title, 'url': url})

            if len(results) >= max_results:
                return results[:max_results]

            time.sleep(random.uniform(1, 3))

        except Exception as e:
            print(f"Error fetching page {page}: {e}")

    return results[:max_results]


def print_help():
    print("Usage: python search.py [OPTIONS] QUERY")
    print("Options:")
    print("  -h              Show this help message")
    print("  -v              Show version information")
    print("  -i [NUM]        Number of results to fetch (default: 100)")
    print("  -s [FILENAME]   Save output to a file")
    print("  -su [FILENAME]  Save only URLs to a file")


def print_version():
    print(f"YogSec Search v{VERSION}")


if __name__ == "__main__":
    print("\n"
          "\n"
          "卐 YogSec Search 🔍 | https://github.com/yogsec 卐"
          "\n"
          "\n")

    if '-h' in sys.argv:
        print_help()
        sys.exit(0)

    if '-v' in sys.argv:
        print_version()
        sys.exit(0)

    max_results = 100
    save_file = None
    save_urls_file = None

    if '-i' in sys.argv:
        try:
            max_results = int(sys.argv[sys.argv.index('-i') + 1])
        except (IndexError, ValueError):
            print("Invalid value for -i. Please provide a number.")
            sys.exit(1)

    if '-s' in sys.argv:
        try:
            save_file = sys.argv[sys.argv.index('-s') + 1]
        except IndexError:
            print("Invalid value for -s. Please provide a filename.")
            sys.exit(1)

    if '-su' in sys.argv:
        try:
            save_urls_file = sys.argv[sys.argv.index('-su') + 1]
        except IndexError:
            print("Invalid value for -su. Please provide a filename.")
            sys.exit(1)

    query = ' '.join(arg for arg in sys.argv[1:] if not arg.startswith('-') and arg not in [str(max_results), save_file, save_urls_file])

    if not query:
        print("Enter your search query: ", end="")
        query = input().strip()

    results = fetch_bing_results(query, max_results=max_results)

    for i, result in enumerate(results, 1):
        print(f"{i}. {result['title']} - {result['url']}")

    if save_file:
        with open(save_file, 'w') as f:
            for result in results:
                f.write(f"{result['title']} - {result['url']}\n")

    if save_urls_file:
        with open(save_urls_file, 'w') as f:
            for result in results:
                f.write(f"{result['url']}\n")
