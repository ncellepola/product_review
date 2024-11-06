import os
import gdown

# Replace this URL with your own shareable link
google_drive_link = 'https://drive.google.com/file/d/1egAjorWzCalP-mxwz8TpBdqKnnVa4a6w/view?usp=sharing'

# Extract the file ID from the link
def extract_file_id(drive_link):
    if 'id=' in drive_link:
        return drive_link.split('id=')[1]
    elif '/d/' in drive_link:
        return drive_link.split('/d/')[1].split('/')[0]
    else:
        raise ValueError('Could not extract file ID from the provided link.')

file_id = extract_file_id(google_drive_link)

# Construct the download URL
download_url = f'https://drive.google.com/uc?id={file_id}'

# Define the destination directory and file path
destination_dir = os.path.join(os.getcwd(), 'data')
os.makedirs(destination_dir, exist_ok=True)
destination_file = os.path.join(destination_dir, 'Reviews.csv')

# Download the file
print("Downloading the CSV file from Google Drive...")
gdown.download(download_url, destination_file, quiet=False)

print(f"\nReviews.csv has been downloaded to {destination_file}")
