<<<<<<< HEAD
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
=======
from tkinter import *
import tkinter.messagebox
import hashlib


def md5_hash():
	hashStr = hashlib.md5()
	hashStr.update(inputString.get().encode("utf-8"))
	digest = hashStr.hexdigest()
	w = Text(root, height=2, width=50)
	w.insert(1.0, digest)
	w.grid(row=1, column=1, rowspan=4)
	w.configure(state="disabled")
	

def sha1_hash():
	hashStr = hashlib.sha1()
	hashStr.update(inputString.get().encode("utf-8"))
	digest = hashStr.hexdigest()
	w = Text(root, height=2, width=50)
	w.insert(1.0, digest)
	w.grid(row=1, column=1, rowspan=4)
	w.configure(state="disabled")

def sha256_hash():
	hashStr = hashlib.sha256()
	hashStr.update(inputString.get().encode("utf-8"))
	digest = hashStr.hexdigest()
	w = Text(root, height=2, width=50)
	w.insert(1.0, digest)
	w.grid(row=1, column=1, rowspan=4)
	w.configure(state="disabled")

def sha512_hash():
	hashStr = hashlib.sha512()
	hashStr.update(inputString.get().encode("utf-8"))
	digest = hashStr.hexdigest()
	w = Text(root, height=3, width=50)
	w.insert(1.0, digest)
	w.grid(row=1, column=1, rowspan=4)
	w.configure(state="disabled")

root = Tk()

Label(root, text="Input String:", padx=5).grid(row=0)

w = Text(root, height=2, width=50)
w.insert(1.0, "Your hash will be here")
w.grid(row=1, column=1, rowspan=4)
w.configure(state="disabled")

hash_md5_btn = Button(root, text="MD5", command=md5_hash)
hash_md5_btn.grid(row=2, column=0, sticky=E+W)

hash_sha1_btn = Button(root, text="SHA1", command=sha1_hash)
hash_sha1_btn.grid(row=3, column=0, sticky=E+W)

hash_sha256_btn = Button(root, text="SHA256", command=sha256_hash)
hash_sha256_btn.grid(row=4, column=0, sticky=E+W)

hash_sha256_btn = Button(root, text="SHA512", command=sha512_hash)
hash_sha256_btn.grid(row=5, column=0, sticky=E+W)

inputString = Entry(root)
inputString.grid(row=0, column=1, sticky=E+W)

root.title("Simple Hasher")

root.mainloop() 
>>>>>>> tkinter
