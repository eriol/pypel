# -*- coding: utf-8 -*-
import argparse

from ebenezer.xmp import XMPReceiptMetadata

def main():
    parser = argparse.ArgumentParser(description='Easy receipts management.')
    parser.add_argument('-s', '--sum', action='store_true',
                        help='sum receipts\' price')
    parser.add_argument('-p', '--price', action='store', type=float,
                        help='receipt\'s price')
    parser.add_argument('-r', '--retailer', action='store', type=str,
                        help='show receipt\'s retailer')
    parser.add_argument('receipts', metavar='receipt', nargs='+',
                        help='a receipt in a supported format')
    args = parser.parse_args()

    price_sum = 0
    max_len_receipt_filename = max([len(receipt) for receipt in args.receipts])

    for receipt in args.receipts:
        metadata = XMPReceiptMetadata(receipt)

        if args.price is not None:
            metadata.price = args.price

        if args.retailer:
            metadata.retailer = args.retailer

        if args.sum:
            price_sum += metadata.price

        if args.price is None and not args.retailer and not args.sum:
            print('{0:{1}} -- {2:.2f} -- {3}'.format(receipt,
                                                     max_len_receipt_filename,
                                                     metadata.price,
                                                     metadata.retailer))

    if args.sum:
        print('{0:.2f}'.format(price_sum))
