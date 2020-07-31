from deepface import DeepFace
import pandas as pd

data = pd.read_csv('entrada.csv', dtype= str)

vetor = []
new_data = []
for item in data:
    new_data.append(item)
    vetor.append(['tests\dataset\\' + item + '_DOCUMENTO_1.jpg', 'tests\dataset\\' + item + '_SELFIE_1.jpg'])

result  = DeepFace.verify(vetor, enforce_detection = False)
df = pd.DataFrame(result).transpose()
df.insert(0, "id", new_data, True)
df.to_csv('saida.csv', index=False, header=False)