from Controller.SliceEnv import SliceEnv
from Controller.SliceDB import SliceDB
from Controller.SliceRecord import SliceRecord

if __name__ == '__main__':
    
    sliceEnv = SliceEnv()
    custDB = sliceEnv.open("CustDB")
    
    custRecord = custDB.createRecord()
    
    custRecord.setString("name", "Joe Smith")
    custRecord.setInt("age", 43)
    custRecord.setString("address", "Montreal")
    
    custDB.set(custRecord)
    
    sliceEnv.close("CustDB")