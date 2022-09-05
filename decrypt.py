from cryptography.fernet import Fernet
import os
import path

def load_key():
    file = open('key.key', 'rb')
    key_ = file.read()
    file.close()
    return key_


key = load_key()
fer = Fernet(key)
os.chdir(r"/var/www/html/sla/TestPython/example-app")

for root, dirs, files in os.walk('.'):
    for filename in files:
        filepath = os.path.join(root, filename)

        with open(filepath, 'rb') as f:
            data = f.read()

        with open(filepath, 'wb') as f:
            f.write(fer.decrypt(data))
            
print('done')