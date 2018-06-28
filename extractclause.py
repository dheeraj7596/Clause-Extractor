##########################################################################
## Imports
##########################################################################

import os
from BerkeleyInterface import *
from StringIO import StringIO
import nltk

##########################################################################
## Main Functionality
##########################################################################

def handle_sbar_tree(tree):
    clauses = []
    for child in tree:
        if child.label() == "S":
            clauses.append(" ".join(child.flatten()))
        elif child.label() == "FRAG":
            for gchild in child:
                if gchild.label() == "S":
                    clauses.append(" ".join(gchild.flatten()))
    return clauses

def extract_clauses(tree):
    clauses = []
    if isinstance(tree, str):
        return clauses
    for ind, child in enumerate(tree):
        clauses += extract_clauses(child)
        if not isinstance(child, str) and child.label() == "SBAR":
            clauses += handle_sbar_tree(child)
            tree.__delitem__(ind)
    return clauses

def extract_all_clauses(tree):
    clauses = extract_clauses(tree)
    clauses.append(" ".join(tree.flatten()))
    return clauses

def extractClause(parser, opts, _input=None):
    _in = StringIO(_input)
    _out = StringIO()
    res = parseInput(parser, opts, inputFile=_in, outputFile=_out)
    res_str = str(_out.getvalue())
    tree = nltk.tree.Tree.fromstring(res_str)
    tree = tree[0]
    clauses = extract_all_clauses(tree)
    return clauses