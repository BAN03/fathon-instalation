def fixer(filePath:str, toChange:str, fix:str):
     with open(filePath, "r+") as f:
          to_edit = f.read()
          edited = to_edit.replace(toChange, fix, 1)
          f.seek(0)
          f.truncate()
          f.write(edited)
     

with_error = [
     "h = np.ceil(len(scales)/3)",
     "cpdef multiFitFlucVec(self, np.ndarray[np.int_t, ndim=2, mode='c'] limitsList, float logBase=np.e, bint verbose=False):"
]
     
fixed = [
     "h = int(np.ceil(len(scales)/3))",
     "cpdef multiFitFlucVec(self, np.ndarray[np.int64_t, ndim=2, mode='c'] limitsList, float logBase=np.e, bint verbose=False):"
]

dirs = [
     "fathon/examples/ht_example.py",
     "fathon/fathon/dcca.pyx",
     "fathon/fathon/dfa.pyx"    
]

for i in range(len(dirs)):
     if i == 0:
          error = with_error[0]
          fix = fixed[0]
     else:
          error = with_error[1]
          fix = fixed[1]
     
     fixer(dirs[i], error, fix)

