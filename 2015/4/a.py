import hashlib

secret = "bgvyzdsv"
secret = "abcdef"
secret = "bgvyzdsv"


for i in range(0, 9999999999999):
    all_bin = secret + str(i)
    res = hashlib.md5(all_bin.encode())
    if res.hexdigest().startswith("00000"):
        print(i)
        break

for i in range(0, 9999999999999):
    all_bin = secret + str(i)
    res = hashlib.md5(all_bin.encode())
    if res.hexdigest().startswith("000000"):
        print(i)
        break

