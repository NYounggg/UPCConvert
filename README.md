# A simple Python script to support retail inventory counting.
This script converts the shrunken UPC-E (8 digit) barcodes to the expanded UPC-A (11 digits with check digit removed) barcodes.

## Input
Input file should be a .csv with headers "UPC-E" and "Quantity".  When running the program, a Windows Explorer instance will open.  Select your input .csv file here.

Example of input data below:

![csv](https://github.com/NYounggg/UPCConvert/assets/71022019/2cc746e8-1f12-48d7-9b74-514a3d8ee1f9)


The data under "UPC-E" can be either UPC-E codes or UPC-A codes.  UPC-A codes will simply be ignored, and UPC-E will be expanded to UPC-A.  


## Output
This program generates an output file, "out.csv", that will contain the UPC-A codes with check digit removed (11 digits) 

## References
Conversion algorithm can be found at [barcodefaq](https://www.barcodefaq.com/barcode-properties/symbologies/upc-e/)
