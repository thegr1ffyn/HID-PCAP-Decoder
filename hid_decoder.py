#!/usr/bin/python
# coding: utf-8
from __future__ import print_function
import sys, os

# Declare the dictionaries for lower and upper case mappings
lcasekey = {}
ucasekey = {}

# Mapping for normal keys (already provided in your original script)
lcasekey[4] = "a";           ucasekey[4] = "A"
lcasekey[5] = "b";           ucasekey[5] = "B"
lcasekey[6] = "c";           ucasekey[6] = "C"
lcasekey[7] = "d";           ucasekey[7] = "D"
lcasekey[8] = "e";           ucasekey[8] = "E"
lcasekey[9] = "f";           ucasekey[9] = "F"
lcasekey[10] = "g";          ucasekey[10] = "G"
lcasekey[11] = "h";          ucasekey[11] = "H"
lcasekey[12] = "i";          ucasekey[12] = "I"
lcasekey[13] = "j";          ucasekey[13] = "J"
lcasekey[14] = "k";          ucasekey[14] = "K"
lcasekey[15] = "l";          ucasekey[15] = "L"
lcasekey[16] = "m";          ucasekey[16] = "M"
lcasekey[17] = "n";          ucasekey[17] = "N"
lcasekey[18] = "o";          ucasekey[18] = "O"
lcasekey[19] = "p";          ucasekey[19] = "P"
lcasekey[20] = "q";          ucasekey[20] = "Q"
lcasekey[21] = "r";          ucasekey[21] = "R"
lcasekey[22] = "s";          ucasekey[22] = "S"
lcasekey[23] = "t";          ucasekey[23] = "T"
lcasekey[24] = "u";          ucasekey[24] = "U"
lcasekey[25] = "v";          ucasekey[25] = "V"
lcasekey[26] = "w";          ucasekey[26] = "W"
lcasekey[27] = "x";          ucasekey[27] = "X"
lcasekey[28] = "y";          ucasekey[28] = "Y"
lcasekey[29] = "z";          ucasekey[29] = "Z"
lcasekey[30] = "1";          ucasekey[30] = "!" 
lcasekey[31] = "2";          ucasekey[31] = "@"
lcasekey[32] = "3";          ucasekey[32] = "#"
lcasekey[33] = "4";          ucasekey[33] = "$"
lcasekey[34] = "5";          ucasekey[34] = "%"
lcasekey[35] = "6";          ucasekey[35] = "^"
lcasekey[36] = "7";          ucasekey[36] = "&"
lcasekey[37] = "8";          ucasekey[37] = "*"
lcasekey[38] = "9";          ucasekey[38] = "("
lcasekey[39] = "0";          ucasekey[39] = ")"
lcasekey[40] = "Enter";      ucasekey[40] = "Enter"
lcasekey[41] = "esc";        ucasekey[41] = "esc"
lcasekey[42] = "del";        ucasekey[42] = "del"
lcasekey[43] = "tab";        ucasekey[43] = "tab"
lcasekey[44] = "space";      ucasekey[44] = "space"
lcasekey[45] = "-";          ucasekey[45] = "_"
lcasekey[46] = "=";          ucasekey[46] = "+"
lcasekey[47] = "[";          ucasekey[47] = "{"
lcasekey[48] = "]";          ucasekey[48] = "}"
lcasekey[49] = "\\";         ucasekey[49] = "|"
lcasekey[50] = " ";          ucasekey[50] = " "
lcasekey[51] = ";";          ucasekey[51] = ":"
lcasekey[52] = "'";          ucasekey[52] = "\""
lcasekey[53] = "`";          ucasekey[53] = "~"
lcasekey[54] = ",";          ucasekey[54] = "<"
lcasekey[55] = ".";          ucasekey[55] = ">"
lcasekey[56] = "/";          ucasekey[56] = "?"
lcasekey[57] = "CapsLock";   ucasekey[57] = "CapsLock"
lcasekey[79] = "RightArrow"; ucasekey[79] = "RightArrow"
lcasekey[80] = "LeftArrow";  ucasekey[80] = "LeftArrow"

# Handle number pad keys for NUM LOCK ON (these key codes are different when NUM LOCK is enabled)
lcasekey[71] = "1";    ucasekey[71] = "1"   # Number pad 1
lcasekey[72] = "2";    ucasekey[72] = "2"   # Number pad 2
lcasekey[73] = "3";    ucasekey[73] = "3"   # Number pad 3
lcasekey[75] = "4";    ucasekey[75] = "4"   # Number pad 4
lcasekey[76] = "5";    ucasekey[76] = "5"   # Number pad 5
lcasekey[77] = "6";    ucasekey[77] = "6"   # Number pad 6
lcasekey[79] = "7";    ucasekey[79] = "7"   # Number pad 7
lcasekey[80] = "8";    ucasekey[80] = "8"   # Number pad 8
lcasekey[81] = "9";    ucasekey[81] = "9"   # Number pad 9
lcasekey[82] = "0";    ucasekey[82] = "0"   # Number pad 0

# Make sure filename to open has been provided
if len(sys.argv) == 2:
    keycodes = open(sys.argv[1])
    for line in keycodes:
        # Dump line to bytearray
        bytesArray = bytearray.fromhex(line.strip())
        # See if we have a key code
        val = int(bytesArray[2])
        if val > 3 and val < 100:
            # Check if Enter or Space should be printed with special handling
            if val == 40:  # Enter key
                print()  # Adds a new line for Enter
            elif val == 44:  # Space key
                print(" ", end='')  # Adds a space for Space
            # See if left shift or right shift was held down
            elif bytesArray[0] == 0x02 or bytesArray[0] == 0x20 :
                print(ucasekey.get(int(bytesArray[2]), "?"), end=''),  # Single line output
            else:
                print(lcasekey.get(int(bytesArray[2]), "?"), end=''),  # Single line output
else:
    print("USAGE: python %s [filename]" % os.path.basename(__file__))
