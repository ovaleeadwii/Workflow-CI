import os
from pydrive2.auth import GoogleAuth
from pydrive2.drive import GoogleDrive


def upload_file(drive, local_path, folder_id=None):
    metadata = {"title": os.path.basename(local_path)}
    if folder_id:
        metadata["parents"] = [{"id": folder_id}]

    file_drive = drive.CreateFile(metadata)
    file_drive.SetContentFile(local_path)
    file_drive.Upload()
    print(f"Uploaded: {local_path}")


def main():
    gauth = GoogleAuth()
    gauth.LoadServiceConfigFile("credentials.json")
    gauth.ServiceAuth()

    drive = GoogleDrive(gauth)

    folder_id = os.getenv("GDRIVE_FOLDER_ID")

    upload_targets = [
        "latest_run_id.txt",
    ]

    for target in upload_targets:
        if os.path.exists(target):
            upload_file(drive, target, folder_id)

    for root, dirs, files in os.walk("MLProject/mlruns"):
        for file in files:
            path = os.path.join(root, file)
            upload_file(drive, path, folder_id)


if __name__ == "__main__":
    main()