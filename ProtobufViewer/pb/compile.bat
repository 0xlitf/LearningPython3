protoc --python_out=../ -I../pb ../pb/*.proto

protoc -I./ -o"smt.pb" --include_imports ./smt.proto
protoc -I./ -o"test.pb" --include_imports ./test.proto

