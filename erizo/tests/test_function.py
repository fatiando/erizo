# Copyright (c) 2019 The Erizo Developers.
# Distributed under the terms of the BSD 3-Clause License.
# SPDX-License-Identifier: BSD-3-Clause
#
# This code is part of the Fatiando a Terra project (https://www.fatiando.org)
#
"""
Test the function module
"""
import pytest

from ..function import function


@pytest.mark.parametrize("name", ["Gauss", "Green", "Newton"])
def test_function(name):
    "Check that function returns the right welcome message"
    assert function(name=name) == "Welcome to the project, {}!".format(name)
