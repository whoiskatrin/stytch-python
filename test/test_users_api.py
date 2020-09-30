# coding: utf-8

"""
    Stytch

    This is the Stytch api.  You can find out more about Stytch at  [stytch.io](https://stytch.io).   # noqa: E501

    OpenAPI spec version: 1.0.0
    Contact: hello@stytch.io
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""

from __future__ import absolute_import

import unittest

import swagger_client
from swagger_client.api.users_api import UsersApi  # noqa: E501
from swagger_client.rest import ApiException


class TestUsersApi(unittest.TestCase):
    """UsersApi unit test stubs"""

    def setUp(self):
        self.api = UsersApi()  # noqa: E501

    def tearDown(self):
        pass

    def test_create_user(self):
        """Test case for create_user

        Create user  # noqa: E501
        """
        pass

    def test_delete_email(self):
        """Test case for delete_email

        Delete email  # noqa: E501
        """
        pass

    def test_delete_user(self):
        """Test case for delete_user

        Delete user  # noqa: E501
        """
        pass

    def test_get_user_by_id(self):
        """Test case for get_user_by_id

        Get user  # noqa: E501
        """
        pass

    def test_get_user_email_verify(self):
        """Test case for get_user_email_verify

        Verify email  # noqa: E501
        """
        pass

    def test_update_user(self):
        """Test case for update_user

        Update user  # noqa: E501
        """
        pass


if __name__ == '__main__':
    unittest.main()