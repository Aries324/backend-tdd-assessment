#!/usr/bin/env python
# -*- coding: utf-8 -*-


import unittest
import echo
import subprocess


class TestEcho(unittest.TestCase):

    # Test setUp()
    def setUp(self):
        self.parser = echo.create_parser()

    # Help Test
    def test_help(self):
        """ Running the program without arguments should show usage. """

        # Run the command `python ./echo.py -h` in a separate process, then
        # collect it's output.
        process = subprocess.Popen(
            ["python", "./echo.py", "-h"],
            stdout=subprocess.PIPE)
        stdout, _ = process.communicate()
        usage = open("./USAGE", "r").read()

        self.assertEquals(stdout, usage)

    def test_text(self):
        args = ["hello world"]
        namespace = self.parser.parse_args(args)
        self.assertEqual(namespace.text, "hello world")

    def test_no_args(self):
        process = subprocess.Popen(
            ["python", "./echo.py"], stdout=subprocess.PIPE)
        stdout, _ = process.communicate()
        usage_reminder = "usage: echo.py [-h] [-u] [-l] [-t] text\n"
        self.assertEqual(stdout, usage_reminder)

    def test_upper_short(self):
        args = ["-u", "hello world"]
        namespace = self.parser.parse_args(args)
        self.assertEqual(namespace.upper, True)
        self.assertEqual(echo.main(args), "HELLO WORLD")

    def test_lower_short(self):
        args = ["-l", "HELLO WORLD"]
        namespace = self.parser.parse_args(args)
        self.assertEqual(namespace.lower, True)
        self.assertEqual(echo.main(args), "hello world")

    def test_title_short(self):
        args = ["-t", "hello world"]
        namespace = self.parser.parse_args(args)
        self.assertEqual(namespace.title, True)
        self.assertEqual(echo.main(args), "Hello World")

    def test_upper_long(self):
        args = ["--upper", "hello world"]
        namespace = self.parser.parse_args(args)
        self.assertEqual(namespace.upper, True)
        self.assertEqual(echo.main(args), "HELLO WORLD")

    def test_lower_long(self):
        args = ["--lower", "HELLO WORLD"]
        namespace = self.parser.parse_args(args)
        self.assertEqual(namespace.lower, True)
        self.assertEqual(echo.main(args), "hello world")

    def test_title_long(self):
        args = ["--title", "hello world"]
        namespace = self.parser.parse_args(args)
        self.assertEqual(namespace.title, True)
        self.assertEqual(echo.main(args), "Hello World")

    def test_all(self):
        args = ["-u", "-l", "-t", "hello world"]
        namespace = self.parser.parse_args(args)
        self.assertEqual(namespace.upper, True)
        self.assertEqual(namespace.lower, True)
        self.assertEqual(namespace.title, True)
        self.assertEqual(echo.main(args), "hello world")
#     def test_help_big(self):
#         process = subprocess.Popen(
#             ["python", "./echo.py", "--help"],
#             stdout=subprocess.PIPE)
#         stdout, _ = process.communicate()
#         usage = open("./USAGE", "r").read()

#         self.assertEquals(stdout, usage)

#     # Upper Test
#     def test_upper_small(self):
#         args = ["hello", "-u"]
#         namespace = self.parser.parse_args(args)
#         self.assertTrue(namespace.upper)
#         self.assertEquals(echo.main(args), "HELLO")

#     def test_upper_big(self):
#         args = ["hello", "--upper"]
#         namespace = self.parser.parse_args(args)
#         self.assertTrue(namespace.upper)
#         self.assertEquals(echo.main(args), "HELLO")

#     # Lower Test
#     def test_lower_small(self):
#         args = ["hello", "-l"]
#         namespace = self.parser.parse_args(args)
#         self.assertTrue(namespace.lower)
#         self.assertEquals(echo.main(args), "hello")

#     def test_lower_big(self):
#         args = ["hello", "--lower"]
#         namespace = self.parser.parse_args(args)
#         self.assertTrue(namespace.lower)
#         self.assertEquals(echo.main(args), "hello")

#     # Title Test
#     def test_title_small(self):
#         args = ["hello", "-t"]
#         namespace = self.parser.parse_args(args)
#         self.assertTrue(namespace.capitalize)
#         self.assertEquals(echo.main(args), "Hello")

#     def test_title_big(self):
#         args = ["hello", "--title"]
#         namespace = self.parser.parse_args(args)
#         self.assertTrue(namespace.capitalize)
#         self.assertEquals(echo.main(args), "Hello")

#     # Multi-Args Test
#     def test_three_small(self):
#         args = ["hello", "-tul"]
#         namespace = self.parser.parse_args(args)
#         pass

#     def test_two_small(self):
#         args = ["hello", "-ul"]
#         namespace = self.parser.parse_args(args)
#         pass

#     # Test tearDown()
#     def tearDown(self):
#         self.parser.tearDown()
#         self.parser = None


if __name__ == '__main__':
    unittest.main()
