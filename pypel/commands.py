# -*- coding: utf-8 -*-

def delete_metadata(receipt, price=None, retailer=None):
    """Delete XMP metadata."""
    if not price and not retailer:
        del receipt.price
        del receipt.retailer

    if price:
        del receipt.price

    if retailer:
        del receipt.retailer

def set_metadata(receipt, price=None, retailer=None):
    """Set XMP metadata."""
    if price:
        receipt.price = price

    if retailer:
        receipt.retailer = retailer
