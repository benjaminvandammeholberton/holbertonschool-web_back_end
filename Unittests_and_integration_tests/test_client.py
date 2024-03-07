#!/usr/bin/env python3
"""Test client module
"""
import unittest
from fixtures import TEST_PAYLOAD
from unittest.mock import patch, Mock, PropertyMock
from parameterized import parameterized, parameterized_class
from client import GithubOrgClient


class TestGithubOrgClient(unittest.TestCase):
    """TestGithubOrgClient class
    """
    @parameterized.expand([
        ("google"),
        ("abc")
    ])
    @patch('client.get_json')
    def test_org(self, org):
        """Test the org method
        """
        with patch('client.get_json') as mock_get_json:
            mock_get_json.return_value = {}

            github_client = GithubOrgClient(org)
            result = github_client.org
            mock_get_json.assert_called_once()
            self.assertEqual(result, {})

    def test_public_repos_url(self):
        """Test the _public_repos_url property
        """
        with patch("client.GithubOrgClient.org",
                   new_callable=PropertyMock) as mock_org:

            mock_org.return_value = {"https://example.com"}
            github_client = GithubOrgClient("example")
            result = github_client.org
            self.assertEqual(result, "https://example.com")

    def test_public_repos(self):
        """Test the public_repos method
        """
        with patch("client.GithubOrgClient._public_repos_url",
                   new_callable=PropertyMock) as mock_org:

            mock_org.return_value = "https://example.com"
            with patch("client.get_json") as mock_get_json:
                mock_get_json.return_value = [{"name": "example"}]
                github_client = GithubOrgClient("example")
                result = github_client.public_repos()
                self.assertEqual(result, ["example"])
                mock_get_json.assert_called_once_with("https://example.com")

    @parameterized.expand([
        ({"license": {"key": "my_license"}}, "my_license", True),
        ({"license": {"key": "other_license"}}, "my_license", False)
    ])
    def test_has_license(self, repo, license_key, expected):
        """Test the has_license method
        """
        github_client = GithubOrgClient("example")
        result = github_client.has_license(repo, license_key)
        self.assertEqual(result, expected)


@parameterized_class(('org_payload', 'repos_payload',
                     'expected_repos', 'apache2_repos'), TEST_PAYLOAD)
class TestIntegrationGithubOrgClient(unittest.TestCase):
    """TestTestIntegrationGithubOrgClient class
    """
    # @classmethod
    # def setUpClass(cls):
    #     """Set up class method
    #     """
    #     cls.get_patcher = patch('requests.get')

    #     cls.mock_get = cls.get_patcher.start()
    #     cls.mock_get.side_effect = [
    #         Mock(json=lambda: cls.org_payload),
    #         Mock(json=lambda: cls.repos_payload),
    #     ]
    @classmethod
    def setUpClass(cls):
        """Set up class method"""
        cls.get_patcher = patch('requests.get')
        cls.mock_get = cls.get_patcher.start()

        # Créer des objets Mock pour les réponses JSON de
        # l'organisation et des dépôts
        cls.mock_response_org = Mock()
        cls.mock_response_repos = Mock()

        # Configurer la méthode json des objets Mock avec les valeurs attendues
        cls.mock_response_org.json.return_value = cls.org_payload
        cls.mock_response_repos.json.return_value = cls.repos_payload

        # Configurer le side_effect avec les objets Mock
        cls.mock_get.side_effect = [
            cls.mock_response_org,
            cls.mock_response_repos,
        ]

    @classmethod
    def tearDownClass(cls):
        """Tear down class method
        """
        cls.get_patcher.stop()

    def test_public_repos(self):
        """Test the public_repos method in an integration test
        """
        github_client = GithubOrgClient("google")
        result = github_client.public_repos()

        self.assertEqual(result, self.expected_repos)

    def test_public_repos_with_license(self):
        """Test the public_repos method with license in an integration test
        """
        github_client = GithubOrgClient("google")
        result = github_client.public_repos("apache-2.0")

        self.assertEqual(result, self.apache2_repos)
