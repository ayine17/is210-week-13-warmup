#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""week 13 task_01 module"""

import os
import csv
import json

GRADING_SCALE = {'A': 1.00,
                 'B': 0.90,
                 'C': 0.80,
                 'D': 0.70,
                 'F': 0.60}


def get_score_summary(filename):
    """ a fuction to manipulate CSV file
    args:
        filename(string): a string which represents the filename whose data
                          will be read and interpreted
    return:
        return a dictionary, keyed by boro, whose value is a tuple with the
        number of restaurateurs per boro (who have scores), and the average
        score (as a float) for that boro.
    example:
        >>> get_score_summary('inspection_results.csv')
        >>> {'BRONX': (156, 0.9762820512820514), 'BROOKLYN':
        (417, 0.9745803357314141), 'STATEN ISLAND': (46, 0.9804347826086955),
        'MANHATTAN': (748, 0.9771390374331531), 'QUEENS':
        (414, 0.9719806763285017)}

    """
    try:
        filepath = open(filename)
        jsonfile = csv.reader(filepath)

    except IOError:
        print ' invalid file'

    de_dupulate = set()
    de_duplicate = {}

    queens_score = 0
    queens_counter = 0
    bronx_counter = 0
    bronx_score = 0
    brooklyn_counter = 0
    brooklyn_score = 0
    staten_counter = 0
    staten_score = 0
    manhattan_score = 0
    manhattan_counter = 0
    for line in jsonfile:
        test = line[10].strip() == ''
        if test or line[10].strip() is None or line[10] == 'P':
            pass
        else:
            if line[0] not in de_dupulate:
                de_dupulate = line
                de_duplicate.update(([(line[0], (line[1], line[10]))]))
    for dep in de_duplicate.iteritems():

        if dep[1][0].strip() == 'QUEENS':
            queens = dep[1][0].strip()
            queens_counter += 1
            if dep[1][1].strip() == GRADING_SCALE.keys()[0]:
                queens_score += GRADING_SCALE[GRADING_SCALE.keys()[0]]

            if dep[1][1].strip() == GRADING_SCALE.keys()[1]:
                queens_score += GRADING_SCALE[GRADING_SCALE.keys()[1]]

            if dep[1][1].strip() == GRADING_SCALE.keys()[2]:
                queens_score += GRADING_SCALE[GRADING_SCALE.keys()[2]]

            if dep[1][1].strip() == GRADING_SCALE.keys()[3]:
                queens_score += GRADING_SCALE[GRADING_SCALE.keys()[2]]

            if dep[1][1].strip() == GRADING_SCALE.keys()[3]:
                queens_score += GRADING_SCALE[GRADING_SCALE.keys()[2]]

        if dep[1][0].strip() == 'BRONX':
            bronx = dep[1][0].strip()
            bronx_counter += 1
            if dep[1][1].strip() == GRADING_SCALE.keys()[0]:
                bronx_score += GRADING_SCALE[GRADING_SCALE.keys()[0]]

            if dep[1][1].strip() == GRADING_SCALE.keys()[1]:
                bronx_score += GRADING_SCALE[GRADING_SCALE.keys()[1]]

            if dep[1][1].strip() == GRADING_SCALE.keys()[2]:
                bronx_score += GRADING_SCALE[GRADING_SCALE.keys()[2]]

            if dep[1][1].strip() == GRADING_SCALE.keys()[3]:
                bronx_score += GRADING_SCALE[GRADING_SCALE.keys()[3]]

            if dep[1][1].strip() == GRADING_SCALE.keys()[4]:
                bronx_score += GRADING_SCALE[GRADING_SCALE.keys()[4]]

        if dep[1][0].strip() == 'MANHATTAN':
            manhattan = dep[1][0].strip()
            manhattan_counter += 1
            if dep[1][1].strip() == GRADING_SCALE.keys()[0]:
                manhattan_score += GRADING_SCALE[GRADING_SCALE.keys()[0]]

            if dep[1][1].strip() == GRADING_SCALE.keys()[1]:
                manhattan_score += GRADING_SCALE[GRADING_SCALE.keys()[1]]

            if dep[1][1].strip() == GRADING_SCALE.keys()[2]:
                manhattan_score += GRADING_SCALE[GRADING_SCALE.keys()[2]]

            if dep[1][1].strip() == GRADING_SCALE.keys()[3]:
                manhattan_score += GRADING_SCALE[GRADING_SCALE.keys()[3]]

            if dep[1][1].strip() == GRADING_SCALE.keys()[4]:
                manhattan_score += GRADING_SCALE[GRADING_SCALE.keys()[4]]

        if dep[1][0].strip() == 'BROOKLYN':
            brooklyn = dep[1][0].strip()
            brooklyn_counter += 1
            if dep[1][1].strip() == GRADING_SCALE.keys()[0]:
                brooklyn_score += GRADING_SCALE[GRADING_SCALE.keys()[0]]

            if dep[1][1].strip() == GRADING_SCALE.keys()[1]:
                brooklyn_score += GRADING_SCALE[GRADING_SCALE.keys()[1]]

            if dep[1][1].strip() == GRADING_SCALE.keys()[2]:
                brooklyn_score += GRADING_SCALE[GRADING_SCALE.keys()[2]]

            if dep[1][1].strip() == GRADING_SCALE.keys()[3]:
                brooklyn_score += GRADING_SCALE[GRADING_SCALE.keys()[3]]

            if dep[1][1].strip() == GRADING_SCALE.keys()[4]:
                brooklyn_score += GRADING_SCALE[GRADING_SCALE.keys()[4]]

        if dep[1][0].strip() == 'STATEN ISLAND':
            staten = dep[1][0].lstrip().rstrip()
            staten_counter += 1
            if dep[1][1].strip() == GRADING_SCALE.keys()[0]:
                staten_score += GRADING_SCALE[GRADING_SCALE.keys()[0]]

            if dep[1][1].strip() == GRADING_SCALE.keys()[1]:
                staten_score += GRADING_SCALE[GRADING_SCALE.keys()[1]]
            if dep[1][1].strip() == GRADING_SCALE.keys()[2]:
                staten_score += GRADING_SCALE[GRADING_SCALE.keys()[2]]

            if dep[1][1].strip() == GRADING_SCALE.keys()[3]:
                staten_score += GRADING_SCALE[GRADING_SCALE.keys()[3]]

            if dep[1][1].strip() == GRADING_SCALE.keys()[4]:
                staten_score += GRADING_SCALE[GRADING_SCALE.keys()[4]]
    filepath.close()
    # calculate Bor AVgs
    queens_avg = queens_score / (queens_counter)
    bronx_avg = bronx_score / (bronx_counter)
    manhattan_avg = manhattan_score / (manhattan_counter)
    brooklyn_avg = brooklyn_score / (brooklyn_counter)
    staten_avg = staten_score / (staten_counter)

    quex = (queens, (queens_counter, queens_avg))
    bnx = (bronx, (bronx_counter, bronx_avg))
    mtt = (manhattan, (manhattan_counter, manhattan_avg))
    bky = (brooklyn, (brooklyn_counter, brooklyn_avg))
    sti = (staten, (staten_counter, staten_avg))
    output = dict([quex, bnx, mtt, bky, sti])
    return output


