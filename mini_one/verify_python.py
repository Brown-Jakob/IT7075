from pathlib import Path
import sys

project_dir = Path(__file__).resolve().parent
print("Python script executed successfully")
print(f"Python version: {sys.version.split()[0]}")
print(f"Project directory: {project_dir}")
