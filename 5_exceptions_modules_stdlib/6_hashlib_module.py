import hashlib

some_string = 'data to encrypt'

md5_string = hashlib.md5(some_string.encode())
print('MD5 hash: ', md5_string.hexdigest())

sha256_string = hashlib.sha256(some_string.encode())
print('SHA256 hash: ', sha256_string.hexdigest())
