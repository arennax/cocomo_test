from data.applied_data import *
from lib.tool import *

def cocomo_II(dataset, a=2.94, b=0.91):
    input = dataset.iloc[:, :-2]
    kloc = dataset.iloc[:, -2:-1]
    effort_actual = dataset.iloc[:, -1]
    eaf = input.prod(axis=1).to_frame(name = 'eaf')
    temp = a * (kloc ** b)
    effort_predict = temp.iloc[:,0] * eaf.iloc[:,0]

    mre_list = mre_calc(effort_predict, effort_actual)  ######### for MRE
    sa_list = sa_calc(effort_predict, effort_actual)  ######### for SA

    return mre_list, sa_list


if __name__ == '__main__':
    print(cocomo_II(data_cocomo81())[1])