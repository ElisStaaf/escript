#!/usr/bin/bash

LIB=./lib
INC=/usr/include
TARGET=escript.h

sudo cp          \
    $LIB/$TARGET \
    $INC/$TARGET

SRC=./src
BIN=/usr/local/bin
FILE=escript.py

sudo cp        \
    $SRC/$FILE \
    $BIN/${FILE%.*}
