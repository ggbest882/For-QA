import os
import time
import requests
import unittest
from dotenv import load_dotenv

load_dotenv()

GITHUB_TOKEN = os.getenv("MY_SECRET")
GITHUB_USERNAME = os.getenv("GITHUB_USERNAME")
REPO_NAME = os.getenv("REPO_NAME")
BASE_URL = "https://api.github.com"

HEADERS = {
    "Authorization": f"token {GITHUB_TOKEN}",
    "Accept": "application/vnd.github.v3+json"
}

class TestGitHubAPI(unittest.TestCase):

    def test_create_and_check_repository(self):
        create_url = f"{BASE_URL}/user/repos"
        data = {
            "name": REPO_NAME,
            "auto_init": True,
            "private": False
        }

        create_response = requests.post(create_url, headers=HEADERS, json=data)
        self.assertEqual(create_response.status_code, 201, f"Failed to create repository: {create_response.json()}")

        check_url = f"{BASE_URL}/repos/{GITHUB_USERNAME}/{REPO_NAME}"

        check_response = requests.get(check_url, headers=HEADERS)
        self.assertEqual(check_response.status_code, 200, f"Repository not found: {check_response.json()}")

    def test_delete_repository(self):
        url = f"{BASE_URL}/repos/{GITHUB_USERNAME}/{REPO_NAME}"

        response = requests.delete(url, headers=HEADERS)
        self.assertEqual(response.status_code, 204, "Failed to delete repository")

if __name__ == "__main__":
    unittest.main()
