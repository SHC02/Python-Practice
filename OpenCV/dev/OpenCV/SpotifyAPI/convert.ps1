#set-executionpolicy remotesigned // giving execution policy for windows 10 on powershell
jupyter nbconvert --output-dir='./client' --to python notebooks/spotify_client.ipynb
