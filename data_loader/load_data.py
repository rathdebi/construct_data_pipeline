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
        """reading CSV file if exist in a given path"""        
        if Path(f"{self.BASE_PATH}/input").exists():
            with os.scandir(f"{self.BASE_PATH}/input") as files_in_basepath:        
                for item in files_in_basepath: 
                    return True   
        else:
            return self.copy_file_from_archive() # copy files from archive folder
    
    def copy_file_from_archive(self):
            if not self.read_csv_file_if_exists():
                shutil.copy(self.ARCHIVE_PATH,f"{self.BASE_PATH}/input")
                return True
            else:
                raise Exception("file not there")

    def get_source_data(self, item, feature_name, **kwargs):    
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
                            df =  self.get_source_data(item,
                                                  'is_red',
                                                   file_name_1 = "white_wine.csv",
                                                   file_name_2 ="red_wine.csv",)
                            data = pd.concat([data,df],axis=0, ignore_index=True)
                data.to_csv(f"{self.BASE_PATH}/input/merged_input_data.csv",index_label="sl_no")
                return data            
        else:
            raise Exception("file can not be loaded!!!")
    
    