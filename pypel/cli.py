# -*- coding: utf-8 -*-
import argparse
import os

from pypel.commands import delete_metadata, set_metadata
from pypel.gpg import sign, verify
from pypel.models import Receipt, SUPPORTED_EXT


def make_parsers():
    """Create the parsers for the CLI tool."""

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

    # A gpg command
    gpg_parser = subparsers.add_parser('gpg', help='Sign or verify receipt')
    gpg_group = gpg_parser.add_mutually_exclusive_group()
    gpg_group.add_argument('-s', '--sign', action='store_true',
                            help='sign receipt')
    gpg_group.add_argument('-v', '--verify', action='store_true',
                            help='verify receipt')

    all_subparsers = dict(
        show_parser=show_parser,
        set_parser=set_parser,
        del_parser=del_parser,
        sum_parser=sum_parser,
        gpg_parser=gpg_parser)

    # HACK: This can be fixed when http://bugs.python.org/issue9540 will be
    # closed.
    for subparser in all_subparsers:
        all_subparsers[subparser].add_argument('receipts',
                                               metavar='receipt',
                                               nargs='+',
                                               help='one or more receipts in a '
                                                    'supported format')

    return parser, all_subparsers

def main():

    parser, subparsers = make_parsers()
    args = parser.parse_args()

    table = []
    price_sum = 0
    max_len_receipt_filename = 0
    max_len_price = 0

    for receipt_file in args.receipts:

        if os.path.isdir(receipt_file):
            print('{}: is a directory.'.format(receipt_file))
            continue

        # Skip if receipt_file is not a supported file.
        if os.path.splitext(receipt_file)[1].lower() not in SUPPORTED_EXT:
            continue

        receipt = Receipt(receipt_file)

        if args.command_name == 'del':
            delete_metadata(receipt, args.price, args.retailer)

        if args.command_name == 'set':
            if args.price is None and args.retailer is None:
                subparsers['set_parser'].error('You must provide at least '
                                               '--price or --retailer.')
            set_metadata(receipt, args.price, args.retailer)

        elif args.command_name == 'show':
            table.append(dict(receipt=receipt_file,
                              price=receipt.price,
                              retailer=receipt.retailer))
            max_len_receipt_filename = max([len(receipt_file),
                                            max_len_receipt_filename])
            max_len_price = max([len(str(receipt.price)), max_len_price])

        elif args.command_name == 'sum':
            if receipt.price is not None:
                price_sum += receipt.price

        elif args.command_name == 'gpg':
            if not args.sign and not args.verify:
                subparsers['gpg_parser'].error('You must provide at least '
                                               '--sign or --verify.')

            if args.sign:
                sign(receipt_file)

            if args.verify:
                try:
                    verify(receipt_file)
                except ValueError as err:
                    print('{}: {}'.format(receipt_file, err))

    if args.command_name == 'show':
        for row in table:
            if row['price'] is None:
                price_fmt = '{2:^{3}}'
            else:
                price_fmt = '{2:{3}.2f}'
            fmt_str = '{0:{1}} -- ' + price_fmt + ' -- {4}'
            print(fmt_str.format(row['receipt'],
                                 max_len_receipt_filename,
                                 row['price'],
                                 max_len_price + 1,
                                 row['retailer']))
    elif args.command_name == 'sum':
        print('{0:.2f}'.format(price_sum))
