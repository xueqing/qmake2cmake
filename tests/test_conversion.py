#!/usr/bin/env python3
#############################################################################
##
## Copyright (C) 2022 The Qt Company Ltd.
## Contact: https://www.qt.io/licensing/
##
## This file is part of the plugins of the Qt Toolkit.
##
## $QT_BEGIN_LICENSE:GPL-EXCEPT$
## Commercial License Usage
## Licensees holding valid commercial Qt licenses may use this file in
## accordance with the commercial license agreement provided with the
## Software or, alternatively, in accordance with the terms contained in
## a written agreement between you and The Qt Company. For licensing terms
## and conditions see https://www.qt.io/terms-conditions. For further
## information use the contact form at https://www.qt.io/contact-us.
##
## GNU General Public License Usage
## Alternatively, this file may be used under the terms of the GNU
## General Public License version 3 as published by the Free Software
## Foundation with exceptions as appearing in the file LICENSE.GPL3-EXCEPT
## included in the packaging of this file. Please review the following
## information to ensure the GNU General Public License requirements will
## be met: https://www.gnu.org/licenses/gpl-3.0.html.
##
## $QT_END_LICENSE$
##
#############################################################################

from pro2cmake import Scope, SetOperation, merge_scopes, recursive_evaluate_scope
from tempfile import TemporaryDirectory

import filecmp
import functools
import os
import pathlib
import pytest
import re
import shutil
import subprocess
import tempfile

from typing import Callable, Optional

debug_mode = bool(os.environ.get("DEBUG_QMAKE2CMAKE_TEST_CONVERSION"))
test_script_dir = pathlib.Path(__file__).parent.resolve()
qmake2cmake_dir = test_script_dir.parent.resolve()
qmake2cmake = qmake2cmake_dir.joinpath("qmake2cmake")
test_data_dir = test_script_dir.joinpath("data", "conversion")


def compare_expected_output_directories(actual: str, expected: str):
    dc = filecmp.dircmp(actual, expected)
    assert(dc.diff_files == [])


def convert(base_name: str, after_conversion_hook: Optional[Callable[[str], None]] = None):
    '''Converts {base_name}.pro to CMake in a temporary directory.

    The optional after_conversion_hook is a function that takes the temporary directory as
    parameter.  It is called after the conversion took place.
    '''
    pro_file_name = str(base_name) + ".pro"
    pro_file_path = test_data_dir.joinpath(pro_file_name)
    assert(pro_file_path.exists())
    with TemporaryDirectory(prefix="testqmake2cmake") as tmp_dir_str:
        tmp_dir = pathlib.Path(tmp_dir_str)
        output_file_path = tmp_dir.joinpath("CMakeLists.txt")
        exit_code = subprocess.call([qmake2cmake, "-o", output_file_path, pro_file_path])
        assert(exit_code == 0)
        if debug_mode:
            output_dir = tempfile.gettempdir() + "/qmake2cmake"
            if not os.path.isdir(output_dir):
                os.mkdir(output_dir)
            shutil.copyfile(output_file_path, output_dir + "/CMakeLists.txt")
        f = open(output_file_path, "r")
        assert(f)
        content = f.read()
        assert(content)
        if after_conversion_hook is not None:
            after_conversion_hook(tmp_dir)
        return content


def convert_and_compare_expected_output(pro_base_name: str, rel_expected_output_dir: str):
    abs_expected_output_dir = test_data_dir.joinpath(rel_expected_output_dir)
    convert(pro_base_name, functools.partial(compare_expected_output_directories,
                                             expected=abs_expected_output_dir))


def test_qt_modules():
    '''Test the conversion of QT assignments to find_package calls.'''
    output = convert("required_qt_modules")
    find_package_lines = []
    for line in output.split("\n"):
        if "find_package(" in line:
            find_package_lines.append(line.strip())
    assert(["find_package(QT NAMES Qt5 Qt6 REQUIRED COMPONENTS Core)",
            "find_package(Qt${QT_VERSION_MAJOR} REQUIRED COMPONENTS Network Widgets)"] == find_package_lines)

    output = convert("optional_qt_modules")
    find_package_lines = []
    for line in output.split("\n"):
        if "find_package(" in line:
            find_package_lines.append(line.strip())
    assert(["find_package(QT NAMES Qt5 Qt6 REQUIRED COMPONENTS Core)",
            "find_package(Qt${QT_VERSION_MAJOR} REQUIRED COMPONENTS Network Widgets)",
            "find_package(Qt${QT_VERSION_MAJOR} OPTIONAL_COMPONENTS OpenGL)"] == find_package_lines)

def test_qt_version_check():
    '''Test the conversion of QT_VERSION checks.'''
    output = convert("qt_version_check")
    interesting_lines = []
    for line in output.split("\n"):
        if line.startswith("if(") and "QT_VERSION" in line:
            interesting_lines.append(line.strip())
    assert(["if(( ( (QT_VERSION_MAJOR GREATER 5) ) AND (QT_VERSION_MINOR LESS 1) ) AND (QT_VERSION_PATCH EQUAL 0))", "if(( ( (QT_VERSION VERSION_GREATER 6.6.5) ) AND (QT_VERSION VERSION_LESS 6.6.7) ) AND (QT_VERSION VERSION_EQUAL 6.6.6))"] == interesting_lines)


def test_subdirs():
    '''Test conversion of a TEMPLATE=subdirs project.'''
    convert_and_compare_expected_output("subdirs/subdirs", "subdirs/expected")