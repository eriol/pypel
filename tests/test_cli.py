# coding: utf-8
""" Tests for pypel.cli.

THIS SOFTWARE IS UNDER BSD LICENSE.
Copyright (c) 2012-2015 Daniele Tricoli <eriol@mornie.org>

Read LICENSE for more informations.
"""

import unittest

from pypel.cli import Row, Table


class RowTestCase(unittest.TestCase):

    def test_empty(self):
        row = Row()

        self.assertEqual(row.len(), None)
        with self.assertRaises(TypeError):
            row.format()
        with self.assertRaises(KeyError):
            row.format('price')

    def test_float(self):
        row = Row({'price': 2.71})

        self.assertEqual(row.len('price'), 4)
        self.assertEqual(row.format('price'), '{price:>{price_len}.2f}')

    def test_int(self):
        row = Row({'price': 2})

        self.assertEqual(row.len('price'), 1)
        self.assertEqual(row.format('price'), '{price:{price_len}}')

    def test_str(self):
        row = Row({'note': 'A simply note.'})
        self.assertEqual(row.len('note'), 14)
        self.assertEqual(row.format('note'), '{note:{note_len}}')


class TableTestCase(unittest.TestCase):

    def setUp(self):
        self.table = Table()

    def test_empty(self):
        self.assertEqual(self.table.rows, [])
        self.assertEqual(self.table.max_len, {})

    def test_add_new_row(self):
        row = Row({'price': 2.71, 'note': 'An useless note.'})
        self.table.add_row(row)

        self.assertEqual(len(self.table.rows), 1)
