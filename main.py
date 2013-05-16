#! /usr/bin/python2.7
# -*- coding: utf-8 -*-

import os

from crawlers import likms
from crawlers import nas
from settings import BASEURL, DIR, RANGE

def main(target):

    directory = '%s/%s' % (DIR['html'], target)
    baseurl = BASEURL[target]
    rng = RANGE[target]
    filename = '%s/%s.csv' % (DIR['results'], target)

    if not os.path.exists(directory):
        os.makedirs(directory)

    eval('%s.crawl("%s", "%s", %s)' % (target, baseurl, directory, rng))
    #eval('%s.parse("%s", "%s", %s)' % (target, directory, filename, rng))

main('nas')
main('likms')
