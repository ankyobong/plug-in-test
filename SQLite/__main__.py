"""
====================================
 :mod:`argoslabs.data.sqlite`
====================================
.. moduleauthor:: Kyobong An <akb0930@argos-labs.com>
.. note:: ARGOS-LABS License

Description
===========
ARGOS LABS plugin module for sqlite
"""

################################################################################
import sys
from alabs.common.util.vvargs import ArgsError, ArgsExit
from plug_in.SQLite import main


################################################################################
if __name__ == '__main__':
    try:
        main()
    except ArgsError as err:
        sys.stderr.write('Error: %s\nPlease -h to print help\n' % str(err))
    except ArgsExit as _:
        pass
