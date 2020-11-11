'''this sort script can copy unique files from "copy" folder to "paste" folder.
"copy" folder is the folder from which we are going to copy files.
"paste" folder is the folder where we are going to save unique files from "copy" folder.
unique files are files which present in "copy" folder but absent in "paste" folder.
This script can help to keep in the "paste" folder the same files like are in the "copy" folder.
It can be useful for backup
''' 

import os,shutil, sys

def file_list(address):
    #create list of files in appropriate folder
    arr_file=os.listdir(address)
    return arr_file

def new_files(list_1,list_2):
     #create a list with unique files by comparison two lists
    new_files=[]
    for i in list_1:
        if i in list_2:
            continue
        else:
           new_files.append(i)
    return new_files

def writing(list):
    #copy unique files from "copy" folder to "paste" folder
    for file in list:
        try:
            shutil.copy2(copy_folder+"\\"+file,paste_folder)
        except IOError as error:
            print(error)
            sys.exit
    print('Done')

#get addresses of "copy" and "paste" folders from user
copy_folder=input('please input path of folder from which files should to copy \n')
paste_folder=input('please input path of folder where new files shold be copy \n')

# check information from user
if copy_folder==paste_folder:
    print("You entered the same folders in both cases.\n Please try again.")
    sys.exit
else:
    pass

#create two lists with appropriate files in both folders: "copy" and "paste" folder
copy_folder_list=file_list(copy_folder)
paste_folder_list=file_list(paste_folder)

#creation of list with unique files
files_for_copy=new_files(copy_folder_list, paste_folder_list)

# save unique files in "paste" folder
writing(files_for_copy)