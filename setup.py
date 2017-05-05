import os
import platform
from setuptools import setup, Command
from subprocess import check_output


class GrammarCommand(Command):
    user_options = []

    def initialize_options(self):
        pass

    def finalize_options(self):
        pass

    def run(self):
        if platform.python_version().startswith('2'):
            from urllib2 import urlopen
        else:
            from urllib.request import urlopen

        ANTLR_URL = 'http://www.antlr.org/download/antlr-4.7-complete.jar'
        ANTLR_DIR = '.antlr'
        ANTLR_JAR = os.path.join(ANTLR_DIR, 'antlr-4.7-complete.jar')
        ANTLR_CMD = ["java", "-jar", ANTLR_JAR]

        if not os.path.exists(ANTLR_JAR):
            if not os.path.exists(ANTLR_DIR):
                os.mkdir(ANTLR_DIR)
            with open(ANTLR_JAR, 'wb') as f:
                f.write(urlopen(ANTLR_URL).read())

        output = check_output(ANTLR_CMD + [
            "-Dlanguage=Python2", "-visitor", "-no-listener",
            "-o", "ren/py2grammar", "ren.g4"])
        if output:
            self.announce(output)
        open('ren/py2grammar/__init__.py', 'a').close()

        output = check_output(ANTLR_CMD + [
            "-Dlanguage=Python3", "-visitor", "-no-listener",
            "-o", "ren/py3grammar", "ren.g4"])
        if output:
            self.announce(output)
        open('ren/py3grammar/__init__.py', 'a').close()


setup(
    name="ren",
    version="0.0.1",
    packages=["ren"],
    cmdclass={
        'grammar': GrammarCommand
    }
)
