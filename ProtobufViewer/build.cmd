set /p version_name="please input aoi-sdk version:"

call ".\protoc.exe" --python_out=./ -I./pb ./pb/*.proto

call "pyinstaller.exe" -F -w -n ProtobufViewer .\main.py

copy ".\dist\ProtobufViewer.exe" ".\dist\ProtobufViewer-for-aoi-sdk-v%version_name%.exe"