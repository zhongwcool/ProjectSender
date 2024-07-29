import configparser
import os
import time

import serial


# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.

def ensure_config_file_exists(config_file_path, default_settings):
    config = configparser.ConfigParser()

    # 检查配置文件是否存在
    if not os.path.exists(config_file_path):
        # 配置文件不存在，使用默认配置创建它
        config['SerialPort'] = default_settings
        with open(config_file_path, 'w') as configfile:
            config.write(configfile)
    else:
        # 配置文件存在，读取现有配置
        config.read(config_file_path)

    return config


def send_hex_line(serial_connection, hex_line):
    # 去除空白字符并转换成字节
    byte_array = bytes.fromhex(hex_line.strip())
    # 打印即将发送的内容
    print(f"Sending: {byte_array.hex().upper()}")
    # 通过串口发送字节
    serial_connection.write(byte_array)


def print_hi(file_path):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {file_path}')  # Press Ctrl+F8 to toggle the breakpoint.

    # 默认配置
    default_serial_settings = {
        'Port': 'COM11',  # Windows设备串口名称
        'BaudRate': '9600',  # 波特率
        'Timeout': '0.5'  # 超时设置
    }

    # 配置文件路径
    config_file_path = 'serial.ini'

    # 确保配置文件存在
    config = ensure_config_file_exists(config_file_path, default_serial_settings)

    # 读取配置
    serial_port = config.get('SerialPort', 'Port')
    baud_rate = config.getint('SerialPort', 'BaudRate')
    timeout = config.getfloat('SerialPort', 'Timeout')

    # 检查文件是否存在
    if not os.path.exists(file_path):
        print(f"Error: The file {file_path} does not exist.")
        time.sleep(100)
    else:
        ser = None  # 初始化ser变量
        # 尝试打开串口
        try:
            ser = serial.Serial(serial_port, baud_rate, timeout=timeout)
            # 读取文件并逐行发送
            with open(file_path, 'r') as file:
                for line in file:
                    send_hex_line(ser, line)
                    time.sleep(0.5)  # 在发送下一行前等待0.5秒

        except serial.SerialException as e:
            print(f"{e}")
        finally:
            # 确保ser已被实例化并且串口已经打开
            if ser and ser.is_open:
                ser.close()


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print_hi('hex_data.txt')

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
