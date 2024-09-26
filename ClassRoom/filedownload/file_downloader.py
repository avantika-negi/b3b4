import requests


def download_file(url, file_name):
    
    '''function to download a file
    it takes two arguments ,URL and filename
    download_files(url, file_name)
    '''
    file_name=f"{file_name}.{url.split(".")[-1].lower()}"# to generate extension from url
    #send a GET request to the provided URL
    response = requests.get(url)
    
    
    # Check if the request with successful (status code 200)
    if response.status_code == 200:
        # Open a local file in binary rite mode and save the content
        with open(file_name , 'wb') as file:
            file.write(response.content)
        print(f"file'{file_name}'download successfully.")
    else:
        print(f"failed to download file. status code:{response.status_code}")
        
        
if __name__ == "__main__":
    url ='https://www.python.org/static/img/psf-logo.png'
    file_name ='file'
    download_file(url , file_name)