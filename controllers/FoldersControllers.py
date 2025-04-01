import os
import shutil
import zipfile
from enums.FoldersEnum import FoldersEnum
from fastapi import UploadFile
from .BaseController import BaseController

class FoldersControllers(BaseController):
    def __init__(self):
        super().__init__()
        self.UPLOAD_FOLDER = FoldersEnum.UPLOAD_FOLDER.value
        self.OUTPUT_FOLDER = FoldersEnum.OUTPUT_FOLDER.value

    def create_data_folders(self):
        os.makedirs(self.UPLOAD_FOLDER, exist_ok=True)
        os.makedirs(self.OUTPUT_FOLDER, exist_ok=True)

    def get_output_folder(self):
        return os.path.join(self.base_dir, self.OUTPUT_FOLDER)

    def get_meshroom_path(self):
        return os.path.join(self.base_dir, "Meshroom-2019.1.0")

    def extract_zip_folder(self, zip_file: UploadFile):
        zip_path = os.path.join(self.UPLOAD_FOLDER, zip_file.filename)
        zip_path = os.path.join(self.base_dir, zip_path)

        # Save uploaded file
        with open(zip_path, "wb") as buffer:
            shutil.copyfileobj(zip_file.file, buffer)

        extract_folder = os.path.join(self.UPLOAD_FOLDER, "extracted_images")
        extract_folder = os.path.join(self.base_dir, extract_folder)

        shutil.unpack_archive(zip_path, extract_folder)

        name, ext = os.path.splitext(zip_file.filename)
        input_path = os.path.join(extract_folder, name)

        return input_path
    
    def zip_folder(folder_path, output_filename):
        with zipfile.ZipFile(output_filename, "w", zipfile.ZIP_DEFLATED) as zipf:
            for root, _, files in os.walk(folder_path):
                for file in files:
                    file_path = os.path.join(root, file)
                    zipf.write(file_path, os.path.relpath(file_path, folder_path))
        