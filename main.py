from groupStatictics import getGroupsStatistics
from find_groups_number import findGroupsNumber
from userStatistics import getNumberOfNewUsers
from utility import updateConf

NUMBER_OF_RUNS=3

if __name__ == '__main__':
    # print("New Users since last time:" + str(getNumberOfNewUsers()))
    cur_run = updateConf()
    getGroupsStatistics(findGroupsNumber(10000), cur_run)