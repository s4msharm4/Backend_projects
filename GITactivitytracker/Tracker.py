import requests
import json
import time

def get_github_username():
    """Prompts the user to enter a GitHub username."""
    username = input("Enter the GitHub username: ").strip()
    if not username:
        print("Username cannot be empty.")
        exit()
    return username

def get_github_events(username):
    """Retrieves the user's recent events from the GitHub API."""
    try:
        respo = requests.get(f'https://api.github.com/users/{username}/events')
        respo.raise_for_status()  # Raise HTTPError for bad responses (4xx or 5xx)
        return respo.json(), respo.headers
    except requests.exceptions.RequestException as e:
        print(f"Error: {e}")
        exit()

def process_events(jsondata):
    """Processes the events and prints a summary of each event."""
    i = 1
    for event in jsondata:
        event_type = event['type']
        repo_name = event['repo']['name']
        event_time = event['created_at']
        print_event(i, event_type, repo_name, event_time, event)  # Pass the entire event
        i += 1

def print_event(i, event_type, repo_name, event_time, event_data=None):
    """Prints a formatted message for the given event with color and icons."""
    # ANSI color codes
    GREEN = '\033[92m'
    YELLOW = '\033[93m'
    BLUE = '\033[94m'
    RED = '\033[91m'
    RESET = '\033[0m'

    if event_type == 'PushEvent':
        num_commits = len(event_data['payload']['commits']) if event_data and 'payload' in event_data and 'commits' in event_data['payload'] else 0
        print(f"{BLUE}{i}-> 🚀 Push{RESET} to {GREEN}{repo_name}{RESET} with {YELLOW}{num_commits}{RESET} commits at {YELLOW}{event_time[:10]}{RESET}")
    elif event_type == 'PullRequestEvent':
        action = event_data['payload']['action'] if event_data and 'payload' in event_data and 'action' in event_data['payload'] else 'unknown'
        print(f"{BLUE}{i}-> 🔗 Pull Request {action}{RESET} in {GREEN}{repo_name}{RESET} at {YELLOW}{event_time[:10]}{RESET}")
    elif event_type == 'IssuesEvent':
        action = event_data['payload']['action'] if event_data and 'payload' in event_data and 'action' in event_data['payload'] else 'unknown'
        print(f"{BLUE}{i}-> 🐛 Issue {action}{RESET} in {GREEN}{repo_name}{RESET} at {YELLOW}{event_time[:10]}{RESET}")
    elif event_type == 'ForkEvent':
        print(f"{BLUE}{i}-> 🍴 Forked{RESET} {GREEN}{repo_name}{RESET} at {YELLOW}{event_time[:10]}{RESET}")
    elif event_type == 'WatchEvent':
        print(f"{BLUE}{i}-> 👀 Watched{RESET} {GREEN}{repo_name}{RESET} at {YELLOW}{event_time[:10]}{RESET}")
    elif event_type == 'CreateEvent':
        print(f"{BLUE}{i}-> ➕ Created{RESET} in {GREEN}{repo_name}{RESET} at {YELLOW}{event_time[:10]}{RESET}")
    elif event_type == 'DeleteEvent':
        print(f"{BLUE}{i}-> 🗑️ Deleted{RESET} in {GREEN}{repo_name}{RESET} at {YELLOW}{event_time[:10]}{RESET}")
    else:
        print(f"{BLUE}{i}-> ❓ Unknown{RESET} event type '{event_type}' in {GREEN}{repo_name}{RESET} at {YELLOW}{event_time[:10]}{RESET}")

def handle_rate_limiting(headers):
    remaining = int(headers.get('X-RateLimit-Remaining', 1))
    if remaining == 0:
        reset_time = int(headers.get('X-RateLimit-Reset', time.time()))
        wait_time = reset_time - time.time()
        print("API rate limit exceeded. Waiting for reset...")
        time.sleep(wait_time)

def main():
    username = get_github_username()
    jsondata, headers = get_github_events(username)
    handle_rate_limiting(headers)
    process_events(jsondata)

if __name__ == "__main__":
    main()
