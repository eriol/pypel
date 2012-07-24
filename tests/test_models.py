# -*- coding: utf-8 -*-

import tempfile
import unittest


import cairo


from pypel.models import Receipt


class ReceiptSetUpTestCase(unittest.TestCase):
    """Create a temporary receipt."""

    def setUp(self):

        self.size = 100, 100
        self.image = cairo.ImageSurface(cairo.FORMAT_RGB24,
                                        self.size[0],
                                        self.size[1])

        self.tmp_file = tempfile.NamedTemporaryFile()
        self.image.write_to_png(self.tmp_file.name)

        self.receipt = Receipt(self.tmp_file.name)

    def tearDown(self):
        self.tmp_file.close()

class ReceiptMetadataTestCase(ReceiptSetUpTestCase):

    def testPrice(self):
        """Set/get price for receipt."""
        self.receipt.price = 8.27
        self.assertEqual(self.receipt.price, 8.27)

        del self.receipt.price
        self.assertEqual(self.receipt.price, None)

    def testRetailer(self):
        """Set/get retailer for receipt."""
        self.receipt.retailer = 'Bazaar'
        self.assertEqual(self.receipt.retailer, 'Bazaar')

        del self.receipt.retailer
        self.assertEqual(self.receipt.retailer, None)
