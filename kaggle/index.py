import os
import subprocess

kaggle_json_path = os.path.join("kaggle.json")
os.chmod(kaggle_json_path, 0o600)

subprocess.run(["kaggle", "datasets", "download", "-d", "leadbest/googlenewsvectorsnegative300"], check=True)
subprocess.run(["unzip", "googlenewsvectorsnegative300.zip"], check=True)