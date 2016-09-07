#!/bin/python2
import os, sys

outputfilename = "output.yaml"
numberofleadinglines = 3

if len(sys.argv) < 2:
    print "add a MAVLINK param input filename exported from QGroundControl"
    exit(0)

if len(sys.argv) > 2:
    outputfilename = "" + sys.argv[2] + ".yaml"

with open(outputfilename, 'w+') as outputFile :
    #
    outputFile.write("autopilot:\n")
    with open(sys.argv[1], 'r') as inputFile :
        lineid = 0
        for line in inputFile :
            if lineid > numberofleadinglines :
                data = line.split("\t")
                outputFile.write("  " + data[2] +": [" + data[3] + "] \n")
            lineid += 1
    outputFile.write("flyt: {global_namespace: flytpod, is_simulation_environment: '1'} \n")
    # End of file
    outputFile.write("\n")
