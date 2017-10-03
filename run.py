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


def _path(val):
    if os.path.isabs(val):
        return val
    else:
        return os.path.abspath(os.path.join(os.path.dirname(__file__), val))

root_parser = argparse.ArgumentParser()
root_subparsers = root_parser.add_subparsers(dest='command0')
root_parser.add_argument('--dry', action='store_true')

build_parser = root_subparsers.add_parser('build')

run_parser = root_subparsers.add_parser('run')
run_parser.add_argument('-f', '--foreground', action='store_true')
run_parser.add_argument('-n', '--no-ports', action='store_true')
run_parser.add_argument('-d', '--data', type=_path)
run_parser.add_argument('instance', type=_port_shift, default=0)
run_parser.add_argument('chain', type=_chain)

rm_parser = root_subparsers.add_parser('rm')
rm_parser.add_argument('instance', type=_port_shift, default=0)
rm_parser.add_argument('chain', type=_chain)

console_parser = root_subparsers.add_parser('console')
console_parser.add_argument('instance', type=_port_shift, default=0)
console_parser.add_argument('chain', type=_chain)


def _system(command, args):
    if args.dry:
        print command
    else:
        os.system(command)


def build(args):
    _system('docker build -t pool/parity .', args)


def run(args):
    ports = '-p {shift}8180:8180 -p {shift}8545:8545 -p {shift}8546:8546'.format(shift=args.instance) if not args.no_ports else ''
    foreground = '--rm' if args.foreground else '-d'
    volumes = '-v {path}:/ethereum'.format(path=args.data) if args.data else ''
    _system('docker run {foreground} {ports} {volumes} --name parity-{instance}-{chain} pool/parity {chain}'.format(ports=ports, chain=args.chain, instance=args.instance, foreground=foreground, volumes=volumes), args)


def rm(args):
    _system('docker rm -f parity-{instance}-{chain}'.format(chain=args.chain, instance=args.instance), args)


def console(args):
    _system('docker exec -ti parity-{instance}-{chain} /app/geth attach http://127.0.0.1:8545'.format(chain=args.chain, instance=args.instance), args)


args = root_parser.parse_args()
{
    'build': build,
    'run': run,
    'rm': rm,
    'console': console,
}[args.command0](args)
