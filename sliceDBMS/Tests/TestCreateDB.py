from Controller import DBSlice
from Controller.SliceEnv import SliceEnv
from Controller.SliceField import SliceField

if __name__ == '__main__':
    
    schemaElements = [SliceField("cust", DBSlice.INT),
                      SliceField("name", DBSlice.STRING),
                      SliceField("age", DBSlice.INT),
                      SliceField("phone", DBSlice.STRING),
                      SliceField("address", DBSlice.STRING)]
    
    sliceEnv = SliceEnv()
    sliceEnv.createDB("CustDB", schemaElements, "cust")