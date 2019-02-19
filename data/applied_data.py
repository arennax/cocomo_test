import pandas as pd
from scipy.io.arff import loadarff
import pdb


def data_cocomo81():
    raw_data = loadarff("./data/cocomo81.arff")
    df_data = pd.DataFrame(raw_data[0])
    return df_data


def data_nasa93():
    raw_data = loadarff("./data/nasa93.arff")
    df_data = pd.DataFrame(raw_data[0]).drop(columns=['recordnumber', 'projectname', 'cat2', 'forg', 'center', 'year', 'mode'])
    rely_dict = {b'vl':0.75, b'l':0.88, b'n':1.00, b'h':1.15, b'vh':1.40, b'xh':0}
    data_dict = {b'vl': 0, b'l': 0.94, b'n': 1.00, b'h': 1.08, b'vh': 1.16, b'xh': 0}
    cplx_dict = {b'vl': 0.70, b'l': 0.85, b'n': 1.00, b'h': 1.15, b'vh': 1.30, b'xh': 1.65}
    time_dict = {b'vl': 0, b'l': 0, b'n': 1.00, b'h': 1.11, b'vh': 1.30, b'xh': 1.66}
    stor_dict = {b'vl': 0, b'l': 0, b'n': 1.00, b'h': 1.06, b'vh': 1.21, b'xh': 1.56}
    virt_dict = {b'vl': 0, b'l': 0.87, b'n': 1.00, b'h': 1.15, b'vh': 1.30, b'xh': 0}
    turn_dict = {b'vl': 0, b'l': 0.87, b'n': 1.00, b'h': 1.07, b'vh': 1.15, b'xh': 0}
    acap_dict = {b'vl': 1.46, b'l': 1.19, b'n': 1.00, b'h': 0.86, b'vh': 0.71, b'xh': 0}
    aexp_dict = {b'vl': 1.29, b'l': 1.13, b'n': 1.00, b'h': 0.91, b'vh': 0.82, b'xh': 0}
    pcap_dict = {b'vl': 1.42, b'l': 1.17, b'n': 1.00, b'h': 0.86, b'vh': 0.70, b'xh': 0}
    vexp_dict = {b'vl': 1.21, b'l': 1.10, b'n': 1.00, b'h': 0.90, b'vh': 0, b'xh': 0}
    lexp_dict = {b'vl': 1.14, b'l': 1.07, b'n': 1.00, b'h': 0.95, b'vh': 0, b'xh': 0}
    modp_dict = {b'vl': 1.24, b'l': 1.10, b'n': 1.00, b'h': 0.91, b'vh': 0.82, b'xh': 0}
    tool_dict = {b'vl': 1.24, b'l': 1.10, b'n': 1.00, b'h': 0.91, b'vh': 0.83, b'xh': 0}
    sced_dict = {b'vl': 1.23, b'l': 1.08, b'n': 1.00, b'h': 1.04, b'vh': 1.10, b'xh': 0}
    df_data.rely = df_data.rely.map(lambda i: rely_dict[i])
    df_data.data = df_data.data.map(lambda i: data_dict[i])
    df_data.cplx = df_data.cplx.map(lambda i: cplx_dict[i])
    df_data.time = df_data.time.map(lambda i: time_dict[i])
    df_data.stor = df_data.stor.map(lambda i: stor_dict[i])
    df_data.virt = df_data.virt.map(lambda i: virt_dict[i])
    df_data.turn = df_data.turn.map(lambda i: turn_dict[i])
    df_data.acap = df_data.acap.map(lambda i: acap_dict[i])
    df_data.aexp = df_data.aexp.map(lambda i: aexp_dict[i])
    df_data.pcap = df_data.pcap.map(lambda i: pcap_dict[i])
    df_data.vexp = df_data.vexp.map(lambda i: vexp_dict[i])
    df_data.lexp = df_data.lexp.map(lambda i: lexp_dict[i])
    df_data.modp = df_data.modp.map(lambda i: modp_dict[i])
    df_data.tool = df_data.tool.map(lambda i: tool_dict[i])
    df_data.sced = df_data.sced.map(lambda i: sced_dict[i])
    # df_data.replace(tmp_dict, inplace=True)
    return df_data


