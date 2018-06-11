#!/usr/bin/python

import click

printable = '0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ!"#$%&\'()*+,-./:;<=>?@[\\]^_`{|}~'

while True:

    print('Continue? [yn] ')
    c = click.getchar()

    print()
    if c == 'y':
        print('We will go on')
    elif c == 'n':
        print('Abort!')
        break
    elif c == '\x1b[D':
        print('Left arrow <-')
    elif c == '\x1b[C':
        print('Right arrow ->')
    else:
        print('Invalid input :(')
        print('You pressed: "' + ''.join([ '\\'+hex(ord(i))[1:] if i not in printable else i for i in c ]) +'"' )