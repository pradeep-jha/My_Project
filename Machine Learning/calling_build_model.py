
import pickle
with open('model_pickle','rb') as f:
    mp=pickle.load(f)

print(mp.predict([[5000]]))