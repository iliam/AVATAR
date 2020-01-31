import os

from pm4py.objects.petri.importer import factory as pnml_importer

from processmining.playout import Player
from systems.util import writeToFile

if __name__ == "__main__": 
    pn = "pb_system_3_6.pnml"
    f_pop = "pb_system_3_6_b_pop.txt"
    f_train = "pb_system_3_6_b_train.txt"
    f_test = "pb_system_3_6_b_test.txt"

    f_pn = os.path.join(pn)
    net, initial_marking, final_marking = pnml_importer.apply(f_pn)
    print(initial_marking)
    print(final_marking)

    player = Player(net, initial_marking, final_marking, maxTraceLength=200, rep_inv_thresh=100, max_loop=3)
    gen_traces = player.play()


    print("*** ALL POSSIBLE TRACES ***")
    print(len(gen_traces))
    writeToFile(f_pop, gen_traces)

    max_len = 0
    for trace in gen_traces:
        if len(trace) > max_len:
            max_len = len(trace)


    test = list()
    train = list()
    for trace in gen_traces:
        if len(trace) == max_len:
            train.append(trace)
            gen_traces.remove(trace)
            break

    gen_traces = list(gen_traces)
    gen_traces.sort(key = lambda s: len(s))
    threshold = 0.7 * len(gen_traces)

    cnt = 0
    for trace in gen_traces:
        if cnt < threshold:
            train.append(trace)
        else:
            test.append(trace)
        cnt += 1

    writeToFile(f_train, train)
    writeToFile(f_test, test)