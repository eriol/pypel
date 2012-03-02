# -*- coding: utf-8 -*-
import argparse
import os
import sys

from ebenezer.xmp import XMPReceiptMetadata, SUPPORTED_EXT

def main():
    parser = argparse.ArgumentParser(description='Easy receipts management.')
    subparsers = parser.add_subparsers(dest='command_name', help='commands')

    # A show command
    show_parser = subparsers.add_parser('show', help='Show receipt\'s metadata')
    show_parser.add_argument('-s', '--sum', action='store_true',
                             help='sum receipts\' price')
    # A set command
    set_parser = subparsers.add_parser('set', help='Set receipt\'s metadata')
    set_parser.add_argument('-p', '--price', action='store', type=float,
                            help='set receipt\'s price')
    set_parser.add_argument('-r', '--retailer', action='store', type=str,
                            help='set receipt\'s retailer')
    # A delete command
    del_parser = subparsers.add_parser('del', help='Delete receipt\'s metadata')
    del_parser.add_argument('-p', '--price', action='store_true',
                            help='delete receipt\'s price')
    del_parser.add_argument('-r', '--retailer', action='store_true',
                            help='delete receipt\'s retailer')

    # A sum command
    sum_parser = subparsers.add_parser('sum', help='Sum receipts\' price')

    # HACK: This can be fixed when http://bugs.python.org/issue9540 will be
    # closed.
    for subparser in (show_parser, set_parser, del_parser, sum_parser):
        subparser.add_argument('receipts', metavar='receipt', nargs='+',
                               help='one or more receipts in a supported '
                                    'format')

    args = parser.parse_args()

    table = []
    price_sum = 0
    max_len_receipt_filename = 0
    max_len_price = 0

    for receipt in args.receipts:

        if os.path.isdir(receipt):
            exit_msg = '{} is a directory'.format(receipt)
            sys.exit(exit_msg)

        # Skip if receipt is not an image file.
        if os.path.splitext(receipt)[1].lower() not in SUPPORTED_EXT:
            continue

        metadata = XMPReceiptMetadata(receipt)

        if args.command_name == 'del':
            if not args.price and not args.retailer:
                del metadata.price
                del metadata.retailer
            elif args.price:
                del metadata.price
            elif args.retailer:
                del metadata.retailer
        if args.command_name == 'set':
            if args.price is None and args.retailer is None:
                set_parser.error('You must provide at least --price '
                                 'or --retailer.')
            if args.price:
                metadata.price = args.price

            if args.retailer:
                metadata.retailer = args.retailer
        elif args.command_name == 'show':
            table.append(dict(receipt=receipt,
                              price=metadata.price,
                              retailer=metadata.retailer))
            max_len_receipt_filename = max([len(receipt),
                                            max_len_receipt_filename])
            max_len_price = max([len(str(metadata.price)), max_len_price])

        elif args.command_name == 'sum':
            price_sum += metadata.price

    if args.command_name == 'show':
        for row in table:
            if row['price'] is None:
                price_fmt = '{2:{3}}'
            else:
                price_fmt = '{2:{3}.2f}'
            fmt_str = '{0:{1}} -- ' + price_fmt + ' -- {4}'
            print(fmt_str.format(row['receipt'],
                                 max_len_receipt_filename,
                                 row['price'],
                                 max_len_price,
                                 row['retailer']))
    elif args.command_name == 'sum':
        print('{0:.2f}'.format(price_sum))
