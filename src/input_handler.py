import shlex

def parse_command(command):
    """
    解析 CLI 指令、拆分參數
    """
    parts = shlex.split(command)  # 解析命令並自動處理引號
    return parts[0], parts[1:]  # 指令名稱, 參數列表
