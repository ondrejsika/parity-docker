#!/bin/sh

PORT_SHIFT=${1:-0}
CHAIN=${2:-livenet}

docker run -ti -p ${PORT_SHIFT}8180:8180 -p ${PORT_SHIFT}8545:8545 -p ${PORT_SHIFT}8546:8546 --name parity-$PORT_SHIFT --rm pool/parity $CHAIN

