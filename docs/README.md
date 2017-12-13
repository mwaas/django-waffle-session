Sample CSV when importing data
###############################
feature,phone_number,feature__name
2,2547125817350,"ucl"
2,2547125817351,"ucl"
2,2547125817352,"ucl"

feature - Flag id as stored in the db
phone_number - MSISDN. Should start with country prefix
feaure__name - Name of the flag as stored in the db

Note
====
1. Creating of the flag is done on the DB
2. Data should be validated before being imported.
3. A good way to  check the expected data input is by exporting some data using the input type you
want to use. The input for import is the same as the output after an export.