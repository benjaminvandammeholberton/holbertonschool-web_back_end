#!/usr/bin/env python3
""" Unittests module for utils file
"""
import unittest
from unittest.mock import patch
from parameterized import parameterized
from utils import access_nested_map, get_json
import requests


class TestAccessNestedMap(unittest.TestCase):
    """ Unitests for access_nested_map function
    """
    @parameterized.expand([
        ({"a": 1}, ("a",), 1),
        ({"a": {"b": 2}}, ("a",), {"b": 2}),
        ({"a": {"b": 2}}, ("a", "b"), 2),
    ])
    def test_access_nested_map(self, nested_map, path, expected):
        """ Unittests for access_nested_map function expected returns
        """
        self.assertEqual(access_nested_map(
            nested_map, path), expected)

    @parameterized.expand([
        ({}, ("a",)),
        ({"a": 1}, ("a", "b")),
    ])
    def test_access_nested_map_exception(self, nested_map, path):
        """ Unittests for access_nested_map function exceptions
        """
        with self.assertRaises(KeyError):
            access_nested_map(nested_map, path)


class TestGetJson(unittest.TestCase):
    """ Unit tests class for get_json function
    """
    @patch('requests.get')
    def test_get_json(self, mock_requests_get):
        """ Tests return values of get_json function
        """
        mock_response = mock_requests_get.return_value
        mock_response.json.return_value = {"payload": True}
        response = get_json("http://example.com")
        self.assertEqual(response, {"payload": True})
        mock_response.json.return_value = {"payload": False}
        response = get_json("http://holberton.io")
        self.assertEqual(response, {"payload": False})
