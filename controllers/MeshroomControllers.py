import os
import subprocess
import open3d as o3d
from .BaseController import BaseController
from .FoldersControllers import FoldersControllers

class MeshroomControllers(BaseController):
    def __init__(self, meshroom_path, input_path, output_path):
        super().__init__()
        self.meshroom_path = meshroom_path
        self.input_path = input_path
        self.output_path = output_path
    
    def run_meshroom(self):
        os.environ['PATH'] = '/content/Meshroom-2019.1.0/aliceVision/bin:' + os.environ['PATH']
        os.environ['LD_LIBRARY_PATH'] = '/content/Meshroom-2019.1.0/aliceVision/lib'

        meshroom_command = [
            os.path.join(self.meshroom_path, "meshroom_photogrammetry"),
            "--input", self.input_path,
            "--output", self.output_path
        ]

        try:
            subprocess.run(meshroom_command, check=True)
        except subprocess.CalledProcessError as e:
            return None
        
        zipped_output = FoldersControllers().zip_folder(self.output_path, "output.zip")
        # obj_file = os.path.join(self.output_path, "texturedMesh.obj")

        return zipped_output

    def reduce_meshroom_size(self):
        mesh = o3d.io.read_triangle_mesh(obj_file)
        simplified_meshroom = mesh.simplify_quadric_decimation(target_number_of_triangles=100000)
        o3d.io.write_triangle_mesh(os.path.join(self.output_path, "reducedMesh.obj"), simplified_meshroom)

        obj_file = os.path.join(self.output_path, "reducedMesh.obj")
        
        return obj_file
