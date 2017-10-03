#!/usr/bin/env python

import argparse
import os


def _chain(val):
    if val not in ('livenet', 'regtest'):
        raise Exception('Chain must be "livenet" or "regtest"')
    return val


def _port_shift(val):
    val = int(val)
    if not 0 <= val <= 5:
        raise Exception('Port shift must be one of 0, 1, 2, 3, 4, 5')
    return val


root_parser = argparse.ArgumentParser()
root_subparsers = root_parser.add_subparsers(dest='command0')
root_parser.add_argument('--dry', action='store_true')

build_parser = root_subparsers.add_parser('build')

run_parser = root_subparsers.add_parser('run')
run_parser.add_argument('--foreground', action='store_true')
run_parser.add_argument('-n', '--no-ports', action='store_true')
run_parser.add_argument('-s', '--port-shift', type=_port_shift, default=0)
run_parser.add_argument('chain', type=_chain)


def _system(command, args):
    if args.dry:
        print command
    else:
        os.system(command)


def build(args):
    _system('docker build -t pool/parity .', args)


def run(args):
    ports = '-p {shift}8180:8180 -p {shift}8545:8545 -p {shift}8546:8546'.format(shift=args.port_shift) if not args.no_ports else ''
    foreground = '--rm' if args.foreground else '-d'
    shift = '-%s' % args.port_shift if args.port_shift else ''
    _system('docker run {foreground} {ports} --name parity-{chain}{shift} pool/parity {chain}'.format(ports=ports, chain=args.chain, shift=shift, foreground=foreground), args)


args = root_parser.parse_args()
{
    'build': build,
    'run': run,
}[args.command0](args)
