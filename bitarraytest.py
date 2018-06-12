from bitarray import bitarray
import pickle

a=bitarray(843908625)



with open("bin.bin","bw") as f:
    s=pickle.dump(a,f)
