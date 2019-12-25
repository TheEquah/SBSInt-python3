<!-- Author (Created): Roger "Equah" Hürzeler -->
<!-- Date (Created): 12019.12.25 HE -->
<!-- License: apache-2.0 -->

**SBSInt [Python 3]**
================================================================================

[SBSInt](https://github.com/TheEquah/SBSInt/) Python 3 implementation.

--------------------------------------------------------------------------------

# Architecture

Overview of the SBSInt architecture.

## SBSInt

An SBSInt are bytes added together, while the first and following is `0xFF`. As soon as a byte is not `0xFF`, it will be added to the number and finish reading there.

Example
```
[0x00, 0x00, 0x00] => 0
[0x0A, 0x00, 0x00] => 10
[0xFF, 0x00, 0x00] => 255
[0xFF, 0xA5, 0x00] => 420
```

--------------------------------------------------------------------------------

# Install

SBSInt provedes a [`/src/setup.py`](https://github.com/TheEquah/SBSInt-python3/blob/master/src/setup.py) script to install the package. To use this script, `cd` into the [`/src/`](https://github.com/TheEquah/SBSInt-python3/tree/master/src/) directory, and execute the script with `python3 ./setup.py install`.

--------------------------------------------------------------------------------

# Examples

This repository provides the following example uses for SBSInt.

## Convert

Example which simply converts numbers between Integer and SBSInt.

Directory: [`/example/convert`](https://github.com/TheEquah/SBSInt-python3/tree/master/example/convert/)

--------------------------------------------------------------------------------
