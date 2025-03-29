# GitHub Events Tracker

A simple Python script that fetches and displays recent events of a GitHub user. It provides details about various activities such as push events, pull requests, issues, forks, and more.

## Features
- Fetches recent public events of a GitHub user.
- Displays event type, repository name, and timestamp.
- Supports event-specific details (e.g., number of commits in a push event).
- Handles GitHub API rate limiting automatically.
- Uses ANSI colors for better readability in the terminal.

## Prerequisites
- Python 3.x
- `requests` library

## Installation
1. Clone the repository or download the script:
   ```sh
   git clone https://github.com/your-repo/github-events-tracker.git
   cd github-events-tracker
   ```
2. Install dependencies:
   ```sh
   pip install requests
   ```

## Usage
Run the script and enter a GitHub username when prompted:
```sh
python script.py
```

## Event Types Handled
- **PushEvent** 🚀 - Displays number of commits.
- **PullRequestEvent** 🔗 - Shows pull request actions.
- **IssuesEvent** 🐛 - Displays issue-related actions.
- **ForkEvent** 🍴 - Indicates repository forking.
- **WatchEvent** 👀 - Shows repository watching.
- **CreateEvent** ➕ - Shows creation events.
- **DeleteEvent** 🗑️ - Shows deletion events.
- **Other Events** ❓ - Displays unclassified event types.

## Handling Rate Limiting
The script checks the `X-RateLimit-Remaining` header from the GitHub API. If the rate limit is exceeded, it waits until reset before continuing.

## License
This project is open-source and available under the [MIT License](LICENSE).

## Author
[Your Name]  
GitHub: [your-github-profile](https://github.com/your-github-profile)

### Roadmap.sh Project URL:
```
https://roadmap.sh/projects/github-user-activity
```

