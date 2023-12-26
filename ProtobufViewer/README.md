# ProtobufViewer

# Build
## Requirement
- python3
- pyqt5
## Install dependency packages
`pip install -r ./requirements.txt `

## Compile Protobuf
`protoc --python_out=./ -I./pb ./pb/*.proto`

## Run
`python main.py`
# Package
`pyinstaller -F -w -n ProtobufViewer .\main.py`