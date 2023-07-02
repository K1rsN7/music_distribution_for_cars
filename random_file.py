# Импорт модулей
from random import randint, choice
from os import listdir, mkdir
from os.path import isdir, join
from shutil import move

is_ru = False


# Проверка на корректность ввода директории
def check_folder(string):
    while True:
        folder_def = input(str(string))
        if isdir(folder_def):
            break
        else:
            print("Error: Such a directory does not exist on your computer")
    return folder_def


# Количество папок, которое нужно создать
def count_folder(folder_start):
    count_folder_start = len(listdir(folder_start))
    count_folder_start = count_folder_start // 250
    folder_count = check_folder("Enter the directory where you want to create a folder with files: ")
    while True:
        count_folders = int(input("Enter the number of folders: "))
        if int(count_folders) > count_folder_start:
            break
        else:
            print("Error: Too few folders")

    return folder_count, int(count_folders)


# Основная программа
def main():
    folder_start = check_folder("Enter the directory from which you want to take the files: ")
    files = listdir(folder_start)
    folder_end, count = count_folder(folder_start)
    for number in range(0, count):
        mkdir(folder_end + "\\" + str(number))
    while files:
        file = join(folder_start, choice(listdir(folder_start)))  # Получение файла
        while True:
            num = randint(0, count - 1)
            if len(listdir(str(folder_end) + "\\" + str(num))) < 255:
                move(file, (str(folder_end) + "\\" + str(num)))
                print(
                    file.replace(folder_start + "\\", "").replace("\\", "") + " --> " + str(
                        folder_end) + "\\" + str(
                        num))
                break

        files = listdir(folder_start)

print("The beginning of the program.")
print("-------------------------------")
main()
print("-------------------------------")
print("The program has finished working")
input()
