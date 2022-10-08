#!/usr/bin/python
# -*- coding: UTF-8 -*-
# Author: leion.tong@outlook.com
# Description: python模块用例：os。

import os

print("获取指定文件的所在目录")
target_file = "C:/Users/leion/Downloads/Untitled-1.py"
print("target_file: ", target_file)
print("dir_of_target_file: ", os.path.dirname(target_file))

print("获取指定文件夹的父目录")
target_folder = "C:/Users/leion/Downloads/"
print("target_folder: " , target_folder)
print("parent_dir_of_target_folder: ", os.path.dirname(os.path.abspath(target_folder).replace('\\', '/')))

print("获取当前运行脚本的完整路径(绝对路径)")
print("full_path_of_current_script: ", os.path.abspath(__file__))

print("获取当前运行脚本的所在目录")
print("dir_of_current_script: ", os.path.dirname(__file__))

print("获取当前运行脚本的父目录")
print("parent_dir_of_current_script: ", os.path.dirname(os.path.dirname(__file__)))
print("parent_dir_of_current_script: ", os.path.dirname(os.path.abspath(__file__)))

print("获取当前运行脚本的工作目录")
print("work_dir: ", os.getcwd())
