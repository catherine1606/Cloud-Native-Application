#!/bin/bash

echo "建置開始..."

# check tinyDB
if ! python -c "import tinydb" &> /dev/null; then
    echo "未檢測到tinyDB，開始安裝..."
    pip install tinydb
else
    echo "tinyDB已安裝，跳過安裝步驟。"
fi

echo "建置完成！"