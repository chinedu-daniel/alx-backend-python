#!/usr/bin/env python3
"""
Parameterize a unit test
"""
import unittest
from parameterized import parameterized
from utils import access_nested_map, get_json, memoize
from unittest.mock import patch, Mock


class TestAccessNestedMap(unittest.TestCase):
    """
    A class that inherits from unittest.TestCase
    """
    @parameterized.expand([
        ({"a": 1}, ("a",), 1),
        ({"a": {"b": 2}}, ("a",), {"b": 2}),
        ({"a": {"b": 2}}, ("a", "b"), 2)
    ])
    def test_access_nested_map(self, nested_map, path, expected):
        """
        method to test that the method returns what it is supposed to
        """
        self.assertEqual(access_nested_map(nested_map, path=path), expected)

    @parameterized.expand([
        ({}, ("a",)),
        ({"a": 1}, ("a", "b"))
    ])
    def test_access_nested_map_exception(self, nested_map, path):
        """
        context manager to test that a KeyError
        """
        with self.assertRaises(KeyError) as context:
            access_nested_map(nested_map, path)

        self.assertEqual(str(context.exception), f"'{path[-1]}'")


class TestGetJson(unittest.TestCase):
    """
    Mock HTTP calls
    """
    @parameterized.expand([
        ("http://example.com", {"payload": True}),
        ("http://holberton.io", {"payload": False}),
    ])
    @patch('utils.requests.get')
    def test_get_json(self, url, payload, mock_get):
        """
        To test that utils.get_json returns the expected result
        """
        mock_response = Mock()
        mock_response.json.return_value = payload

        mock_get.return_value = mock_response

        result = get_json(url)

        self.assertEqual(result, payload)


class TestMemoize(unittest.TestCase):
    """
    Parameterize and patch
    """
    class TestClass:
        """Test Case"""
        def a_method(self):
            return 42

        @memoize
        def a_property(self):
            return self.a_method()

    @patch(TestClass, "a_method")
    def test_memoize(self, mock_method):
        """
        test_memoize
        """
        mock = self.TestClass()
        #mock_a_method.return_value = 42

        result1 = mock.a_property
        mock_methd.assert_called_once()

        result2 = mock.a_property()
        mock_a_method.assert_called_once()


if __name__ == "__main__":
    unittest.main()
