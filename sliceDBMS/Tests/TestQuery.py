from Controller.SliceEnv import SliceEnv
from Controller.SliceDB import SliceDB
from Controller.SliceRecord import SliceRecord
from Controller.SliceCondition import SliceCondition
from Controller.SliceQuery import SliceQuery
from Controller import OPSlice

if __name__ == '__main__':
    
    sliceEnv = SliceEnv()
    custDB = sliceEnv.open("CustDB")
    
    columns = []
    columns.append('name')
    columns.append('age')
    
    condition = SliceCondition("name", OPSlice.EQ, "Marcia Vang")
    
    custQuery = SliceQuery(columns, "CustDB", condition)
    
    sliceRecords = custDB.query(custQuery)
    
    print "Customer Age"
    for record in sliceRecords:
        name = record.getString("name")
        age = record.getInt("age")
        print name + " " + age
    
    sliceEnv.close("CustDB")