import os
import requests
import zipfile
from tqdm import tqdm

def download_and_extract_tiny_imagenet():
    """Download and extract the Tiny ImageNet dataset"""
    os.makedirs('./data', exist_ok=True)
    
    if os.path.exists('./data/tiny-imagenet-200'):
        print("Dataset already exists.")
        return
    
    url = 'http://pages.ucsd.edu/~ztu/courses/tiny-imagenet-200.zip'
    print("Downloading Tiny ImageNet dataset...")
    response = requests.get(url, stream=True)
    
    zip_path = './data/tiny-imagenet-200.zip'
    with open(zip_path, 'wb') as f:
        for chunk in tqdm(response.iter_content(chunk_size=1024*1024)):
            if chunk:
                f.write(chunk)
    
    print("Extracting Tiny ImageNet dataset...")
    with zipfile.ZipFile(zip_path, 'r') as zip_ref:
        zip_ref.extractall('./data')
    
    os.remove(zip_path)
    print("Download and extraction complete.")

# Download and extract dataset
download_and_extract_tiny_imagenet()