def get_market_density(filename):
    """ a fuction to manipulate Json file
    args:
        filename(string): file name to be open and read from
    return:
        Return a dictionary of the number of green markets per borough.
    example:
        >>> get_market_density('green_markets.json')
        {u'STATEN ISLAND': 2, u'BROOKLYN': 48, u'BRONX': 32,
        u'MANHATTAN': 39, u'QUEENS': 16}
    """

    filepath = os.path.abspath(filename)
    openfile = open(filepath)
    jsonfile = json.load(openfile)

    bronx_counter = 0
    staten_counter = 0
    manhattan_counter = 0
    queens_counter = 0
    brooklyn_counter = 0
    for line in jsonfile['data']:

        if line[8].rstrip().lstrip() == 'Bronx':
            bronx_counter += 1
            bronx = line[8].lstrip().rstrip().upper()
        if line[8].rstrip().lstrip() == 'Staten Island':
            staten_counter += 1
            staten = line[8].lstrip().rstrip().upper()
        if line[8].rstrip().lstrip() == 'Manhattan':
            manhattan_counter += 1
            manhattan = line[8].lstrip().rstrip().upper()
        if line[8].rstrip().lstrip() == 'Queens':
            queens_counter += 1
            queens = line[8].lstrip().rstrip().upper()
        if line[8].rstrip().lstrip() == 'Brooklyn':
            brooklyn_counter += 1
            brooklyn = line[8].lstrip().rstrip().upper()
    openfile. close()
    return dict(([(bronx, bronx_counter), (manhattan, manhattan_counter),
                  (queens, queens_counter), (brooklyn, brooklyn_counter),
                  (staten, staten_counter)]))


def correlate_data(csvfile, jsonfile, outputfile):
    """ a fuction that Combine csv and Json files data into a single dict
    args:
        csvfile(file): name of a file with restaurant scores data
        Jsonfile (file): the name of a JSON file with green_market data
        outputfile(file): the name of a file that will contain the
                            output of this function.
    return:
        return a file of single dictionary keyed by borough, whose whose
        values are tuples containing the borough food score and the
        percentage density of green markets to restaurateurs as a float.
    example:
        correlate_data('inspection_results.csv', 'green_markets.json',
        'outputfile')
        {'bronx': (0.9762820512820514, 0.1987179487179487)}
    """

    inspection_results = get_score_summary(csvfile)
    green_market_data = get_market_density(jsonfile)
    dict_opt = []
    for green_keys, green_values in green_market_data.iteritems():
        if green_keys in inspection_results:
            inspe_value = inspection_results[green_keys]

            green = green_values
            value = inspection_results[green_keys][1]

            percen = green/float(inspe_value[0])
            dict_opt.append(dict([(green_keys, (value, percen))]))

    outfile = open(outputfile, 'w')
    json.dump(dict_opt, outfile)
    outfile.close()
    return dict_opt
