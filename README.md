# Dockerized Parity (Ethereum Client) with configuration

    Ondrej Sika <ondrej@ondrejsika.com>


## Usage

global optional arguments:

- `--dry` - print out the Docker command

### Build Docker image

```
./run.py build
```


### Run Parity container

```
usage: run.py run [-h] [-f] [-n] [-d DATA] instance chain
```

optional arguments:

-  `-f`, `--foreground`
-  `-n`, `--no-ports` - no port forwarding to host
-  `-d DATA`, `--data DATA` - blockchain and data path


Example run Parity with livenet configuration on default ports

```
./run.py run 0 livenet
```

Example run Parity with regtest configuration on shifted ports like: 8545 -> 18545

```
./run.py run 1 regtest
```


### Parity console

Console doesn't require port forwarding.

```
usage: run.py console [-h] instance
```

Example for livenet

```
./run.py console 0 livenet
```


### Stop and remove Parity container

```
usage: run.py rm [-h] instance chain
```

Example for livenet

```
./run.py rm 0 livenet
```
