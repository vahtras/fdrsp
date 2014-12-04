Nightly testing
===============

Sample script
-------------

The `cronjob` script is included as an example of how to repeat calculations
on a dayly basis::

    #!/bin/bash
    #:r !env | grep SSH_
    #
    export SSH_AGENT_PID SSH_AUTH_SOCK

    cd /tmp
    rm -rf dalton
    git clone git@repo.ctcc.no:dalton.git
    cd dalton
    ./setup --fc=mpif90 --cc=mpicc --cxx=mpiCC -D CPP=-DDISABLE_XC_RESPONSE_SANITY_CHECK
    cd build
    make dalton.x || exit
    git clone https://github.com/vahtras/fdrsp.git
    cd fdrsp
    export PATH=$PATH:/tmp/dalton/build
    ./submitall pure_functionals
    #
    # Unpack html at a site of your choice
    #
    # scp test_findif.tgz remote_host:
    # ssh remote_host tar -C ./pub -xzf test_findif.tgz
    #

* You need to define set-up ssh environment variables to access your repository without giving passwords interactively. Typically in your shell::

    $ eval $(ssh-agent)
    Agent pid 6396
    $ env | grep SSH_
    SSH_AGENT_PID=6396
    SSH_AUTH_SOCK=/tmp/ssh-70Eb02l3p1ws/agent.6395

* Enter the output of these lines after line three in the `cronjob` script::

    #!/bin/bash
    #:r !env | grep SSH_
    #
    SSH_AGENT_PID=6396
    SSH_AUTH_SOCK=/tmp/ssh-70Eb02l3p1ws/agent.6395
    export SSH_AGENT_PID SSH_AUTH_SOCK

* By default all code is unpacked and compiled in `/tmp`. Edit that if you like

* The script stops if the compile step finishes with a non-zero status

* The list of functionals in `pure_functionals` are tested. Please change if you prefer otherwise. Functionals that have an asterix attached (e.g. `LYP*`) are tested together with a HF exchange component. This used when functionals, e.g. pure correletion functionals, do not converge on their own.

Setting up cron
---------------

To edit your cron job settings::

    $ crontab -e

Add line at the end of this file like this::

    ...
    # For more information see the manual pages of crontab(5) and cron(8)
    # 
    # m h  dom mon dow   command
    0 0 * * * /home/vahtras/dev/py/fdrsp/cronjob

and the tests will run at midnight of every daty

