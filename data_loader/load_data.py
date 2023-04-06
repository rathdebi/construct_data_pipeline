# load data script

import os
import shutil
import pandas as pd
from pathlib import Path
from config import Configuration


class LoadData(Configuration):
    def __init__(self,BASE_PATH, ARCHIVE_PATH):
        super().__init__(BASE_PATH, ARCHIVE_PATH)

    # def read_csv_file_if_exists(self):
    #     """reading CSV file if exist in a given path"""        
    #     if Path(f"{self.BASE_PATH}/input").exists():
    #         with os.scandir(f"{self.BASE_PATH}/input") as files_in_basepath:        
    #             for item in files_in_basepath: 
    #                 return True   
    #     else:
    #         return self.copy_file_from_archive() # copy files from archive folder

    def read_csv_file_if_exists(self):
        """reading CSV file if exist in a given path"""
        if not os.path.exists(self.BASE_PATH+ "input"):
            os.makedirs(self.BASE_PATH + "input")
   
        elif not os.path.exists(self.ARCHIVE_PATH):
            os.makedirs(self.BASE_PATH + "archive")

        elif Path(f"{self.BASE_PATH}/input").glob("*.csv"):
            return True
   
        else:
            return self.copy_file_from_archive(self.BASE_PATH, self.ARCHIVE_PATH) 

        
    def copy_file_from_archive(self):
        """copy files from archive folder to input"""
        if not os.path.exists(self.BASE_PATH+ "input"):
            os.makedirs(self.BASE_PATH + "input")

        elif not os.path.exists(self.ARCHIVE_PATH):
            os.makedirs(self.BASE_PATH + "archive")

        elif Path(self.ARCHIVE_PATH).glob("*.csv"):
            with os.scandir(self.ARCHIVE_PATH) as files:
                for file in files:
                    shutil.copy(file,f"{self.BASE_PATH}/input")
        else:
            raise Exception("file not there in archive!!!")


    # def copy_file_from_archive(self):
    #         if not self.read_csv_file_if_exists():
    #             shutil.copy(self.ARCHIVE_PATH,f"{self.BASE_PATH}/input")
    #             return True
    #         else:
    #             raise Exception("file not there")

    def merge_source_data(self, item, feature_name, **kwargs):    
        """get source data with a target feature"""        
        df_item = pd.read_csv(item, engine="c", sep=',')    
        if item.name == kwargs.get("file_name_1"): # say "first_data.csv"                    
            df_item[feature_name] = 0
    
        elif item.name == kwargs.get("file_name_2"): # say "second_data.csv"                    
            df_item[feature_name] = 1  
          
        else:  
            raise Exception("item do not exists")
        
        return df_item

    def load_csv_from_base_path(self):
        """load csv file from path"""
        if self.read_csv_file_if_exists(): # file exists              
            with os.scandir(f"{self.BASE_PATH}/input") as files_in_basepath:
                print(f"{self.BASE_PATH}/input")
                data = pd.DataFrame() 
                for item in files_in_basepath:
                    if item.name.endswith('.csv'):
                        if Path(f"{self.BASE_PATH}/input/merged_input.csv").exists():
                            data = pd.read_csv(f"{self.BASE_PATH}/input/merged_input.csv")
                        else:
                            df =  self.merge_source_data(item,
                                                  'is_red',
                                                   file_name_1 = "white_wine.csv",
                                                   file_name_2 ="red_wine.csv",)
                            data = pd.concat([data,df],axis=0, ignore_index=True)
                data.to_csv(f"{self.BASE_PATH}/input/merged_input_data.csv",index_label="sl_no")
                return data            
        else:
            raise Exception("file can not be loaded!!!")
    
    