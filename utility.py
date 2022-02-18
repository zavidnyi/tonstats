def updateConf():
    n_of_run=0
    with open("config", "r") as cur_conf:
            n_of_run = int(cur_conf.read())
            with open("config", "w") as new_conf:
                new_conf.write(str((n_of_run + 1) % 3))
    return n_of_run
            