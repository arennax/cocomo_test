import time
from method.cocomo2 import *
from lib.tool import *

data = data_cocomo81()
repeats = 20
metrics = 1     # "0" for MRE, "1" for SA


if __name__ == '__main__':
    list_temp = []
    time2 = time.time()
    for i in range(repeats):
        list_temp.append(cocomo_II(data)[metrics])
    run_time2 = str(time.time() - time2)

    flat_list = np.array(list_temp).flatten()
    list_output = sorted(flat_list.tolist())

    print(list_output)
    print("median for COCOMO_II:", np.median(list_output))
    print("runtime for COCOMO_II:", run_time2)

    with open("./output/cocomo_sk_results.txt", "w") as output:
        output.write('\n\n' + "COCOMO_II" + '\n')
        for i in sorted(list_output):
            output.write(str(i) + " ")