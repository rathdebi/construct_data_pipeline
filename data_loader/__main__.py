from load_data import LoadData


# create LoadData object
def main():
    load_data = LoadData()
    input_data = load_data.load_csv_from_base_path()
    print(input_data)

if "__name__" == "__main__":
    main()