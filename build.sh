#!/bin/bash

echo "建置開始..."
conda activate base

# check tinyDB
if ! python -c "import tinydb" &> /dev/null; then
    echo "未檢測到tinyDB，開始安裝..."
    conda install tinydb
else
    echo "tinyDB已安裝，跳過安裝步驟。"
fi

echo "建置完成！"