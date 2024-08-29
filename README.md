# Non-AI-Based Plagiarism Detection Script

This script checks for potential plagiarism in code repositories by searching for similar code snippets across GitHub without relying on AI-based approaches. It uses the GitHub API to find matches.

## Features

- Supports multiple programming languages.
- Searches GitHub for code snippets without needing a reference repository.
- Provides clear results indicating whether a match is found.
- Customizable snippet length for searching.

## Prerequisites

- **Python 3.6+**
- **GitHub Personal Access Token**: Required to access the GitHub API.
- **Python Libraries**: `requests`

## Installation

1. **Clone this repository** to your local machine:
    ```bash
    git clone https://github.com/yourusername/your-repo.git
    cd your-repo
    ```

2. **Install required Python libraries**:
    ```bash
    pip install requests
    ```

## Usage

1. **Run the script**:
    ```bash
    python script.py
    ```

2. **Provide the following inputs when prompted**:
    - **GitHub Personal Access Token**: Create one [here](https://github.com/settings/tokens).
    - **Repository Path**: Local path of the repository you want to check.
    - **Number of Lines to Check**: The number of lines to include in each snippet search (recommended: 5-20).

3. **Review the Output**:
    - The script will print "Match found" along with the URLs of the repositories where similar code is detected.
    - If no match is found, it will print "Match not found."

## Example Output

```plaintext
Enter your GitHub Personal Access Token: ghp_exampleToken123456789
Enter the path of the repository to check: /path/to/your/repository
Enter the number of lines to search for plagiarism (suggested: 5-20): 10

Match found for /path/to/your/repository/main.py:
- https://github.com/someuser/somerepo/blob/main/src/main.py

Match not found for snippet from /path/to/your/repository/sample.c
Match not found in any file.
