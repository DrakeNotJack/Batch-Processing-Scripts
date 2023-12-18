import os
from openpyxl import Workbook

def extract_folder_names(directory):
    folder_names = []
    for item in os.listdir(directory):
        if os.path.isdir(os.path.join(directory, item)):
            folder_names.append(item)
    return folder_names

def write_to_excel(folder_names, output_file):
    workbook = Workbook()
    sheet = workbook.active
    for index, folder_name in enumerate(folder_names, start=1):
        sheet.cell(row=index, column=1, value=folder_name)
    workbook.save(output_file)

# Replace 'directory_path' with the path to your target directory
directory_path = r'DirectoryPath'
output_file = 'folder_names.xlsx'

folder_names = extract_folder_names(directory_path)
write_to_excel(folder_names, output_file)
