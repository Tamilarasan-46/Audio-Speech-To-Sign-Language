import os
import django
import json
# Manually set Django settings
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "A2SL.settings")
django.setup()

import cloudinary
import cloudinary.uploader
import cloudinary.api
from A2SL.models import UploadedFile  # Now it will work!
from django.db import transaction  # For bulk database saving

# Configure Cloudinary (Replace with your actual Cloudinary credentials)
cloudinary.config(
    cloud_name="dyaqkgsc8",
    api_key="147315349636758",
    api_secret="LxsbXdRs7vVBWcJ2yGE40ylqq00"
)

def upload_folder_to_cloudinary(folder_path):
    """ Uploads all files from a local folder to Cloudinary and returns a dictionary of URLs """
    file_urls = {}

    # Supported file extensions
    IMAGE_EXTENSIONS = (".jpg", ".jpeg", ".png", ".gif", ".bmp", ".webp")
    VIDEO_EXTENSIONS = (".mp4", ".avi", ".mov", ".mkv", ".flv", ".wmv")

    # Loop through all files in the folder
    for filename in os.listdir(folder_path):
        file_path = os.path.join(folder_path, filename)

        if os.path.isfile(file_path):  # Ensure it's a file, not a subfolder
            print(f"Uploading {filename}...")

            # Check if file is an image or video
            if filename.lower().endswith(IMAGE_EXTENSIONS):
                response = cloudinary.uploader.upload(file_path, folder="speech_to_sign_assets")
            elif filename.lower().endswith(VIDEO_EXTENSIONS):
                response = cloudinary.uploader.upload(file_path, folder="speech_to_sign_assets", resource_type="video")
            else:
                print(f"Skipping {filename} (unsupported file type)")
                continue

            file_urls[filename] = response["secure_url"]  # Store URL in dictionary
            print(f"Uploaded: {response['secure_url']}")

    return file_urls

# # Define the path to the assets folder
assets_folder = r"D:\Final Year Project\speech to sign convertor\Audio-Speech-To-Sign-Language\assets"

# # Upload all files and print the Cloudinary URLs
uploaded_files = upload_folder_to_cloudinary(assets_folder)
print("Uploaded Files:", uploaded_files)


with open("cloudinary_urls.json", "w") as json_file:
    json.dump(uploaded_files, json_file, indent=4)

print("Cloudinary URLs saved to cloudinary_urls.json")

    