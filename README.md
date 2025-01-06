# EScript
EScript (Espresso Script) is a set of tools for writing beatiful,
script-like C. It uses a C library and a python "executable" to
run the file. It works (kinda?) like a C compiler, but doesn't
*do* the compiling, ``gcc`` does.

## Install
```sh
git clone https://github.com/ElisStaaf/escript
cd escript
sudo ./install.sh
```

## Usage
```sh
escript <file>
```

## Example
```c
printf("Starting loop...");
int i = 0;
do {
    printf("%d\n", i + 1);
} while (++i < 10);
printf("Loop ended!");
```
