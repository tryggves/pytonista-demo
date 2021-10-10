# Google Protocol Buffers Example

Following the python tutorial see:
https://developers.google.com/protocol-buffers/docs/pythontutorial

Generate the protobuf file from the .proto definition by running the
command:

```commandline
export SRC_DIR=/Users/tryggve/Develop/pytonista-demo/protobuf
protoc -I=$SRC_DIR --python_out=$SRC_DIR $SRC_DIR/addressbook.proto
```
