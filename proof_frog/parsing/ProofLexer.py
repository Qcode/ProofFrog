# Generated from proof_frog/antlr/Proof.g4 by ANTLR 4.13.1
from antlr4 import *
from io import StringIO
import sys
if sys.version_info[1] > 5:
    from typing import TextIO
else:
    from typing.io import TextIO


def serializedATN():
    return [
        4,0,68,462,6,-1,2,0,7,0,2,1,7,1,2,2,7,2,2,3,7,3,2,4,7,4,2,5,7,5,
        2,6,7,6,2,7,7,7,2,8,7,8,2,9,7,9,2,10,7,10,2,11,7,11,2,12,7,12,2,
        13,7,13,2,14,7,14,2,15,7,15,2,16,7,16,2,17,7,17,2,18,7,18,2,19,7,
        19,2,20,7,20,2,21,7,21,2,22,7,22,2,23,7,23,2,24,7,24,2,25,7,25,2,
        26,7,26,2,27,7,27,2,28,7,28,2,29,7,29,2,30,7,30,2,31,7,31,2,32,7,
        32,2,33,7,33,2,34,7,34,2,35,7,35,2,36,7,36,2,37,7,37,2,38,7,38,2,
        39,7,39,2,40,7,40,2,41,7,41,2,42,7,42,2,43,7,43,2,44,7,44,2,45,7,
        45,2,46,7,46,2,47,7,47,2,48,7,48,2,49,7,49,2,50,7,50,2,51,7,51,2,
        52,7,52,2,53,7,53,2,54,7,54,2,55,7,55,2,56,7,56,2,57,7,57,2,58,7,
        58,2,59,7,59,2,60,7,60,2,61,7,61,2,62,7,62,2,63,7,63,2,64,7,64,2,
        65,7,65,2,66,7,66,2,67,7,67,1,0,1,0,1,0,1,0,1,0,1,0,1,0,1,0,1,0,
        1,0,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,2,1,2,1,2,1,2,1,2,1,2,1,2,
        1,2,1,2,1,2,1,3,1,3,1,3,1,3,1,3,1,3,1,3,1,3,1,4,1,4,1,4,1,4,1,4,
        1,4,1,5,1,5,1,5,1,5,1,5,1,5,1,5,1,6,1,6,1,6,1,6,1,6,1,6,1,6,1,6,
        1,7,1,7,1,7,1,7,1,7,1,7,1,8,1,8,1,8,1,8,1,9,1,9,1,9,1,9,1,9,1,9,
        1,10,1,10,1,10,1,10,1,10,1,10,1,10,1,10,1,10,1,10,1,11,1,11,1,11,
        1,11,1,11,1,12,1,12,1,13,1,13,1,14,1,14,1,15,1,15,1,16,1,16,1,17,
        1,17,1,18,1,18,1,19,1,19,1,20,1,20,1,21,1,21,1,22,1,22,1,23,1,23,
        1,24,1,24,1,25,1,25,1,26,1,26,1,27,1,27,1,28,1,28,1,29,1,29,1,30,
        1,30,1,30,1,31,1,31,1,31,1,32,1,32,1,32,1,33,1,33,1,33,1,34,1,34,
        1,34,1,35,1,35,1,35,1,36,1,36,1,36,1,37,1,37,1,38,1,38,1,39,1,39,
        1,40,1,40,1,40,1,40,1,41,1,41,1,41,1,41,1,41,1,42,1,42,1,42,1,42,
        1,43,1,43,1,43,1,43,1,44,1,44,1,44,1,44,1,44,1,44,1,44,1,45,1,45,
        1,45,1,45,1,45,1,45,1,45,1,46,1,46,1,46,1,46,1,46,1,46,1,46,1,46,
        1,46,1,46,1,47,1,47,1,47,1,47,1,47,1,47,1,48,1,48,1,48,1,48,1,48,
        1,48,1,48,1,48,1,48,1,48,1,49,1,49,1,49,1,49,1,49,1,49,1,49,1,49,
        1,50,1,50,1,50,1,51,1,51,1,51,1,51,1,52,1,52,1,52,1,53,1,53,1,53,
        1,54,1,54,1,54,1,54,1,54,1,54,1,55,1,55,1,55,1,55,1,55,1,56,1,56,
        1,56,1,56,1,56,1,56,1,56,1,57,1,57,1,57,1,58,1,58,1,58,1,58,1,58,
        1,58,1,59,1,59,1,59,1,59,1,59,1,59,1,59,1,59,1,60,1,60,1,60,1,60,
        1,60,1,61,1,61,1,61,1,61,1,61,1,62,1,62,1,62,1,62,4,62,416,8,62,
        11,62,12,62,417,1,63,4,63,421,8,63,11,63,12,63,422,1,64,1,64,5,64,
        427,8,64,10,64,12,64,430,9,64,1,65,4,65,433,8,65,11,65,12,65,434,
        1,65,1,65,1,66,1,66,1,66,1,66,5,66,443,8,66,10,66,12,66,446,9,66,
        1,66,3,66,449,8,66,1,66,1,66,1,66,1,66,1,67,1,67,4,67,457,8,67,11,
        67,12,67,458,1,67,1,67,1,444,0,68,1,1,3,2,5,3,7,4,9,5,11,6,13,7,
        15,8,17,9,19,10,21,11,23,12,25,13,27,14,29,15,31,16,33,17,35,18,
        37,19,39,20,41,21,43,22,45,23,47,24,49,25,51,26,53,27,55,28,57,29,
        59,30,61,31,63,32,65,33,67,34,69,35,71,36,73,37,75,38,77,39,79,40,
        81,41,83,42,85,43,87,44,89,45,91,46,93,47,95,48,97,49,99,50,101,
        51,103,52,105,53,107,54,109,55,111,56,113,57,115,58,117,59,119,60,
        121,61,123,62,125,63,127,64,129,65,131,66,133,67,135,68,1,0,6,1,
        0,48,49,1,0,48,57,4,0,36,36,65,90,95,95,97,122,5,0,36,36,48,57,65,
        90,95,95,97,122,3,0,9,10,13,13,32,32,7,0,32,32,36,36,46,57,60,62,
        65,90,95,95,97,122,468,0,1,1,0,0,0,0,3,1,0,0,0,0,5,1,0,0,0,0,7,1,
        0,0,0,0,9,1,0,0,0,0,11,1,0,0,0,0,13,1,0,0,0,0,15,1,0,0,0,0,17,1,
        0,0,0,0,19,1,0,0,0,0,21,1,0,0,0,0,23,1,0,0,0,0,25,1,0,0,0,0,27,1,
        0,0,0,0,29,1,0,0,0,0,31,1,0,0,0,0,33,1,0,0,0,0,35,1,0,0,0,0,37,1,
        0,0,0,0,39,1,0,0,0,0,41,1,0,0,0,0,43,1,0,0,0,0,45,1,0,0,0,0,47,1,
        0,0,0,0,49,1,0,0,0,0,51,1,0,0,0,0,53,1,0,0,0,0,55,1,0,0,0,0,57,1,
        0,0,0,0,59,1,0,0,0,0,61,1,0,0,0,0,63,1,0,0,0,0,65,1,0,0,0,0,67,1,
        0,0,0,0,69,1,0,0,0,0,71,1,0,0,0,0,73,1,0,0,0,0,75,1,0,0,0,0,77,1,
        0,0,0,0,79,1,0,0,0,0,81,1,0,0,0,0,83,1,0,0,0,0,85,1,0,0,0,0,87,1,
        0,0,0,0,89,1,0,0,0,0,91,1,0,0,0,0,93,1,0,0,0,0,95,1,0,0,0,0,97,1,
        0,0,0,0,99,1,0,0,0,0,101,1,0,0,0,0,103,1,0,0,0,0,105,1,0,0,0,0,107,
        1,0,0,0,0,109,1,0,0,0,0,111,1,0,0,0,0,113,1,0,0,0,0,115,1,0,0,0,
        0,117,1,0,0,0,0,119,1,0,0,0,0,121,1,0,0,0,0,123,1,0,0,0,0,125,1,
        0,0,0,0,127,1,0,0,0,0,129,1,0,0,0,0,131,1,0,0,0,0,133,1,0,0,0,0,
        135,1,0,0,0,1,137,1,0,0,0,3,147,1,0,0,0,5,155,1,0,0,0,7,165,1,0,
        0,0,9,173,1,0,0,0,11,179,1,0,0,0,13,186,1,0,0,0,15,194,1,0,0,0,17,
        200,1,0,0,0,19,204,1,0,0,0,21,210,1,0,0,0,23,220,1,0,0,0,25,225,
        1,0,0,0,27,227,1,0,0,0,29,229,1,0,0,0,31,231,1,0,0,0,33,233,1,0,
        0,0,35,235,1,0,0,0,37,237,1,0,0,0,39,239,1,0,0,0,41,241,1,0,0,0,
        43,243,1,0,0,0,45,245,1,0,0,0,47,247,1,0,0,0,49,249,1,0,0,0,51,251,
        1,0,0,0,53,253,1,0,0,0,55,255,1,0,0,0,57,257,1,0,0,0,59,259,1,0,
        0,0,61,261,1,0,0,0,63,264,1,0,0,0,65,267,1,0,0,0,67,270,1,0,0,0,
        69,273,1,0,0,0,71,276,1,0,0,0,73,279,1,0,0,0,75,282,1,0,0,0,77,284,
        1,0,0,0,79,286,1,0,0,0,81,288,1,0,0,0,83,292,1,0,0,0,85,297,1,0,
        0,0,87,301,1,0,0,0,89,305,1,0,0,0,91,312,1,0,0,0,93,319,1,0,0,0,
        95,329,1,0,0,0,97,335,1,0,0,0,99,345,1,0,0,0,101,353,1,0,0,0,103,
        356,1,0,0,0,105,360,1,0,0,0,107,363,1,0,0,0,109,366,1,0,0,0,111,
        372,1,0,0,0,113,377,1,0,0,0,115,384,1,0,0,0,117,387,1,0,0,0,119,
        393,1,0,0,0,121,401,1,0,0,0,123,406,1,0,0,0,125,411,1,0,0,0,127,
        420,1,0,0,0,129,424,1,0,0,0,131,432,1,0,0,0,133,438,1,0,0,0,135,
        454,1,0,0,0,137,138,5,82,0,0,138,139,5,101,0,0,139,140,5,100,0,0,
        140,141,5,117,0,0,141,142,5,99,0,0,142,143,5,116,0,0,143,144,5,105,
        0,0,144,145,5,111,0,0,145,146,5,110,0,0,146,2,1,0,0,0,147,148,5,
        97,0,0,148,149,5,103,0,0,149,150,5,97,0,0,150,151,5,105,0,0,151,
        152,5,110,0,0,152,153,5,115,0,0,153,154,5,116,0,0,154,4,1,0,0,0,
        155,156,5,65,0,0,156,157,5,100,0,0,157,158,5,118,0,0,158,159,5,101,
        0,0,159,160,5,114,0,0,160,161,5,115,0,0,161,162,5,97,0,0,162,163,
        5,114,0,0,163,164,5,121,0,0,164,6,1,0,0,0,165,166,5,99,0,0,166,167,
        5,111,0,0,167,168,5,109,0,0,168,169,5,112,0,0,169,170,5,111,0,0,
        170,171,5,115,0,0,171,172,5,101,0,0,172,8,1,0,0,0,173,174,5,112,
        0,0,174,175,5,114,0,0,175,176,5,111,0,0,176,177,5,111,0,0,177,178,
        5,102,0,0,178,10,1,0,0,0,179,180,5,97,0,0,180,181,5,115,0,0,181,
        182,5,115,0,0,182,183,5,117,0,0,183,184,5,109,0,0,184,185,5,101,
        0,0,185,12,1,0,0,0,186,187,5,116,0,0,187,188,5,104,0,0,188,189,5,
        101,0,0,189,190,5,111,0,0,190,191,5,114,0,0,191,192,5,101,0,0,192,
        193,5,109,0,0,193,14,1,0,0,0,194,195,5,103,0,0,195,196,5,97,0,0,
        196,197,5,109,0,0,197,198,5,101,0,0,198,199,5,115,0,0,199,16,1,0,
        0,0,200,201,5,108,0,0,201,202,5,101,0,0,202,203,5,116,0,0,203,18,
        1,0,0,0,204,205,5,99,0,0,205,206,5,97,0,0,206,207,5,108,0,0,207,
        208,5,108,0,0,208,209,5,115,0,0,209,20,1,0,0,0,210,211,5,105,0,0,
        211,212,5,110,0,0,212,213,5,100,0,0,213,214,5,117,0,0,214,215,5,
        99,0,0,215,216,5,116,0,0,216,217,5,105,0,0,217,218,5,111,0,0,218,
        219,5,110,0,0,219,22,1,0,0,0,220,221,5,102,0,0,221,222,5,114,0,0,
        222,223,5,111,0,0,223,224,5,109,0,0,224,24,1,0,0,0,225,226,5,123,
        0,0,226,26,1,0,0,0,227,228,5,125,0,0,228,28,1,0,0,0,229,230,5,91,
        0,0,230,30,1,0,0,0,231,232,5,93,0,0,232,32,1,0,0,0,233,234,5,40,
        0,0,234,34,1,0,0,0,235,236,5,41,0,0,236,36,1,0,0,0,237,238,5,60,
        0,0,238,38,1,0,0,0,239,240,5,62,0,0,240,40,1,0,0,0,241,242,5,59,
        0,0,242,42,1,0,0,0,243,244,5,58,0,0,244,44,1,0,0,0,245,246,5,44,
        0,0,246,46,1,0,0,0,247,248,5,46,0,0,248,48,1,0,0,0,249,250,5,42,
        0,0,250,50,1,0,0,0,251,252,5,61,0,0,252,52,1,0,0,0,253,254,5,43,
        0,0,254,54,1,0,0,0,255,256,5,45,0,0,256,56,1,0,0,0,257,258,5,47,
        0,0,258,58,1,0,0,0,259,260,5,63,0,0,260,60,1,0,0,0,261,262,5,61,
        0,0,262,263,5,61,0,0,263,62,1,0,0,0,264,265,5,33,0,0,265,266,5,61,
        0,0,266,64,1,0,0,0,267,268,5,62,0,0,268,269,5,61,0,0,269,66,1,0,
        0,0,270,271,5,60,0,0,271,272,5,61,0,0,272,68,1,0,0,0,273,274,5,124,
        0,0,274,275,5,124,0,0,275,70,1,0,0,0,276,277,5,60,0,0,277,278,5,
        45,0,0,278,72,1,0,0,0,279,280,5,38,0,0,280,281,5,38,0,0,281,74,1,
        0,0,0,282,283,5,92,0,0,283,76,1,0,0,0,284,285,5,33,0,0,285,78,1,
        0,0,0,286,287,5,124,0,0,287,80,1,0,0,0,288,289,5,83,0,0,289,290,
        5,101,0,0,290,291,5,116,0,0,291,82,1,0,0,0,292,293,5,66,0,0,293,
        294,5,111,0,0,294,295,5,111,0,0,295,296,5,108,0,0,296,84,1,0,0,0,
        297,298,5,73,0,0,298,299,5,110,0,0,299,300,5,116,0,0,300,86,1,0,
        0,0,301,302,5,77,0,0,302,303,5,97,0,0,303,304,5,112,0,0,304,88,1,
        0,0,0,305,306,5,114,0,0,306,307,5,101,0,0,307,308,5,116,0,0,308,
        309,5,117,0,0,309,310,5,114,0,0,310,311,5,110,0,0,311,90,1,0,0,0,
        312,313,5,105,0,0,313,314,5,109,0,0,314,315,5,112,0,0,315,316,5,
        111,0,0,316,317,5,114,0,0,317,318,5,116,0,0,318,92,1,0,0,0,319,320,
        5,66,0,0,320,321,5,105,0,0,321,322,5,116,0,0,322,323,5,83,0,0,323,
        324,5,116,0,0,324,325,5,114,0,0,325,326,5,105,0,0,326,327,5,110,
        0,0,327,328,5,103,0,0,328,94,1,0,0,0,329,330,5,65,0,0,330,331,5,
        114,0,0,331,332,5,114,0,0,332,333,5,97,0,0,333,334,5,121,0,0,334,
        96,1,0,0,0,335,336,5,80,0,0,336,337,5,114,0,0,337,338,5,105,0,0,
        338,339,5,109,0,0,339,340,5,105,0,0,340,341,5,116,0,0,341,342,5,
        105,0,0,342,343,5,118,0,0,343,344,5,101,0,0,344,98,1,0,0,0,345,346,
        5,115,0,0,346,347,5,117,0,0,347,348,5,98,0,0,348,349,5,115,0,0,349,
        350,5,101,0,0,350,351,5,116,0,0,351,352,5,115,0,0,352,100,1,0,0,
        0,353,354,5,105,0,0,354,355,5,102,0,0,355,102,1,0,0,0,356,357,5,
        102,0,0,357,358,5,111,0,0,358,359,5,114,0,0,359,104,1,0,0,0,360,
        361,5,116,0,0,361,362,5,111,0,0,362,106,1,0,0,0,363,364,5,105,0,
        0,364,365,5,110,0,0,365,108,1,0,0,0,366,367,5,117,0,0,367,368,5,
        110,0,0,368,369,5,105,0,0,369,370,5,111,0,0,370,371,5,110,0,0,371,
        110,1,0,0,0,372,373,5,71,0,0,373,374,5,97,0,0,374,375,5,109,0,0,
        375,376,5,101,0,0,376,112,1,0,0,0,377,378,5,101,0,0,378,379,5,120,
        0,0,379,380,5,112,0,0,380,381,5,111,0,0,381,382,5,114,0,0,382,383,
        5,116,0,0,383,114,1,0,0,0,384,385,5,97,0,0,385,386,5,115,0,0,386,
        116,1,0,0,0,387,388,5,80,0,0,388,389,5,104,0,0,389,390,5,97,0,0,
        390,391,5,115,0,0,391,392,5,101,0,0,392,118,1,0,0,0,393,394,5,111,
        0,0,394,395,5,114,0,0,395,396,5,97,0,0,396,397,5,99,0,0,397,398,
        5,108,0,0,398,399,5,101,0,0,399,400,5,115,0,0,400,120,1,0,0,0,401,
        402,5,101,0,0,402,403,5,108,0,0,403,404,5,115,0,0,404,405,5,101,
        0,0,405,122,1,0,0,0,406,407,5,78,0,0,407,408,5,111,0,0,408,409,5,
        110,0,0,409,410,5,101,0,0,410,124,1,0,0,0,411,412,5,48,0,0,412,413,
        5,98,0,0,413,415,1,0,0,0,414,416,7,0,0,0,415,414,1,0,0,0,416,417,
        1,0,0,0,417,415,1,0,0,0,417,418,1,0,0,0,418,126,1,0,0,0,419,421,
        7,1,0,0,420,419,1,0,0,0,421,422,1,0,0,0,422,420,1,0,0,0,422,423,
        1,0,0,0,423,128,1,0,0,0,424,428,7,2,0,0,425,427,7,3,0,0,426,425,
        1,0,0,0,427,430,1,0,0,0,428,426,1,0,0,0,428,429,1,0,0,0,429,130,
        1,0,0,0,430,428,1,0,0,0,431,433,7,4,0,0,432,431,1,0,0,0,433,434,
        1,0,0,0,434,432,1,0,0,0,434,435,1,0,0,0,435,436,1,0,0,0,436,437,
        6,65,0,0,437,132,1,0,0,0,438,439,5,47,0,0,439,440,5,47,0,0,440,444,
        1,0,0,0,441,443,9,0,0,0,442,441,1,0,0,0,443,446,1,0,0,0,444,445,
        1,0,0,0,444,442,1,0,0,0,445,448,1,0,0,0,446,444,1,0,0,0,447,449,
        5,13,0,0,448,447,1,0,0,0,448,449,1,0,0,0,449,450,1,0,0,0,450,451,
        5,10,0,0,451,452,1,0,0,0,452,453,6,66,0,0,453,134,1,0,0,0,454,456,
        5,39,0,0,455,457,7,5,0,0,456,455,1,0,0,0,457,458,1,0,0,0,458,456,
        1,0,0,0,458,459,1,0,0,0,459,460,1,0,0,0,460,461,5,39,0,0,461,136,
        1,0,0,0,8,0,417,422,428,434,444,448,458,1,6,0,0
    ]

