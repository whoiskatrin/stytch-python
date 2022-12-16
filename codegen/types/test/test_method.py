#!/usr/bin/env python3

import unittest

from codegen.types.http_method import HttpMethod
from codegen.types.method import InvalidMethodSpecError, Method
from codegen.types.response_type import ResponseType


class TestMethod(unittest.TestCase):
    def setUp(self) -> None:
        self.methods = {
            "get": Method(
                "get",
                method=HttpMethod.GET,
                api_path="get",
                args=[],
                response_type=ResponseType(name="GetResponse", d={}),
            ),
            "post": Method(
                "post",
                method=HttpMethod.POST,
                api_path="post",
                args=[],
                response_type=ResponseType(name="PostResponse", d={}),
            ),
            "put": Method(
                "put",
                method=HttpMethod.PUT,
                api_path="put",
                args=[],
                response_type=ResponseType(name="PutResponse", d={}),
            ),
            "delete": Method(
                "delete",
                method=HttpMethod.DELETE,
                api_path="delete",
                args=[],
            ),
            "manual": Method(
                "manual",
                # Even though api_path isn't used, it will default to `name`
                api_path="manual",
                args=[],
                manual_implementation=True,
            ),
        }
        pass

    def test_params_or_json(self) -> None:
        # Act and assert
        self.assertEqual("params", self.methods["get"].params_or_json)
        self.assertEqual("json", self.methods["post"].params_or_json)
        self.assertEqual("json", self.methods["put"].params_or_json)
        self.assertEqual(
            "SHOULD_NEVER_BE_CALLED", self.methods["delete"].params_or_json
        )

    def test_is_delete_method(self) -> None:
        # Act and assert
        self.assertFalse(self.methods["get"].is_delete_method)
        self.assertFalse(self.methods["post"].is_delete_method)
        self.assertFalse(self.methods["put"].is_delete_method)
        self.assertTrue(self.methods["delete"].is_delete_method)

    def test_return_type_name(self) -> None:
        # Arrange
        tests_with_expected = [
            ("authenticate", "AuthenticateResponse"),
            ("authenticate_start", "AuthenticateStartResponse"),
            ("a_b_c", "ABCResponse"),
        ]
        for name, expected in tests_with_expected:
            # Act
            actual = Method.return_type_name(name)
            # Assert
            self.assertEqual(expected, actual)

    def test_from_dict(self) -> None:
        # Arrange
        d = {
            "name": "get",
            "args": [],
            "api_path": "get",
            "response_type": {},
            "eval_api_path": False,
            "manual_implementation": False,
            "use_base_path_as_api_path": False,
            "method": "GET",
        }

        with self.subTest("all_present"):
            # Act
            actual = Method.from_dict(d)
            # Assert
            self.assertEqual(self.methods["get"], actual)
        with self.subTest("use_base_path_as_api_path"):
            # Arrange more
            this_data = d.copy()
            this_data["use_base_path_as_api_path"] = True
            # Act
            actual = Method.from_dict(this_data)
            # Assert
            self.assertEqual(self.methods["get"], actual)
        with self.subTest("manual_implementation"):
            # Arrange more
            this_data = d.copy()
            this_data["name"] = "manual"
            this_data["manual_implementation"] = True
            del this_data["method"]
            del this_data["api_path"]
            del this_data["response_type"]
            # Act
            actual = Method.from_dict(this_data)
            # Assert
            self.assertEqual(self.methods["manual"], actual)
        with self.subTest("minimal"):
            # Arrange more
            this_data = d.copy()
            del this_data["api_path"]
            del this_data["eval_api_path"]
            del this_data["use_base_path_as_api_path"]
            del this_data["manual_implementation"]
            # Act
            actual = Method.from_dict(this_data)
            # Assert
            self.assertEqual(self.methods["get"], actual)
        with self.subTest("invalid_no_method"):
            # Arrange more
            this_data = d.copy()
            del this_data["method"]
            # Act and assert
            with self.assertRaises(InvalidMethodSpecError):
                Method.from_dict(this_data)
        with self.subTest("invalid_no_response_type"):
            # Arrange more
            this_data = d.copy()
            del this_data["response_type"]
            # Act and assert
            with self.assertRaises(InvalidMethodSpecError):
                Method.from_dict(this_data)