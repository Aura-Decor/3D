import os
from fastapi import UploadFile, File, APIRouter
from fastapi.responses import FileResponse
from controllers import FoldersControllers, MeshroomControllers
from fastapi.responses import JSONResponse
from enums import ResponseEnums


meshroom_router = APIRouter(
    tags=["api_v1", "meshroom"],
)


@meshroom_router.post("/generate-3d-model")
async def generate_3d_model(file: UploadFile = File(...)):
    folders = FoldersControllers()
    # create folder
    folders.create_data_folders()
    output_folder = folders.get_output_folder()
    # get meshroom path
    meshroom_path = folders.get_meshroom_path()
    # save file to upload folder
    input_path = folders.extract_zip_folder(file)

    # run meshroom
    meshroom = MeshroomControllers(meshroom_path, input_path, output_folder)
    zipped_output = meshroom.run_meshroom()

    # reduce meshroom size
    if zipped_output:
        # obj_file = meshroom.reduce_meshroom_size()
        return FileResponse(zipped_output, filename="3d_model.obj")
    
    else:
        return JSONResponse(
            status_code=400,
            content={
                "message": ResponseEnums.GENERATED_FAILED.value
            }
        )
