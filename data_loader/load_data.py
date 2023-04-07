# load data script

import os
import shutil
import pandas as pd
from pathlib import Path
from config import Configuration


class LoadData(Configuration):
    def __init__(self,BASE_PATH, ARCHIVE_PATH):
        super().__init__(BASE_PATH, ARCHIVE_PATH)


    def read_csv_file_if_exists(self):
        """reading CSV file if exists in a given path"""
        if not Path(f"{self.BASE_PATH}/input").exists():
            os.makedirs(self.BASE_PATH+ f"""/input""")
   
        elif not Path(self.ARCHIVE_PATH).exists():
            os.makedirs(self.BASE_PATH+ f"""/archive""")

        elif not len(list(Path(f"{self.BASE_PATH}/input").glob("*.csv"))) >= 2:
            self.copy_file_from_archive() 
   
        else:
            pass
        return True

        
    def copy_file_from_archive(self):
        """copy files from archive folder to input"""
        if not Path(f"{self.BASE_PATH}/input").exists():
            os.makedirs(self.BASE_PATH + f"""/input""")

        elif not Path(self.ARCHIVE_PATH):
            os.makedirs(self.BASE_PATH + f"""archive""")

        elif len(list(Path(self.ARCHIVE_PATH).glob("*.csv"))) == 2:
            with os.scandir(self.ARCHIVE_PATH) as files:
                for file in files:
                    shutil.copy(file,f"{self.BASE_PATH}/input")
        else:
            raise Exception("archive folder do not contain files!!!")
        

    def merge_source_data(self, item, feature_name, **kwargs):    
        """get source data with a target feature"""        
        df_item = pd.read_csv(item, engine="c", sep=',')
        if item.name == kwargs.get("file_name_1"): # say "first_data.csv"                    
            df_item[feature_name] = 0
        elif item.name == kwargs.get("file_name_2"): # say "second_data.csv"                    
            df_item[feature_name] = 1

        else:  
            raise Exception("item do not exists!!!")
        
        return df_item

    def load_csv_from_base_path(self):
        """load csv file from path"""
        if self.read_csv_file_if_exists(): # file exists
            print(self.read_csv_file_if_exists())           
            with os.scandir(f"{self.BASE_PATH}/input") as files_in_basepath:
                data = pd.DataFrame() 
                for item in files_in_basepath:
                    print("item in this iteration:::", item)
                    if item.name.endswith('.csv'):
                        if Path(f"{self.BASE_PATH}/input/merged_input_data.csv").exists():
                            print("MERGED FILE PRESENT:::WE are all set!!!")
                            return pd.read_csv(f"{self.BASE_PATH}/input/merged_input_data.csv")
                        else:
                            print("MERGED FILE NOT PRESENT:::WE are in process to merge sources!!!")
                            df =  self.merge_source_data(item,
                                                  'is_red',
                                                   file_name_1 = "white_wine.csv",
                                                   file_name_2 ="red_wine.csv",)
                            data = pd.concat([data,df],axis=0) # index based
                data.to_csv(f"{self.BASE_PATH}/input/merged_input_data.csv",index=False)
                return data.sample(frac=1).reset_index(drop=True)          
        else:
            raise Exception("reading csv files from path got an exception!!!")
    
    