# Author (Created): Roger "Equah" Hürzeler
# Author (Modified): Roger "Equah" Hürzeler
# Date (Created): 12019.12.25 HE
# Date (Modified): 12020.03.22 HE
# License: apache-2.0


# [>] List To Integer
# [i] Converts a list of SBSInt bytes to an integer.
# [P] {list|bytes|bytearray} bl => List of SBSInt bytes.
# [R] {(int, int)} => Tuple of SBSInt value and amount of bytes read.
def list_to_int(bl) :
    
    size = 1
    sbsint = 0
    
    next_byte = bl[0]
    while next_byte == 0xFF :
        sbsint += 0xFF
        next_byte = bl[size]
        size += 1
        pass
    
    sbsint += next_byte
    
    return (sbsint, size)

# [>] Single Bytes To Integer
# [i] Uses a given function to read single bytes of an SBSInt and converts it to an integer.
# [P] {function () > int} fn_r => Function returning the next byte.
# [R] {(int, int)} => Tuple of SBSInt value.
def sbytes_to_int(fn_r) :
	
	size = 1
	sbsint = 0
	next_byte = fn_r()
	while next_byte == 0xFF :
		sbsint += 0xFF
		size += 1
		pass
	sbsint += next_byte
	
	return (sbsint, size)

# [>] Integer To Bytearray
# [i] Converts an integer to SBSInt bytearray.
# [P] {int} i => Integer to convert to SBSInt.
# [P] {bytearray} buff => Bytearray to which SBSInt will be written.
# [R] {int} => Amount of written bytes to represent SBSInt.
def int_to_bytearray(i, buff) :
    
    size = 1
    
    while i >= 0xFF :
        buff.append(0xFF)
        i -= 0xFF
        size += 1
        pass
    
    buff.append(i)
    
    return size

# [>] Integer To Single Bytes
# [i] Converts given integer to SBSInt andwrites it with given function in single bytes.
# [P] {int} i => Integer to convert to SBSInt bytes.
# [P] {function (int)} => Function to write a single byte.
# [R] {int} => Amount of written bytes.
def int_to_sbytes(i, fn_w) :
	
	size = 1
	
	while i >= 0xFF :
		fn_w(0xFF)
		i -= 0xFF
		size += 1
		pass
	
	fn_w(i)
	
	return size
