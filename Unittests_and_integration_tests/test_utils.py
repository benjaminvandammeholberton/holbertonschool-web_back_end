#!/usr/bin/env python3
""" Unittests module for utils file
"""
import unittest
from unittest.mock import patch, Mock
from parameterized import parameterized
from utils import access_nested_map, get_json, memoize
from typing import Dict


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
    """TestGetJson class"""

    @parameterized.expand([
        ("http://example.com", {"payload": True}),
        ("http://holberton.io", {"payload": False})
    ])
    @patch("requests.get")
    def test_get_json(
            self,
            test_url: str,
            test_payload: Dict,
            mock_get
    ) -> None:
        """Tests the get_json function"""

        mock_response = Mock()
        mock_response.json.return_value = test_payload

        mock_get.return_value = mock_response

        self.assertEqual(get_json(test_url), test_payload)


class TestMemoize(unittest.TestCase):
    """TestMemoize class"""

    def test_memoize(self) -> None:
        """Tests the memoize function"""

        class TestClass:

            def a_method(self):
                return 42

            @memoize
            def a_property(self):
                return self.a_method()

        my_obj = TestClass()
        with patch.object(my_obj, 'a_method') as mock_a_method:
            mock_a_method.return_value = 42
            result = my_obj.a_property
            self.assertEqual(result, 42)
            result = my_obj.a_property
            mock_a_method.assert_called_once()
