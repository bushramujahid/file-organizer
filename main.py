import os # os module is used to interact with the operating system, such as creating folders and moving files
import shutil # shutil module is used to move files from one location to another

# folder path you want to organize
FOLDER_PATH = os.getcwd() # Current working directory


#file type mapping

FILE_TYPE = {
    "Images": [".jpg", ".jpeg", ".png", ".gif", ".bmp"],
    "Documents": [".pdf", ".docx", ".txt", ".xlsx", ".pptx"],
    "Audio": [".mp3", ".wav", ".aac"],
    "Videos": [".mp4", ".avi", ".mov", ".mkv"],
    "Archives": [".zip", ".rar", ".tar", ".gz"],
    "Scripts": [".js", ".html", ".css"],
    "Others": []
}

# create folders for each file type
for folder in FILE_TYPE.keys(): # creates folders for each file type in the current working directory
    folder_path = os.path.join(FOLDER_PATH, folder) # creates a path for each folder
    if not os.path.exists(folder_path): # checks if the folder already exists, if not it creates the folder
        os.makedirs(folder_path) # creates the folder


# organize files in the folder
for file in os.listdir(FOLDER_PATH): # iterates through each file in the current working directory
    file_path = os.path.join(FOLDER_PATH, file) # creates a path for each file


    #skip folders
    if os.path.isdir(file_path): # checks if the file is a directory, if so it skips it
        continue

    # get file extension
    # print(os.path.splitext(file)) # prints the file name and extension
    file_ext = os.path.splitext(file)[1].lower() # gets the file extension and converts it to lowercase

    for folder, extensions in FILE_TYPE.items(): # iterates through each folder and its corresponding file extensions
        if file_ext in extensions: # checks if the file extension is in the list of extensions for the folder
            shutil.move(file_path, os.path.join(FOLDER_PATH, folder, file)) # moves the file to the corresponding folder
            break # breaks the loop once the file is moved

    print("Files organized successfully ✅")  

               
               

