import hashlib

def md5_hasher(inputString):
	hashed = hashlib.md5()
	hashed.update(inputString)
	return hashed.hexdigest()
	
def sha1_hasher(inputString):
	hashed = hashlib.sha1()
	hashed.update(inputString)
	return hashed.hexdigest()
	
def sha256_hasher(inputString):
	hashed = hashlib.sha256()
	hashed.update(inputString)
	return hashed.hexdigest()
	
def sha512_hasher(inputString):
	hashed = hashlib.sha512()
	hashed.update(inputString)
	return hashed.hexdigest()

userInput = input("Enter String: ").encode("utf-8")
print("1 - MD5; 2 - SHA1; 3 - SHA256; 4 - SHA512")
userHasher = int(input("Choose Hashing Algorhitm (number only): "))

if userHasher == 1:
	output = md5_hasher(userInput)
	print("Output: ", output)
elif userHasher == 2:
	output = sha1_hasher(userInput)
	print("Output: ", output)
elif userHasher == 3:
	output = sha256_hasher(userInput)
	print("Output: ", output)
elif userHasher == 4:
	output = sha512_hasher(userInput)
	print("Output: ", output)
