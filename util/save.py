import pickle

def save(obj,file_path):
    with open(file_path+".pkl","wb") as outp:
        pickle.dump(obj,outp,pickle.HIGHEST_PROTOCOL)

def load(file_path):
    try:
        with open(file_path+".pkl","rb") as inp:
            return pickle.load(inp)
    except:
        return None