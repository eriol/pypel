# -*- coding: utf-8 -*-
import os.path

import gnupg

gpg = gnupg.GPG()

def _sign_file_path(file_path):
    return file_path + '.sig'

def sign(file_path, keyid=None):

    with open(file_path, 'rb') as f:
        signed = gpg.sign_file(f, keyid, detach=True)

    sign_file_path = _sign_file_path(file_path)

    with open(sign_file_path, 'wb') as sign_file:
        sign_file.write(signed.data)


def verify(file_path):

    with open(_sign_file_path(file_path), 'rb') as f:
        verified = gpg.verify_file(f, file_path)

        if not verified:
            raise ValueError('Signature could not be verified!')

        return verified
