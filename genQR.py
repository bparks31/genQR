# requires hashlib to generate the hash of addresses.txt
import hashlib
#uses pyqrcode to generate QR codes.
import pyqrcode
import os


#Function that generates a sha256 hash of the "addresses.txt" file returns text to be displayed
def checkHashOfAddressesFile():
    sha256_hash = hashlib.sha256()
    with open("addresses.txt", "rb") as addressFile:
        for byte_block in iter(lambda: addressFile.read(4096),b""):
            sha256_hash.update(byte_block)
        return "THIS IS THE SHA256 HASH OF YOUR addresses.txt FILE.\n\n" + sha256_hash.hexdigest() + "\n\nMAKE NOTE OF IT. IF IT HAS CHANGED, addresses.txt HAS BEEN ALTERED! \n"

# Creates an list of every used address
def loadUsedAddresses():
    usedAddressesArray = []
    with open("usedAddresses.txt") as usedAddressesFile:
        for i in usedAddressesFile:
            usedAddressesArray.append(i.split(None, 1)[0])
        return usedAddressesArray

#Checks if the line in the addresses.txt file is a valid address
def checkIfAddress(address):
    #if legacy address
    if address.startswith("1") == True:
        return True
    #if native segwit address
    elif address.startswith("bc1") == True:
        return True
    # if P2SH address
    elif address.startswith("3") == True:
        return True
    else:
        return False

#Prints the new address with QR
def qrGen(address):
    print(address)
    print(pyqrcode.create(address).terminal())

#User input for address discription
def discriptionForAddress(address):
    discription = "DISCRIPTION: " + input("Discription for: {} :".format(address)) 
    return discription + "\n"

#compares address to listOfUsedAddresses to see if the address is in the usedAddresses.txt file
def checkIfAddressIsUsed(address,listOfUsedAddresses):
    for usedAddress in listOfUsedAddresses:
        if address == usedAddress:
            return True
    else:
        return False

def findNewAddress():
    #pulls out the address from the addresses.txt file
  with open("addresses.txt") as addressFile:
        for line in addressFile:
            lists = [x.strip() for x in line.split(',')]
            address = lists[1]
            address = address[1:-1]
            address = address.strip()
            if checkIfAddress(address) == True:
                    #if address has not been used, qrGen() prints the address and shows QR
                if checkIfAddressIsUsed(address, loadUsedAddresses()) == False:
                    qrGen(address)
                    with open("usedAddresses.txt", "a") as usedAddressesFile:
                        # user is prompted for discription. 
                        # if no discription is entered, and terminal is closed, address will not be marked as used.
                        addressDiscription = discriptionForAddress(address)
                        usedAddressesFile.write(address)
                        usedAddressesFile.write("\t\t" + addressDiscription)
                        return address
        else:
            print ("ALL OF THE ADDRESSES HAVE BEEN USED \n")

#if running on windows replace "clear" with "cls"
os.system("clear")
print (checkHashOfAddressesFile())
findNewAddress()