import roboflow

rf = roboflow.Roboflow(api_key=YOUR_API_KEY_HERE)
workspace = rf.workspace("WORKSPACE_URL")
workspace.upload_dataset(
    
    num_workers=10,
    project_license="Interview",
    project_type="object-detection",
    batch_name=None,
    num_retries=0
)
