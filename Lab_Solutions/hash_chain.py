import hashlib

seed = 'ecsc'
challenge = 'c89aa2ffb9edcc6604005196b5f0e0e4'

hash1 = hashlib.md5(seed.encode()).hexdigest()
print(hash1)
print()
while hash1 != challenge:
    hash1 = hashlib.md5(hash1.encode()).hexdigest()
    print(hash1)
