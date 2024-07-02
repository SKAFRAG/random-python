from datetime import *
import psutil

def random(*args, **kargs):
    temps = datetime.now()
    temps = str(temps)
    temps_string = str(temps)
    after = ""
    dictio_id_var = {}


    for char in temps_string:
        if char == "-":
            char = ""
            after = after + char
        elif char == ".":
            char = ""
            after = after + char
        elif char == " ":
            char = ""
            after = after + char
        elif char == ":":
            char = ""
            after = after + char
        else:
            after = after + char
        int_after = int(after)

    list_id = []
    list_after_arg = []

    for arg in args:
        cpu_freq_act = psutil.cpu_freq()
        cpu_freq_act = cpu_freq_act.current
        cpu_freq_act = int(cpu_freq_act)
        int_after = int_after +4 ** 2 

        list_id.append(id(arg))
        after_arg =  2 + int_after + cpu_freq_act
        list_after_arg.append(after_arg)
        dictio_id_var[id(arg)] = arg

    
    minimum = min(list_after_arg)

    for i in range(len(list_after_arg)):
        if list_after_arg[i] == minimum:
            index_list_after_arg = i
    for i in dictio_id_var.keys():
        if i == list_id[index_list_after_arg]:
            var_final = dictio_id_var[i]
        else:
            pass

    print(var_final)
    return(var_final)



random(10,14,4,2,6,7)