DATA PIPELINE AS A CONSTRUCT
----------------------------

feature development roadmap:-
-----------------------------
    - define data sequence flow as a data pipeline
    - add data operations for different data settings
    - save and retrieve data files as per process

version 0.0.1:-
---------------

    1- create a concept of data pipeline
    2- add data access methods from filepath
        2.1- check data file availability in base path
        2.2- in case file not there, copy from archive
        2.3- if merged data present then read as is
    4- load data file from base path
    5- runnable data pipeline with data load(TEST success)