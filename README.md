# genQR

PURPOSE:

To learn. if you decide to use this, do not trust the addresses/QR created are correct. PLEASE VERIFY. I'm a new to this and
just wanted to make something.


SETUP:

genQR.py, addresses.txt, and usedAddresses.txt must all be in the same directory
usedAddresses.txt must exist and be completely empty.

this script requires the pyqrcode library to generate the QRs.
you can find the library here: https://github.com/mnooner256/pyqrcode

RUNNING:

-script will show user the SHA256 hash of address.txt. user should make note of this. it should not change.

-script will retrieve address from address.txt and compare to addresses in usedAddresses.txt

-if the address retrieved does not match any address in usedAddresses.txt, 
user will be prompted for a discription for the address and a QR for the address will be displayed.

-if the address retrieved does match an address in usedAddresses.txt,
script will move to the next availible address in addresses.txt.

-retrieved address as well as discription will be apended to usedAddresses.txt
user should not need to edit usedAddresses.txt directly.

-script will display only one address when it is ran. 


if you think this is cool, here's a tipping address. =)

bc1q8gpcj8rjn2f2h7ljd8cv8k887dfqdtlqe59f2t

