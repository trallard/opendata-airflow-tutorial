Setup
===============
This section will guide you through the pre requisites for the workshop.
Please make sure to install the libraries before the workshop as the conference WiFi 
can get quite slow when having too many people downloading and installing things at the same 
time.

Make sure to follow all the steps as detailed here.

Python 3.x
++++++++++

3.7 Preferred

We will be using `Python <https://www.python.org/>`_.
Installing all of Python's packages individually can be a bit
difficult, so we recommend using `Anaconda <https://www.anaconda.com/>`_ which
provides a variety of useful packages/tools.

To download Anaconda, follow the link https://www.anaconda.com/download/ and select
Python 3. Following the download, run the installer as per usual on your machine.

If you prefer not using Anaconda then this `tutorial <https://realpython.com/installing-python/>`_ can help you with the installation and 
setup.

If you already have Python installed but not via Anaconda do not worry.
Make sure to have either ``venv`` or ``pipenv`` installed. Then follow the instructions to set 
your virtual environment further down.

Git
+++

`Git <https://git-scm.com/>`_ is a version control software that records changes
to a file or set of files. Git is especially helpful for software developers
as it allows changes to be tracked (including who and when) when working on a
project.

To download Git, go to the following link and choose the correct version for your
operating system: https://git-scm.com/downloads.

Windows
--------

Download the  `git for Windows installer <https://gitforwindows.org/>`_ . 
Make sure to select "use Git from the Windows command prompt" 
this will ensure that Git is permanently added to your PATH. 

Also select "Checkout Windows-style, commit Unix-style line endings" selected and click on "Next".

This will provide you both git and git bash. We will use the command line quite a lot during the workshop 
so using git bash is a good option.

GitHub
++++++

GitHub is a web-based service for version control using Git. You will need
to set up an account at `https://github.com <https://github.com>`_. Basic GitHub accounts are
free and you can now also have private repositories.

Text Editors/IDEs
++++++++++++

Text editors are tools with powerful features designed to optimize writing code.
There are several text editors that you can choose from.
Here are some we recommend:

- `VS code <https://code.visualstudio.com//?wt.mc_id=euroscipy-github-taallard>`_: this is your facilitator's favourite 💜 and it is worth trying if you have not checked it yet
- `Pycharm <https://www.jetbrains.com/pycharm/download/>`_
- `Atom <https://atom.io>`_

We suggest trying several editors before settling on one.

If you decide to go for VSCode make sure to also
have the `Python extension <https://marketplace.visualstudio.com/itemdetails?itemName=ms-python.python&wt.mc_id=euroscipy-github-taallard>`_
installed. This will make your life so much easier (and it comes with a lot of nifty
features 😎).

Creating a virtual environment
+++++++++++++++++++++++++++++++

You will need to create a virtual environment to make sure that you have the right packages and setup needed to follow along the tutorial.
Follow the instructions that best suit your installation.

Anaconda
--------

Clone the repository: 
::
    git clone https://github.com/trallard/opendata-airflow-tutorial

Change into the repo
::
    cd opendata-airflow-tutorial   

Create a conda environment:
:: 
    conda env create -f environment.yml

Once all the dependencies are installed you can activate your environment through the following commands 
::
    source activate airflow-env # Mac
    activate airflow-env        # Windows and Linux
To exit the environment you can use 
::
    conda deactivate   

virtualenv
-----------
Create a directory for the tutorial, for example :
::
    mkdir airflow-tutorial 
and change directories into it (``cd airflow-tutorial``).
Now you  need to run venv 
::
    python3 -m venv env/airflow # Mac and Linux 
    python -m venv env/airflow  # Windows

this will create a virtual Python environment in the ``env/airflow`` folder.
Before installing the required packages you need to activate your virtual environment: 
::
    source env/bin/activate # Mac and Linux 
    .\env\Scripts\activate  # Windows 


Now you can install the packages using via pip ``pip install -r requirements.txt``

To leave the virtual environment run ``deactivate``

Docker
+++++++

There is a Docker image built with all the needed libraries. 

You can run it locally with:
::
    docker run --rm -it -p 5555:5555/tcp -p 8080:8080/tcp -p 8793:8793/tcp -p 8888:8888/tcp -e JUPYTER_ENABLE_LAB=yes trallard/airflow-tutorial:1.0