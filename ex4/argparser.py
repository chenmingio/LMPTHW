class Argparser():

    def __init__(self, argv_list):
        help_doc = "help doc..."
        flag_list = []
        option_list = []
        pos_list = []
        self.flags = []
        self.option = []
        self.pos = []

        # arguments categorizing
        for n in range(1,len(argv_list)):
            if "-" in argv_list[n]:
                flag_list.append(n)

        last_flag = flag_list[-1]

        for j in range(1, last_flag):
            if j not in flag_list:
                option_list.append(j)

        for i in range(last_flag + 1, len(argv_list)):
            if '.' not in argv_list[i]:
                print("positional argument error: " + argv_list[i])
            else:
                pos_list.append(i)

        self.flags = [argv_list[n] for n in flag_list]
        self.option = [argv_list[n] for n in option_list]
        self.pos = [argv_list[n] for n in pos_list]

        # arguments handling
        for n in flag_list:
            if argv_list[n] in ["-h", "-help"]:
                print(help_doc)

