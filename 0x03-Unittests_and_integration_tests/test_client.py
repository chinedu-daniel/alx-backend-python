#!/usr/bin/env python3
"""Module for testing client """
from client import GithubOrgClient
import unittest
from parameterized import parameterized
from unittest.mock import patch, PropertyMock
from utils import get_json


class TestGithubOrgClient(unittest.TestCase):
    """Test case for github organization client"""

    @parameterized.expand(
        [
            ("google",),
            ("abc",),
        ]
    )
    @patch("client.get_json")
    def test_org(self, org_name, mock_org):
        """Method ot test"""
        client = GithubOrgClient(org_name)
        mock_org.return_value = {"login": org_name}
        self.assertEqual(client.org, mock_org.return_value)
        mock_org.assert_called_once_with(
            f"https://api.github.com/orgs/{org_name}")

    @parameterized.expand(
        [
            ("google",),
            ("abc",),
        ]
    )
    def test_public_repos_url(self, org_name):
        """Mocking a property"""
        with patch.object(
            GithubOrgClient, "_public_repos_url", new_callable=PropertyMock
        ) as mocked_property:
            obj = GithubOrgClient(org_name)
            mocked_property.return_value = "this is a value"
            self.assertEqual(obj._public_repos_url,
                             mocked_property.return_value)
            mocked_property.assert_called_once()

    @parameterized.expand(
        [
            ("google",),
            ("abc",),
        ]
    )
    @patch("client.get_json")
    def test_public_repos(self, org_name, mock_get_json):
        """Testing public repos"""
        mock_get_json.return_value = [
            {"name": "repo1"},
            {"name": "repo2"},
            {"name": "repo3"},
        ]

        with patch.object(
            GithubOrgClient, "_public_repos_url", new_callable=PropertyMock
        ) as mocked_property:
            obj = GithubOrgClient(org_name)
            return_value = ["repo1", "repo2", "repo3"]
            self.assertEqual(obj.public_repos(), return_value)
            mock_get_json.assert_called_once()
            mocked_property.assert_called_once()

    @parameterized.expand([
        ({"license": {"key": "my_license"}}, "my_license", True),
        ({"license": {"key": "other_license"}}, "my_license", False),
    ])
    def test_has_license(self, repo, license_key,  expected):
        """Checking for repo license"""
        client = GithubOrgClient("google")

        result = client.has_license(repo, license_key)

        self.assertEqual(result, expected)
