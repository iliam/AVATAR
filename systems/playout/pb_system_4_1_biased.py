from systems.playout.util import biased_playout

if __name__ == "__main__": 
    pn = "data/systems/pb_system_4_1.pnml"
    f_pop = "data/variants/pb_system_4_1_b_pop.txt"
    f_train = "data/variants/pb_system_4_1_b_train.txt"
    f_test = "data/variants/pb_system_4_1_b_test.txt"
    xes_train = "data/variants/pb_system_4_1_b_train.xes"
    csv_train = "data/variants/pb_system_4_1_b_train.csv"

    biased_playout(pn=pn, f_pop=f_pop, f_train=f_train, f_test=f_test, xes_train=xes_train, csv_train=csv_train)