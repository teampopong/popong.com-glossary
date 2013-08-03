#! /usr/bin/python2.7
# -*- coding: utf-8 -*-

import re
from flask import Flask, render_template

from settings import BABEL_SETTINGS, SERVER_SETTINGS
from utils.i18n import PopongBabel
from utils.glossary import load as load_glossary

app = Flask(__name__)
app.debug = SERVER_SETTINGS['debug']

terms = load_glossary('static/data/crawlers/glossary/glossary.csv')
PopongBabel(app, **BABEL_SETTINGS)

@app.route('/')
def home():
    return render_template('glossary.html', terms=terms)

def cmd_args():
    from argparse import ArgumentParser
    parser = ArgumentParser()
    parser.add_argument('-l', dest='locale',
            choices=app.LOCALES + ['auto'],
            default='auto')
    args = parser.parse_args()
    return args

def main():
    args = cmd_args()
    if args.locale and args.locale != 'auto':
        app.babel.locale_selector_func = lambda: args.locale
    app.run(**SERVER_SETTINGS)


if __name__ == '__main__':
    main()
