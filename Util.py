#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Jun 15 13:59:56 2019

@author: BradleyCrump
"""
import time as t
import sys


def wait(time):
    timer = 0
    while timer < time:
        t.sleep(1)
        output = "."
        output.rstrip()
        print(output, end="")
        timer += 1


def waitNoDot(time):
    timer = 0
    while timer < time:
        # t.sleep(1)
        timer += 1

# not quite working


def progress():
    toolbar_width = 40

    # setup toolbar
    sys.stdout.write("[%s]" % (" " * toolbar_width))
    sys.stdout.flush()
    # return to start of line, after '['

    for i in range(toolbar_width):
        t.sleep(0.1)  # do real work here
        sys.stdout.write("-")
        sys.stdout.write("\b" * (toolbar_width+1))
        sys.stdout.flush()

    sys.stdout.write("]\n")  # this ends the progress bar
