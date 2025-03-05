# YogSec Search

## Overview
YogSec Search is a powerful and flexible search tool designed to fetch search results from Bing. It is specifically built for security researchers, digital investigators, and developers who need to gather URLs and website information efficiently. 

![YogSec Search](https://github.com/yogsec/YogSec-Search/blob/main/Screenshot%20from%202025-03-05%2013-30-09.png?raw=true)

## Problem
Performing manual searches through search engines is time-consuming and often returns unwanted URLs like tracking links from search platforms (e.g., `bing.com/ck/a`). Additionally, users may face duplicate results or may require a larger number of results, which is not easily accessible through a standard search.

## Solution
YogSec Search automates the process of querying Bing and filters out unwanted results like Bing tracking URLs. It ensures that only unique and relevant URLs are returned, streamlining your search process and saving time.

## Key Features
- Fetches search results from Bing.
- Removes unwanted tracking URLs from Bing (e.g., `bing.com/ck/a`).
- Ensures no duplicate URLs in the output.
- Fetches up to **200 search results** using the `-i` parameter.
- Saves the complete output with titles and URLs to a file.
- Saves only URLs to a separate file.
- Displays help and version information.
- Customizable user agent for better evasion.

## Installation
### Prerequisites
Ensure you have **Python 3.x** installed on your system.

### Installation Steps
1. Clone the repository:
    ```bash
    git clone https://github.com/YogSec/YogSec-Search.git
    ```
2. Navigate to the directory:
    ```bash
    cd YogSec-Search
    ```
3. Install dependencies (if needed):
    ```bash
    pip install bs4
    ```

## Usage
Run the script using the command line:

```bash
python script.py [OPTIONS] QUERY
```

### Options:
| Option        | Description                                          |
|---------------|------------------------------------------------------|
| `-h`          | Show help message.                                   |
| `-v`          | Show version information.                            |
| `-i [NUM]`    | Number of results to fetch (default: 100, max: 200). |
| `-s [FILENAME]` | Save output (title + URL) to a file.              |
| `-su [FILENAME]` | Save only URLs to a file.                        |

### Examples:
#### 1. Basic Search
```bash
python script.py "site:example.com"
```
#### 2. Fetch 200 Results
```bash
python script.py -i 200 "site:example.com"
```
#### 3. Save Output to a File
```bash
python script.py -s results.txt "site:example.com"
```
#### 4. Save Only URLs to a File
```bash
python script.py -su urls.txt "site:example.com"
```
#### 5. Combine Options
```bash
python script.py -i 200 -s results.txt -su urls.txt "site:example.com"
```

## How It Works
1. Sends search queries to **Bing**.
2. Parses the search result HTML using **BeautifulSoup**.
3. Filters out unwanted Bing tracking URLs like `bing.com/ck/a`.
4. Removes duplicate URLs from the output.
5. Outputs the results to the terminal or saves them to a file if specified.

## Customization
- User agents can be modified in the `USER_AGENTS` list to rotate between different browsers.

## Dependencies
- `requests`
- `BeautifulSoup4`

You can install these packages using:
```bash
pip install requests beautifulsoup4
```

## Version
Current Version: **1.0**

## License
This project is licensed under the MIT License.

## Author
Developed by **Abhinav Singwal** | YogSec

## 🌟 Let's Connect!

Hello, Hacker! 👋 We'd love to stay connected with you. Reach out to us on any of these platforms and let's build something amazing together:

🌐 **Website:** [https://yogsec.github.io/yogsec/](https://yogsec.github.io/yogsec/)  
📜 **Linktree:** [https://linktr.ee/yogsec](https://linktr.ee/yogsec)  
🔗 **GitHub:** [https://github.com/yogsec](https://github.com/yogsec)  
💼 **LinkedIn (Company):** [https://www.linkedin.com/company/yogsec/](https://www.linkedin.com/company/yogsec/)  
📷 **Instagram:** [https://www.instagram.com/yogsec.io/](https://www.instagram.com/yogsec.io/)  
🐦 **Twitter (X):** [https://x.com/yogsec](https://x.com/yogsec)  
👨‍💼 **Personal LinkedIn:** [https://www.linkedin.com/in/cybersecurity-pentester/](https://www.linkedin.com/in/cybersecurity-pentester/)  
📧 **Email:** abhinavsingwal@gmail.com

## ☕ Buy Me a Coffee

If you find our work helpful and would like to support us, consider buying us a coffee. Your support keeps us motivated and helps us create more awesome content. ❤️

☕ **Support Us Here:** [https://buymeacoffee.com/yogsec](https://buymeacoffee.com/yogsec)
