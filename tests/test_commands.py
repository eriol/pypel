# -*- coding: utf-8 -*-

from test_models import ReceiptSetUpTestCase

from pypel.commands import delete_metadata, set_metadata

class CommandsTestCase(ReceiptSetUpTestCase):

    def test_set_metadata(self):
        """Test set_metadata command."""

        self.assertEqual(self.receipt.price, None)
        self.assertEqual(self.receipt.retailer, None)

        set_metadata(self.receipt, price=8.27)
        self.assertEqual(self.receipt.price, 8.27)
        self.assertEqual(self.receipt.retailer, None)

        set_metadata(self.receipt, retailer='Bazaar')
        self.assertEqual(self.receipt.retailer, 'Bazaar')

    def test_delete_metadata(self):
        """Test delete_metadata command."""

        set_metadata(self.receipt, price=8.27, retailer='Bazaar')

        self.assertEqual(self.receipt.price, 8.27)
        self.assertEqual(self.receipt.retailer, 'Bazaar')

        delete_metadata(self.receipt, price=True)
        self.assertEqual(self.receipt.price, None)

        delete_metadata(self.receipt, retailer=True)
        self.assertEqual(self.receipt.retailer, None)