class ProofLexer(Lexer):

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    REDUCTION = 1
    AGAINST = 2
    ADVERSARY = 3
    COMPOSE = 4
    PROOF = 5
    ASSUME = 6
    THEOREM = 7
    GAMES = 8
    LET = 9
    CALLS = 10
    INDUCTION = 11
    FROM = 12
    L_CURLY = 13
    R_CURLY = 14
    L_SQUARE = 15
    R_SQUARE = 16
    L_PAREN = 17
    R_PAREN = 18
    L_ANGLE = 19
    R_ANGLE = 20
    SEMI = 21
    COLON = 22
    COMMA = 23
    PERIOD = 24
    TIMES = 25
    EQUALS = 26
    PLUS = 27
    SUBTRACT = 28
    DIVIDE = 29
    QUESTION = 30
    EQUALSCOMPARE = 31
    NOTEQUALS = 32
    GEQ = 33
    LEQ = 34
    OR = 35
    SAMPLES = 36
    AND = 37
    BACKSLASH = 38
    NOT = 39
    VBAR = 40
    SET = 41
    BOOL = 42
    INTTYPE = 43
    MAP = 44
    RETURN = 45
    IMPORT = 46
    BITSTRING = 47
    ARRAY = 48
    PRIMITIVE = 49
    SUBSETS = 50
    IF = 51
    FOR = 52
    TO = 53
    IN = 54
    UNION = 55
    GAME = 56
    EXPORT = 57
    AS = 58
    PHASE = 59
    ORACLES = 60
    ELSE = 61
    NONE = 62
    BINARYNUM = 63
    INT = 64
    ID = 65
    WS = 66
    LINE_COMMENT = 67
    FILESTRING = 68

    channelNames = [ u"DEFAULT_TOKEN_CHANNEL", u"HIDDEN" ]

    modeNames = [ "DEFAULT_MODE" ]

    literalNames = [ "<INVALID>",
            "'Reduction'", "'against'", "'Adversary'", "'compose'", "'proof'", 
            "'assume'", "'theorem'", "'games'", "'let'", "'calls'", "'induction'", 
            "'from'", "'{'", "'}'", "'['", "']'", "'('", "')'", "'<'", "'>'", 
            "';'", "':'", "','", "'.'", "'*'", "'='", "'+'", "'-'", "'/'", 
            "'?'", "'=='", "'!='", "'>='", "'<='", "'||'", "'<-'", "'&&'", 
            "'\\'", "'!'", "'|'", "'Set'", "'Bool'", "'Int'", "'Map'", "'return'", 
            "'import'", "'BitString'", "'Array'", "'Primitive'", "'subsets'", 
            "'if'", "'for'", "'to'", "'in'", "'union'", "'Game'", "'export'", 
            "'as'", "'Phase'", "'oracles'", "'else'", "'None'" ]

    symbolicNames = [ "<INVALID>",
            "REDUCTION", "AGAINST", "ADVERSARY", "COMPOSE", "PROOF", "ASSUME", 
            "THEOREM", "GAMES", "LET", "CALLS", "INDUCTION", "FROM", "L_CURLY", 
            "R_CURLY", "L_SQUARE", "R_SQUARE", "L_PAREN", "R_PAREN", "L_ANGLE", 
            "R_ANGLE", "SEMI", "COLON", "COMMA", "PERIOD", "TIMES", "EQUALS", 
            "PLUS", "SUBTRACT", "DIVIDE", "QUESTION", "EQUALSCOMPARE", "NOTEQUALS", 
            "GEQ", "LEQ", "OR", "SAMPLES", "AND", "BACKSLASH", "NOT", "VBAR", 
            "SET", "BOOL", "INTTYPE", "MAP", "RETURN", "IMPORT", "BITSTRING", 
            "ARRAY", "PRIMITIVE", "SUBSETS", "IF", "FOR", "TO", "IN", "UNION", 
            "GAME", "EXPORT", "AS", "PHASE", "ORACLES", "ELSE", "NONE", 
            "BINARYNUM", "INT", "ID", "WS", "LINE_COMMENT", "FILESTRING" ]

    ruleNames = [ "REDUCTION", "AGAINST", "ADVERSARY", "COMPOSE", "PROOF", 
                  "ASSUME", "THEOREM", "GAMES", "LET", "CALLS", "INDUCTION", 
                  "FROM", "L_CURLY", "R_CURLY", "L_SQUARE", "R_SQUARE", 
                  "L_PAREN", "R_PAREN", "L_ANGLE", "R_ANGLE", "SEMI", "COLON", 
                  "COMMA", "PERIOD", "TIMES", "EQUALS", "PLUS", "SUBTRACT", 
                  "DIVIDE", "QUESTION", "EQUALSCOMPARE", "NOTEQUALS", "GEQ", 
                  "LEQ", "OR", "SAMPLES", "AND", "BACKSLASH", "NOT", "VBAR", 
                  "SET", "BOOL", "INTTYPE", "MAP", "RETURN", "IMPORT", "BITSTRING", 
                  "ARRAY", "PRIMITIVE", "SUBSETS", "IF", "FOR", "TO", "IN", 
                  "UNION", "GAME", "EXPORT", "AS", "PHASE", "ORACLES", "ELSE", 
                  "NONE", "BINARYNUM", "INT", "ID", "WS", "LINE_COMMENT", 
                  "FILESTRING" ]

    grammarFileName = "Proof.g4"

    def __init__(self, input=None, output:TextIO = sys.stdout):
        super().__init__(input, output)
        self.checkVersion("4.13.1")
        self._interp = LexerATNSimulator(self, self.atn, self.decisionsToDFA, PredictionContextCache())
        self._actions = None
        self._predicates = None


