#!/usr/bin/python3

# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
# Copyright (c) 2025 Elis Staaf                                             #
#                                                                           #
# Licensed under the Apache License, Version 2.0 (the "License");           #
# you may not use this file except in compliance with the License.          #
# You may obtain a copy of the License at                                   #
#                                                                           #
#     http://www.apache.org/licenses/LICENSE-2.0                            #
#                                                                           #
# Unless required by applicable law or agreed to in writing, software       #
# distributed under the License is distributed on an "AS IS" BASIS,         #
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.  #
# See the License for the specific language governing permissions and       #
# limitations under the License.                                            #
# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

from sys import argv
argc: int = len(argv)

import os

OPEN_BRACKET:   str = "{"
CLOSED_BRACKET: str = "}"

USAGE: str = """ESCRIPT
    EScript is a tool that allows you
    to easily write C in script mode, e.g
    this is normal C:
        #include <stdio.h>

        int main() {
            printf(\"Hello World!\\n\");
            return 0;
        }
    But *this* is script mode:
        printf(\"Hello World!\\n\");
USAGE:
    escript <file>
FLAGS:
    -h, --help: Show this message
    -S, --Save: Save all tmp files
"""

def script(src: str):
    return f"""/* THIS IS A FILE
* GENERATED BY ESCRIPT,
* DO NOT MODIFY.
*/

/* STDLIB */
#include <assert.h>
#include <errno.h>
#include <stdbool.h>
#include <stddef.h>
#include <stdint.h>
#include <stdio.h>
#include <stdlib.h>

/* ESCRIPT.LIB */
#include <escript.h>

/* ESCRIPT.MAIN */
DO {OPEN_BRACKET}
{src}
return 0;
{CLOSED_BRACKET}"""

HELP_FLAGS: list[str] = ["-h", "--help"]
SAVE_FLAGS: list[str] = ["-S", "--Save"]

def rmext(arr: str) -> str:
    tmp_arr: list[str] = arr.split(".")
    tmp_arr[-1] = ""
    return "".join(tmp_arr)

class EScript:
    def __init__(self, file: str) -> None:
        self.file:    str = file
        self.outfile: str = f"{rmext(file)}.escript.c"
        self.binfile: str = f"{rmext(file)}"
        with open(file, "r") as f:
            self.src: str = f.read()
            f.close()
        
    def compile(self, save: bool = False) -> None:
        with open(self.outfile, "w") as f:
            f.write(script(self.src))
            f.close()
        os.system(f"gcc -o {self.binfile} {self.outfile}")
        if not save:
            os.remove(self.outfile)

def main() -> None:
    findex:   int  = 1
    save_tmp: bool = False
    if argc <= 1:
        print("USAGE: escript <file>")
        print("Type --help for more info.")
        return
    if argv[1] in HELP_FLAGS:
        print(USAGE)
        return
    if argv[1] in SAVE_FLAGS:
        findex   = 2
        save_tmp = True
    escript: any = EScript(argv[findex])
    escript.compile(save=save_tmp)

if __name__ == "__main__":
    main()
