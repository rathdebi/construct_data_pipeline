# main pipeline script
from constants import BASE_PATH, ARCHIVE_PATH
from load_data import LoadData

# create load data object 
def main():
    load_data = LoadData(BASE_PATH=BASE_PATH, ARCHIVE_PATH=ARCHIVE_PATH)
    input_data = load_data.load_csv_from_base_path()
    print(input_data)

if __name__  == "__main__":
    main()