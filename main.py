import os
import cloudinary
import cloudinary.uploader
import cloudinary.api

# Configure Cloudinary with your credentials
cloudinary.config(
	cloud_name="REPLACE_THIS",
	api_key="REPLACE_THIS",
	api_secret="REPLACE_THIS",
)

upload_preset = "REPLACE_THIS"
image_extensions = (".png", ".jpg", ".jpeg", ".gif", "svg")
video_extensions = (".mp4")
base_dir = "REPLACE_THIS"
cloudinary_prefix = ""

def upload_to_cloudinary(file_path, cloudinary_folder, **options):
	"""Uploads a single image to Cloudinary, preserving folder structure."""
	try:
		response = cloudinary.uploader.upload(
			file_path,
			asset_folder=f"{cloudinary_prefix}{cloudinary_folder}",
			use_filename=True,
			unique_filename=False,
			upload_preset=upload_preset,
			public_id=f"{cloudinary_prefix}{cloudinary_folder}/{'.'.join(file_path.split('/')[-1].split('.')[:-1])}",
			**options,
		)
		print(f"Uploaded: {file_path} to {response['url']}")
	except Exception as e:
		print(f"Error uploading {file_path}: {str(e)}")

if __name__ == "__main__":
	for root, _dirs, files in os.walk(base_dir):
		for file in files:
			if file.lower().endswith(image_extensions):
				cloudinary_folder = os.path.relpath(root, base_dir).replace(os.sep, "/").replace(".", "")
				file_path = os.path.join(root, file)
				upload_to_cloudinary(file_path, cloudinary_folder)
			
			elif file.lower().endswith(video_extensions):
				cloudinary_folder = os.path.relpath(root, base_dir).replace(os.sep, "/").replace(".", "")
				file_path = os.path.join(root, file)
				upload_to_cloudinary(file_path, cloudinary_folder, resource_type="video")
