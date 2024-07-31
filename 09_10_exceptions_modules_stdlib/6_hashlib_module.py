import hashlib

some_string = 'data to encrypt'

email1 = 'hennadii@example.com'
email2 = 'hennadii@example.com'

# Equal hash results
print(hashlib.md5(email1.encode()).hexdigest())
print(hashlib.md5(email2.encode()).hexdigest())

md5_string = hashlib.md5(some_string.encode())
print('MD5 hash: ', md5_string.hexdigest())

sha256_string = hashlib.sha256(some_string.encode())
print('SHA256 hash: ', sha256_string.hexdigest())
