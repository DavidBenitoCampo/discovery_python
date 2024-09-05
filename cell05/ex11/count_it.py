  #!/bin/python3

import sys

if(len(sys.argv)) == 1:
    print("None")
    exit(1)

if (len(sys.argv) != 1):
 for arg in sys.argv[1:]:
   a = arg
   print(f"{a} : {len(a)}")

    
