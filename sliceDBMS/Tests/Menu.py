import sys
import subprocess
from Controller import DBSlice
from Controller.SliceEnv import SliceEnv
from Controller.SliceField import SliceField
from Controller.SliceCondition import SliceCondition
from Controller.SliceQuery import SliceQuery

def _run():
    while True:
        print ("\nSlice DBMS Menu\n" + 
                "1. Create Database\n" +
                "2. Update Record\n"+
                "3. Add Record\n"+
                "4. Delete Record\n"+
                "5. Bulk Load\n"+
                "6. Display Join\n"+
                "7. Run Query\n"+
                "8. Report 1\n"+
                "9. Report 2\n"+
                "10. Exit\n")
        client_input = _getInput('Select')
        if(client_input == '1'):
            _createDatabase()
        elif(client_input == '2'):
            _updateRecord()
        elif(client_input == '3'):
            _addRecord()
        elif(client_input == '4'):
            _deleteRecord()
        elif(client_input == '5'):
            _bulkLoad()
        elif(client_input == '6'):
            _displayJoin()
        elif(client_input == '7'):
            _runQuery()
        elif(client_input == '8'):
            _report1()
        elif(client_input == '9'):
            _report2()
        elif(client_input == '10'):
            print "Application terminated - Goodbye!"
            sys.exit()
        else:
            print "Invalid input"

def _createDatabase():
    databaseName = _getInput('Enter Database Name')
    count = _processInteger('Enter Number of Fields')
    schemaElements = []
    i = 0
    while i < count:
        field_name = _getInput('Enter Field Name')
        if _checkIfAlreadyExists(field_name, schemaElements):
            print "Error: Field name already exits"
        else:
            while True:
                print ("\nChoose Field Type\n" +
                       "1. INT\n" + 
                       "2. DOUBLE\n" +
                       "3. STRING\n")
                client_input = _getInput('Select')
                if(client_input == '1'):
                    field_type = DBSlice.INT
                    break
                elif(client_input == '2'):
                    field_type = DBSlice.DOUBLE
                    break
                elif(client_input == '3'):
                    field_type = DBSlice.STRING
                    break
                else:
                    print "Error: Invalid input"
            schemaElements.append(SliceField(field_name, field_type))
            i = i + 1
    indexNotGood = True
    while indexNotGood:
        index = _getInput('Enter Index Name (Optional, INT Type)')
        if index == '':
            indexNotGood = False
        for field in schemaElements:
            if field.name == index and field.type == DBSlice.INT:
                indexNotGood = False
    if index == '':
        index = None
    sliceEnv = SliceEnv()
    sliceEnv.createDB(databaseName, schemaElements, index)