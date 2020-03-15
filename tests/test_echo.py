#!/usr/bin/env python
# -*- coding: utf-8 -*-


import unittest
import echo
import subprocess


class TestEcho(unittest.TestCase):

    # Test setUp()
    def setUp(self):
        """
        This function is called only once for all tests.
        """
        self.parser = echo.create_parser()

    # Help Test
    def test_help(self):
        """ Running the program without arguments should show usage. """

        # Run the command `python ./echo.py -h` in a separate process, then
        # collect it's output.
        process = subprocess.Popen(
            ["python", "./echo.py", "-h", "--help"],
            stdout=subprocess.PIPE)
        stdout, _ = process.communicate()
        with open("./USAGE") as f:
            usage = f.read()
        self.assertEquals(stdout, usage)

    def test_text(self):
        args = ["hello world"]
        namespace = self.parser.parse_args(args)
        self.assertEqual(namespace.text, "hello world")

    def test_no_args(self):
        args = ["hello world"]
        namespace = self.parser.parse_args(args)
        self.assertEqual(namespace.upper, False)
        self.assertEqual(namespace.lower, False)
        self.assertEqual(namespace.title, False)
        self.assertEqual(echo.main(args), "hello world")

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
        args = ["-tul", "hello world"]
        namespace = self.parser.parse_args(args)
        self.assertEqual(namespace.upper, True)
        self.assertEqual(namespace.lower, True)
        self.assertEqual(namespace.title, True)
        self.assertEqual(echo.main(args), "Hello World")

        # Test tearDown()

        def tearDown(self):
            self.parser.tearDown()
        self.parser = None


if __name__ == '__main__':
    unittest.main()
