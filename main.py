import os
from datetime import datetime


def create_folder_and_files(folder_name):
    base_folder = os.getcwd()
    new_folder_path = os.path.join(base_folder, folder_name)

    if os.path.exists(new_folder_path):
        return f"Folder '{folder_name}' already exists"
    else:
        os.mkdir(new_folder_path)
        file_names = ["name.txt", "content.txt", "times.txt", "other.txt"]
        for file_name in file_names:
            file_path = os.path.join(new_folder_path, file_name)
            with open(file_path, 'w') as file:
                file.write(f"This is the {file_name} file for folder '{folder_name}'")
        return f"Folder '{folder_name}' created successfully with 4 text files"


def edit_file_in_folder(folder_name, file_name, new_content):
    base_folder = os.getcwd()
    file_path = os.path.join(base_folder, folder_name, file_name)
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    content_with_timestamp = f"\n{new_content}\n\nWritten on: {timestamp}\n"
    if os.path.exists(file_path):
        with open(file_path, 'a') as file:
            file.write(content_with_timestamp)
        print(f"Content of '{file_name}' in folder '{folder_name}' edited.")
    else:
        print(f"Folder '{folder_name}' or '{file_name}' does not exist.")


def print_all_folders():
    folders = [item for item in os.listdir() if os.path.isdir(item) and not item.startswith(".")]
    for i, folder in enumerate(folders, start=1):
        if i < len(folders):
            print(f"{i}. {folder}", end="\t")
        else:
            print(f"{i}. {folder}")


while True:
    choice = input("\n\n请选择要进行的操作：\na. 新建烂梗\nb. 编辑烂梗\nc. 查看烂梗\ne. 退出程序\n")
    if choice == 'a':
        shitname = input('请输入烂梗名称')
        create_folder_and_files(shitname)
    elif choice == 'b':
        folder_name = input("请输入要编辑的烂梗名称")
        file_name = input("请输入要编辑的项目")
        new_content = input("请输入要添加的内容")
        edit_file_in_folder(folder_name, file_name, new_content)
    elif choice == 'c':
        print_all_folders()
    elif choice == 'e':
        print("程序已退出。")
        break
    else:
        print("输入无效，请重新输入。")
