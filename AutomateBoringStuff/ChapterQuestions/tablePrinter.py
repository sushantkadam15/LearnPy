tableData = [['apples', 'oranges', 'cherries', 'banana'],
             ['Alice', 'Bob', 'Carol', 'David'],
             ['dogs', 'cats', 'moose', 'goose']]
tableDataLength = len(tableData)
newTableData = []
for i in tableData:
    tempData = i
    for i in tempData:
        newTableData.append(i)

newTableDataLength = len(newTableData)
print(newTableDataLength)
x = 0
while x != (newTableDataLength - 1):
    print(newTableData[x], newTableData[x+1], newTableData[x+2])
    if x+3 < newTableDataLength - 1:
        x+=3
    else:
        x=x
  