#! /usr/bin/python2.7
# -*- coding: utf-8 -*-

from flask import Flask, render_template
import os
import re

from settings import BABEL_SETTINGS, SERVER_SETTINGS, SCRIPT_NAME
from utils.i18n import PopongBabel
from utils.glossary import load as load_glossary
from utils.reverse_proxy import init_app as init_reverse_proxy

app = Flask(__name__)
app.debug = SERVER_SETTINGS['debug']

p = os.path.join(app.root_path, 'static/data/crawlers/glossary/glossary.csv')
terms = load_glossary(p)
PopongBabel(app, **BABEL_SETTINGS)
init_reverse_proxy(app, SCRIPT_NAME)

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
