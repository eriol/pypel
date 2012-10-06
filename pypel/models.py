# -*- coding: utf-8 -*-
import pyexiv2

PRICE_KEY = 'Xmp.pypel.Price'
RETAILER_KEY = 'Xmp.pypel.Retailer'

SUPPORTED_EXT = ('.jpg', '.jpeg', '.png', '.eps')

pyexiv2.xmp.register_namespace('http://mornie.org/xmp/pypel/', 'pypel')

class Receipt(object):

    def __init__(self, file):
        self.file = file
        self._metadata = pyexiv2.ImageMetadata(file)
        self._metadata.read()

    @property
    def price(self):
        try:
            return float(self._metadata[PRICE_KEY].value)
        except KeyError:
            pass

    @price.setter
    def price(self, price):
        self._metadata[PRICE_KEY] = str(price)
        self._metadata.write()

    @price.deleter
    def price(self):
        try:
            del self._metadata[PRICE_KEY]
        except KeyError:
            pass
        self._metadata.write()

    @property
    def retailer(self):
        try:
            return self._metadata[RETAILER_KEY].value
        except KeyError:
            pass

    @retailer.setter
    def retailer(self, retailer):
        self._metadata[RETAILER_KEY] = retailer
        self._metadata.write()

    @retailer.deleter
    def retailer(self):
        try:
            del self._metadata[RETAILER_KEY]
        except KeyError:
            pass
        self._metadata.write()
