import nltk
import os
from BerkeleyInterface import *
from extractclause import *

JAR_PATH = r'./BerkeleyParser-1.7.jar'
GRM_PATH = r'./eng_sm6.gr'

cp = os.environ.get("BERKELEY_PARSER_JAR", JAR_PATH)

# This has to be changed with respect to your JAVA_HOME. 
os.environ["JAVA_HOME"] = "/usr/lib/jvm/java-1.8.0-openjdk-1.8.0.171-8.b10.el7_5.x86_64"


startup(cp)

gr = os.environ.get("BERKELEY_PARSER_GRM", GRM_PATH)
args = {"gr":gr, "tokenize":True}
opts = getOpts(dictToArgs(args))
parser = loadGrammar(opts)
_input = "The actor was happy he got a part in a movie, although the part was small."

clauses = extractClause(parser, opts, _input)
print clauses