#File Renaming Program
import os
import shutil

def move_file(new_name,source_folder):
    verification = input('Would you like to create a new folder or transfer to an existing folder? (new/old): ')
    if verification == 'new':
        new_directory = input('Name for new directory: ')
        path = os.path.join(source_folder, new_directory)
        if not os.path.exists(path):
            os.mkdir(path)
            print('New directory', new_directory , 'created')
        else:
            print('Directory', new_directory, 'already exists')
        source_path = os.path.join(source_folder, new_name)
        target_folder = input('Enter new folder address: ')
        target_path = os.path.join(target_folder, new_name)
        shutil.move(source_path, target_path)
        print('File moved')
    elif verification == 'old':
        target_folder = input('Enter folder address: ')
        source_path = os.path.join(source_folder, new_name)
        target_path = os.path.join(target_folder, new_name)
        if os.path.exists(target_path):
            print('File with the same name already exists in this folder')
        else:
            shutil.move(source_path, target_path)
            print('File moved')
    else:
        print('Invalid input')


        
def rename_file():
    source_folder = input('Enter folder address: ')
    for file in os.listdir(source_folder):
        if os.path.isfile(os.path.join(source_folder, file)):
            print('Selected File: ', file)
            f_name, f_ext = os.path.splitext(file)
            f_week = input('Enter week: ')
            f_location = input('Enter location: ')
            f_phrase = input('Enter phrase: ')
            f_name = (f_week + '-' + f_location + '-' + f_phrase)
            new_name = f_name + f_ext
            print('New file name: ' , (new_name))
            os.rename(os.path.join(source_folder, file), os.path.join(source_folder, new_name))
            option = input('Would you like to store the file in a seperate folder?(y/n): ')
            if option == 'y':
                move_file(new_name,source_folder)
            elif option == 'n':
                pass
            else:
                print('Invalid input')
                

def main():
    rename_file()
    print('Done')
