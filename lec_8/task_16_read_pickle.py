import pickle
import os

res = pickle.loads(b"cos\nsystem\n(S'echo Hello world!'\ntR.")
print(f'res = {res}')

os.system('echo Hello World!')
