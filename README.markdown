Basic implementation of functions to convert integers to roman numerals and back via roman() and unroman() respectively.

Roman Numerals used the summed value of letters to represent a number.

```	
Symbol	Value
I		1
V		5
X		10
L		50
C		100
D		500
M		1,000
```


Example output when running test cases through it:
```
	X : roman(X)   :  unroman(roman(x))
-------------------------------------------
   -5 : -V         :    -5
   -4 : -IV        :    -4
   -3 : -III       :    -3
   -2 : -II        :    -2
   -1 : -I         :    -1
    0 :            :     0
    1 : I          :     1
    2 : II         :     2
    3 : III        :     3
    4 : IV         :     4
    5 : V          :     5
    6 : VI         :     6
    7 : VII        :     7
    8 : IIX        :     8
    9 : IX         :     9
   10 : X          :    10
   11 : XI         :    11
   12 : XII        :    12
   13 : XIII       :    13
   14 : XIV        :    14
   15 : XV         :    15
   16 : XVI        :    16
   17 : XVII       :    17
   18 : XIIX       :    18
   19 : XIX        :    19
   81 : XXCI       :    81
  256 : CCLVI      :   256
  625 : DCXXV      :   625
 1296 : MCCXCVI    :  1296
 2401 : MMCDI      :  2401
 4096 : MMMMXCVI   :  4096
 6561 : MMMMMMDLXI :  6561
[Finished in 0.1s]
```