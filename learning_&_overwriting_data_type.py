import pandas as pd


# reading csv file

def collecting_data(file):
    try:
        datas = pd.read_csv(file)
        print(datas)
        return datas
    except:
        print("check if your file is csv")


# getting data and writing

def defining_data(datas):
    j = 0
    dic_data = {}
    for i in datas.columns:
        dlist = []
        check = datas.iloc[:, j]
        for a in check:
            print(a)
            s1 = str(type(a))
            s2 = s1[8:11]
            dlist.append(s2)
        datatype = pd.Series(dlist)
        dic_data["{}".format(i)] = datatype
        j = j + 1
    Data = pd.DataFrame(dic_data)
    print(Data)
    Data.to_csv("datatypes.csv")


# testing

defining_data(collecting_data("test.csv"))