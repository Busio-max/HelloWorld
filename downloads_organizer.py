import os
import shutil

# Set the path to the downloads folder
downloads_folder = "C:\\Users\\leagu\\Downloads"

# Set the path to the directory where you want to organize your files
organize_folder = "C:\\Users\\leagu\\OneDrive\\Desktop\\Download_Organization"

# Set the paths to the folders where the files should be organized
image_folder = os.path.join(organize_folder, 'images')
text_folder = os.path.join(organize_folder, 'text')
video_folder = os.path.join(organize_folder, 'videos')
other_folder = os.path.join(organize_folder, 'other')

# Create the folders if they don't already exist
if not os.path.exists(image_folder):
    os.makedirs(image_folder)
if not os.path.exists(text_folder):
    os.makedirs(text_folder)
if not os.path.exists(video_folder):
    os.makedirs(video_folder)
if not os.path.exists(other_folder):
    os.makedirs(other_folder)

# Define a function to determine the file type based on its extension
def get_file_type(file_extension):
    if file_extension in ['.jpg', '.png', '.gif']:
        return 'image'
    elif file_extension in ['.txt', '.doc', '.docx', '.pdf']:
        return 'text'
    elif file_extension in ['.mp4', '.avi', '.mkv']:
        return 'video'
    else:
        return 'other'

# Loop through the files in the downloads folder
for filename in os.listdir(downloads_folder):
    # Get the file extension (e.g. '.txt', '.jpg', etc.)
    file_extension = os.path.splitext(filename)[1]

    # Get the file type based on its extension
    file_type = get_file_type(file_extension)

    # Set the path to the folder where the file should be moved
    if file_type == 'image':
        move_folder = image_folder
    elif file_type == 'text':
        move_folder = text_folder
    elif file_type == 'video':
        move_folder = video_folder
    else:
        move_folder = other_folder

    # Move the file to the appropriate folder
    shutil.move(os.path.join(downloads_folder, filename), move_folder)