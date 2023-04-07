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


version 0.0.2:-
---------------

    1- create a concept of data pipeline
    2- add data access methods from filepath
        2.1- check data file availability in base path
            2.1.1- verify base path, if not create it
        2.2- in case file not there, copy from archive
            2.2.1- verify archive path, if not create it
        2.3- if merged data present then read as is
            2.3.1- merge data read need to be fixed[DONE]
            2.3.2- merge data read issue fixed, working in sequence
    4- load data file from base path
        4.1- using load data module access data as per process
        4.2- print data in buffer/ restore back to be used
    5- runnable data pipeline with data load(TEST success)
        5.1- pipeline line working now, all tests passed

