# config script

class Configuration:
    """configuration concept or blue-print"""
    def __init__(self,BASE_PATH, ARCHIVE_PATH):
        self.BASE_PATH = BASE_PATH
        self.ARCHIVE_PATH = ARCHIVE_PATH

# DEBUGGER------------------------------------------------------------>
# config = Configuration(BASE_PATH=BASE_PATH,ARCHIVE_PATH=ARCHIVE_PATH)
# print(config.ARCHIVE_PATH)
# DEBUGGER------------------------------------------------------------->