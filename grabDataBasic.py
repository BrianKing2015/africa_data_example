import requests
import pathlib


def download_data(file_to_download):
    name_of_file = pathlib.Path('sensor_data.csv')
    if not pathlib.Path.exists(name_of_file):
        grab_file = requests.get(url=file_to_download)
        print(grab_file)
        with open("sensor_data.csv", "w") as file:
            file.write(grab_file.text)


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    file_location = 'https://open.africa/dataset/912c4b7c-7ec1-4fe5-8f4e-c0966262020b/resource/5543e478-63c5-4237-8ef9-5deae376c8a6/download/may_2021_sensor_data_archive.csv'
    download_data(file_to_download=file_location)