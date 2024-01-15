"""
an implementation of asymmetric encryption
"""

import rsa

publicKey, privateKey = rsa.newkeys(512)

message = "hello, world"

encMessage = rsa.encrypt(message.encode(), publicKey)

print("original string: ", message)
print("encrypted string: ", encMessage)

decMessage = rsa.decrypt(encMessage, privateKey).decode()

print("decrypted string: ", decMessage)
