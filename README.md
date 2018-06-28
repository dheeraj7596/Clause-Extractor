# Clause Extractor

This extracts the clauses from a given paragraph. This uses python implementation of Berkeley Parser as [here](https://github.com/emcnany/berkeleyinterface) 

## Environment ##

Note that this package requires the Berkeley Parser 1.6 or Berkeley Parser 1.7 JAR file (depending on your version of Java) as well as a grammar file. You can tell the Python module the location of these files via an ENVVAR:
    
    export BERKELEY_PARSER_JAR=/path/to/berkeley/parser.jar
    export BERKELEY_PARSER_GRM=/path/toberkeley/english.gr

*Note*: The default is currently set in the package. In future, please change accordingly.

## Installation and Dependencies ##
Download the JPype package from [JPype 0.5.4.2](http://jpype.sourceforge.net/) and unpackage it in your current working directory. Run the command:

    pip install JPype-0.5.4.2

which should begin the installation process. Then simply run:

    python setup.py install

And the BerkeleyInterface package should be installed into your Python path.

*Note*: For Mac users, you may have to modify JPype's settings a bit, according to this [Stackoverflow Question](http://stackoverflow.com/questions/18524501/installing-jpype-in-mountain-lion). Modify the `JPype-0.5.4.2/setup.py` file to include the line following line:

    def setupInclusion(self):
        self.includeDirs = [
            self.javaHome+"/include",
            self.javaHome+"/include/"+self.jdkInclude,
            "src/native/common/include",
            "src/native/python/include",

            #I added this line below. The folder contains a jni.h
            "/System/Library/Frameworks/JavaVM.framework/Versions/A/Headers/"
        ]

Then run the `pip install JPype-0.5.4.2` command and it should work.

## Run
Set the `_input` accordingly in `main.py` and execute to extract the clauses.