def data_cocomo_nasa_1():
    raw_data = loadarff("./data/cocomonasa_v1.arff")
    df_data = pd.DataFrame(raw_data[0])
    RELY_dict = {b'Very_Low':0.75, b'Low':0.88, b'Nominal':1.00, b'High':1.15, b'Very_High':1.40, b'Extra_High':0}
    DATA_dict = {b'Very_Low': 0, b'Low': 0.94, b'Nominal': 1.00, b'High': 1.08, b'Very_High': 1.16, b'Extra_High': 0}
    CPLX_dict = {b'Very_Low': 0.70, b'Low': 0.85, b'Nominal': 1.00, b'High': 1.15, b'Very_High': 1.30, b'Extra_High': 1.65}
    TIME_dict = {b'Very_Low': 0, b'Low': 0, b'Nominal': 1.00, b'High': 1.11, b'Very_High': 1.30, b'Extra_High': 1.66}
    STOR_dict = {b'Very_Low': 0, b'Low': 0, b'Nominal': 1.00, b'High': 1.06, b'Very_High': 1.21, b'Extra_High': 1.56}
    VIRT_dict = {b'Very_Low': 0, b'Low': 0.87, b'Nominal': 1.00, b'High': 1.15, b'Very_High': 1.30, b'Extra_High': 0}
    TURN_dict = {b'Very_Low': 0, b'Low': 0.87, b'Nominal': 1.00, b'High': 1.07, b'Very_High': 1.15, b'Extra_High': 0}
    ACAP_dict = {b'Very_Low': 1.46, b'Low': 1.19, b'Nominal': 1.00, b'High': 0.86, b'Very_High': 0.71, b'Extra_High': 0}
    AEXP_dict = {b'Very_Low': 1.29, b'Low': 1.13, b'Nominal': 1.00, b'High': 0.91, b'Very_High': 0.82, b'Extra_High': 0}
    PCAP_dict = {b'Very_Low': 1.42, b'Low': 1.17, b'Nominal': 1.00, b'High': 0.86, b'Very_High': 0.70, b'Extra_High': 0}
    VEXP_dict = {b'Very_Low': 1.21, b'Low': 1.10, b'Nominal': 1.00, b'High': 0.90, b'Very_High': 0, b'Extra_High': 0}
    LEXP_dict = {b'Very_Low': 1.14, b'Low': 1.07, b'Nominal': 1.00, b'High': 0.95, b'Very_High': 0, b'Extra_High': 0}
    MODP_dict = {b'Very_Low': 1.24, b'Low': 1.10, b'Nominal': 1.00, b'High': 0.91, b'Very_High': 0.82, b'Extra_High': 0}
    TOOL_dict = {b'Very_Low': 1.24, b'Low': 1.10, b'Nominal': 1.00, b'High': 0.91, b'Very_High': 0.83, b'Extra_High': 0}
    SCED_dict = {b'Very_Low': 1.23, b'Low': 1.08, b'Nominal': 1.00, b'High': 1.04, b'Very_High': 1.10, b'Extra_High': 0}
    df_data.RELY = df_data.RELY.map(lambda i: RELY_dict[i])
    df_data.DATA = df_data.DATA.map(lambda i: DATA_dict[i])
    df_data.CPLX = df_data.CPLX.map(lambda i: CPLX_dict[i])
    df_data.TIME = df_data.TIME.map(lambda i: TIME_dict[i])
    df_data.STOR = df_data.STOR.map(lambda i: STOR_dict[i])
    df_data.VIRT = df_data.VIRT.map(lambda i: VIRT_dict[i])
    df_data.TURN = df_data.TURN.map(lambda i: TURN_dict[i])
    df_data.ACAP = df_data.ACAP.map(lambda i: ACAP_dict[i])
    df_data.AEXP = df_data.AEXP.map(lambda i: AEXP_dict[i])
    df_data.PCAP = df_data.PCAP.map(lambda i: PCAP_dict[i])
    df_data.VEXP = df_data.VEXP.map(lambda i: VEXP_dict[i])
    df_data.LEXP = df_data.LEXP.map(lambda i: LEXP_dict[i])
    df_data.MODP = df_data.MODP.map(lambda i: MODP_dict[i])
    df_data.TOOL = df_data.TOOL.map(lambda i: TOOL_dict[i])
    df_data.SCED = df_data.SCED.map(lambda i: SCED_dict[i])
    return df_data


# def data_cocomo_sdr():
#     raw_data = loadarff("./data/cocomo-sdr.arff")
#     df_data = pd.DataFrame(raw_data[0]).drop(columns=['ProjectID', 'PREC', 'FLEX', 'RESL', 'TEAM', 'PMAT'])
#     return df_data

 
if __name__ == '__main__':
    print(data_nasa93())
