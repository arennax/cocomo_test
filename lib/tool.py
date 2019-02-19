import numpy as np


def mre_calc(y_predict, y_actual):
    mre = []
    for predict, actual in zip(y_predict, y_actual):
        mre.append(abs(predict - actual) / (actual))
    return mre


def sa_calc(Y_predict, Y_actual):
    sa = []
    mae_guess = sum(Y_actual) / len(Y_actual)
    for predict, actual in zip(Y_predict, Y_actual):
        ar = abs(predict - actual)
        sa.append(1 - ar / mae_guess)
    return sa