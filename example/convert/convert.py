# Author (Created): Roger "Equah" Hürzeler
# Date (Created): 12019.12.25 HE
# License: apache-2.0

import equah.sbsint

# [>] Main
if __name__ == "__main__":
    
    # [i] Start number.
    start_number = 420
    
    # [i] To SBSInt bytearray.
    sbsint_bytearray = bytearray()
    sbsint_bytearray_len = equah.sbsint.int_to_bytearray(start_number, sbsint_bytearray)
    
    # [i] Back to number.
    # [NOTE] Returns tuple (number_value, amount_bytes_read).
    end_number, end_number_len = equah.sbsint.list_to_int(sbsint_bytearray)
    
    # [i] Print conversion of number.
    print("{} -> {} -> {}".format(start_number, sbsint_bytearray, end_number))
    
    exit()
