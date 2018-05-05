#!/usr/bin/python3

import sys
import Train
import Recommend


def printHelp():
    print('Help')


def train(filename):
    """[summary]
    训练数据
    Arguments:
        filename str
    """

    print('---------------------------------')
    print('Import Data File:', filename)
    t=Train.loadData(filename)
    print('Import Time: %.1f s'%(t))
    print('Import Done!')
    print('---------------------------------')
    print('Start Train Model')
    t=Train.train()
    print('Train Time %.1f s'%(t))
    print('Train Done!')
    print('---------------------------------')


def recommend(filename):
    print("Recommend", filename)


if __name__ == '__main__':
    if len(sys.argv) != 3:
        printHelp()
        exit()
    if sys.argv[1] == '-t':
        filename = sys.argv[2]
        train(filename)
    elif sys.argv[1] == '-n':
        filename = sys.argv[2]
        recommend(filename)
    else:
        print('help')
