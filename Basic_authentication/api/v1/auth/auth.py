#!/usr/bin/env python3
""" Module of Auth views
"""

from typing import List, TypeVar
from flask import request


class Auth:
    """ Auth class
    """
    def require_auth(self, path: str, excluded_paths: List[str]) -> bool:
        """Check if authentication is required"""
        return False

    def authorization_header(self, request=None) -> str:
        """Get authorization header from request
        """
        return None

    def current_user(self, request=None) -> TypeVar('User'):
        """Get current user from request"""
        return None
