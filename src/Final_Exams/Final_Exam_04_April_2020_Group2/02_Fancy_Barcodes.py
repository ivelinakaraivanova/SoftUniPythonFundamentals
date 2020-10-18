import re

barcode_pattern = r'(@#+)([A-Z][A-Za-z0-9]{4,}[A-Z])(@#+)'
n = int(input())

for _ in range(n):
    text = input()
    barcodes = re.finditer(barcode_pattern, text)
    is_barcode = False
    for item in barcodes:
        barcode = item[2]
        digits_str = ''
        for s in barcode:
            if s.isdigit():
                digits_str += s
        if digits_str == '':
            print("Product group: 00")
        else:
            print(f"Product group: {digits_str}")
        is_barcode = True
    if not is_barcode:
        print("Invalid barcode")