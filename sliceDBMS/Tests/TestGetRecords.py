from Controller.SliceEnv import SliceEnv
from Controller.SliceDB import SliceDB
from Controller.SliceRecord import SliceRecord

if __name__ == '__main__':
    
    sliceEnv = SliceEnv()
    custDB = sliceEnv.open("CustDB")
    
    custRecord = custDB.get(298)
    
    if(custRecord):
        print "Name " + custRecord.getString("name")
        print "Age " + custRecord.getInt("age")
        print "Address " + custRecord.getString("address")
    
    sliceEnv.close("CustDB")