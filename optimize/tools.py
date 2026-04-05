import pandas as pd
import fnmatch
from decimal import Decimal

PACKAGES = ["0201", "0402", "0603", "0805", "1206", "1210", "2512"]
DIELECTRICS = ["NP0", "NPO", "X7R", "X5R"]
TOLERANCE_SYMB = {
    "B": 0.1,
    "C": 0.25,
    "D": 0.5,
    "F": 1,
    "G": 2,
    "J": 5,
    "K": 10,
    "M": 20,
    "S": 50
}
SUFFIXIES = {
    "f": 10 ** (-15),
    "p": 10 ** (-12),
    "n": 10 ** (-9),
    "u": 10 ** (-6),
    "m": 10 ** (-3),
    "K": 10 ** 3,
    "k": 10 ** 3,
    "M": 10 ** 6,
    "R": 1
}

def is_number(s: str) -> bool:
    try:
        float(s)
        return True
    except ValueError:
        return False

def concatRow(row, table):
    

    try:
        for index, roww in table.iterrows():
            
            for index, value in roww.items():
                row[index] = value
    except:
        pass
        # for column in roww.columns().values():
        #     print(roww[column])
    return row

def reIndexBySubsequence(table, subsequence):

    columns = table.columns.array
    columnSubsequence = []

    for columnName in subsequence:
        if columnName in columns:
            columnSubsequence.append(columnName)

    for columnName in columns:
        if columnName not in columnSubsequence:
            columnSubsequence.append(columnName)

    return  table[columnSubsequence]

    

def getTableByRequest(table, request):

    output_table = pd.DataFrame()

    for index, row in table.iterrows():
        if fnmatch.fnmatch(row['pn'], f"*{request}*"):
            #new_row = row
            #print(row)

            new_row = concatRow(row, splittedLine(row['pn']))
            
            #print(new_row)
            #new_row = splittedLine(row['pn'])
            output_table = pd.concat([output_table, new_row], axis=1, ignore_index=True)

    #print(output_table)
    output_table = output_table.transpose()

    output_table = output_table.rename(columns={'pn': 'Номенклатура 1С', 'count': 'Количество'})

    rightColumnSubsequence = ["Количество", "Номенклатура 1С", "Номинал", "Корпус", "Напряжение", "Диэлектрик", "Точность"]
    output_table = reIndexBySubsequence(output_table, rightColumnSubsequence)

    return output_table

def getFloat(strValue):

    for suffix in SUFFIXIES.keys():
        if suffix in strValue:
            index = strValue.find(suffix)
            if index != len(strValue) - 1:
                if is_number(strValue[index+1]):
                    strValue = strValue.replace(suffix, ".")
                    if is_number(strValue):
                        return float(strValue) * SUFFIXIES[suffix]
                    else:
                        return -1
                if is_number(strValue[:index]):
                    return float(strValue[:index]) * SUFFIXIES[suffix]
                else:
                    return -1
            else:
                if is_number(strValue[:index]):
                    return float(strValue[:index]) * SUFFIXIES[suffix]
                else:
                    return -1
    return -2

def splittedLine(partNumber, stripSymbol = "-"):
    
    package = ""
    dielectric = ""
    voltage = -1
    tolerance = -1
    value = -1
    
    stripLine = partNumber.split(stripSymbol)
    #print(stripLine)

    componentType = stripLine[0]
    try:
        match componentType:
            case "C":
                if stripLine[1] in PACKAGES:
                    package = stripLine[1]
                if stripLine[2] in DIELECTRICS:
                    dielectric = stripLine[2]
                if is_number(stripLine[3]):
                    voltage = float(stripLine[3])
                #print(stripLine[4].strip(" "))
                [valueStr, tolSymb] = stripLine[4].split(" ")

                if tolSymb in TOLERANCE_SYMB.keys():
                    tolerance = TOLERANCE_SYMB[tolSymb]
                value = getFloat(valueStr)
                return pd.DataFrame([[package, dielectric, voltage, tolerance, value]], columns=["Корпус", "Диэлектрик", "Напряжение", "Точность", "Номинал"])
            case "R":
                if stripLine[1] in PACKAGES:
                    package = stripLine[1]
                
                [valueStr, tolSymb] = stripLine[2].split(" ")

                if tolSymb in TOLERANCE_SYMB.keys():
                    tolerance = TOLERANCE_SYMB[tolSymb]
                value = getFloat(valueStr)
                return pd.DataFrame([[package, tolerance, value]], columns=["Корпус", "Точность", "Номинал"])
    except:
        return pd.DataFrame()
    

if __name__ == "__main__":
    d = splittedLine("C-0603-NP0-50-100pF K")

    d = pd.DataFrame()

    print(d.columns.array)

    print(getFloat("1K"))