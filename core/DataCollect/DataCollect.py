# 2020 03 22
# Feature : 데이터가 수집된 일시 ,총 프로세스 ,총 쓰레드 갯수

import os
import csv
import psutil
from time import localtime

def dataCollecting(exit_flag):
    cur_time = str(localtime().tm_min) + ":" + str(localtime().tm_sec)
    # 0~10분 까지
    if len(cur_time.split(":")[0]) == 1:
        print("0분대")
        train_path = "./core/csvDataSet/TrainSet0.csv"
        if os.path.isfile(train_path):
            try:
                f = open(train_path, "a+", newline='')
                wr = csv.writer(f)

                # 총 프로세스 , 총 쓰레드 갯수
                tot_process_number = len([x for x in psutil.pids()])
                tot_thread_number = sum([x.num_threads() for x in psutil.process_iter()])
                memory_usage = psutil.virtual_memory()
                print(cur_time, tot_process_number, tot_thread_number, memory_usage.percent)

                wr.writerow([cur_time, tot_process_number, tot_thread_number, memory_usage.percent])
                f.close()
            except Exception as e:
                print(e)
        else:
            f = open(train_path, "a+", newline='')
            wr = csv.writer(f)
            wr.writerow(["time", "process", "threads", "memory_usage"])
            f.close()

    elif len(cur_time.split(":")[0]) == 2:
        if int(cur_time.split(":")[0][0]) == 1:
            print("10분대")
            train_path = "./core/csvDataSet/TrainSet1.csv"
            if os.path.isfile(train_path):
                try:
                    f = open(train_path, "a+", newline='')
                    wr = csv.writer(f)

                    # 총 프로세스 , 총 쓰레드 갯수
                    tot_process_number = len([x for x in psutil.pids()])
                    tot_thread_number = sum([x.num_threads() for x in psutil.process_iter()])
                    memory_usage = psutil.virtual_memory()
                    print(cur_time, tot_process_number, tot_thread_number, memory_usage.percent)

                    wr.writerow([cur_time, tot_process_number, tot_thread_number, memory_usage.percent])
                    f.close()
                except Exception as e:
                    print(e)
            else:
                f = open(train_path, "a+", newline='')
                wr = csv.writer(f)
                wr.writerow(["time", "process", "threads", "memory_usage"])
                f.close()


        elif int(cur_time.split(":")[0][0]) == 2:
            print("20분대")
            train_path = "./core/csvDataSet/TrainSet2.csv"
            if os.path.isfile(train_path):
                try:
                    f = open(train_path, "a+", newline='')
                    wr = csv.writer(f)

                    # 총 프로세스 , 총 쓰레드 갯수
                    tot_process_number = len([x for x in psutil.pids()])
                    tot_thread_number = sum([x.num_threads() for x in psutil.process_iter()])
                    memory_usage = psutil.virtual_memory()
                    print(cur_time, tot_process_number, tot_thread_number, memory_usage.percent)

                    wr.writerow([cur_time, tot_process_number, tot_thread_number, memory_usage.percent])
                    f.close()
                except Exception as e:
                    print(e)
            else:
                f = open(train_path, "a+", newline='')
                wr = csv.writer(f)
                wr.writerow(["time", "process", "threads", "memory_usage"])
                f.close()

        elif int(cur_time.split(":")[0][0]) == 3:
            print("30분대")
            train_path = "./core/csvDataSet/TrainSet3.csv"
            if os.path.isfile(train_path):
                try:
                    f = open(train_path, "a+", newline='')
                    wr = csv.writer(f)

                    # 총 프로세스 , 총 쓰레드 갯수
                    tot_process_number = len([x for x in psutil.pids()])
                    tot_thread_number = sum([x.num_threads() for x in psutil.process_iter()])
                    memory_usage = psutil.virtual_memory()
                    print(cur_time, tot_process_number, tot_thread_number, memory_usage.percent)

                    wr.writerow([cur_time, tot_process_number, tot_thread_number, memory_usage.percent])
                    f.close()
                except Exception as e:
                    print(e)
            else:
                f = open(train_path, "a+", newline='')
                wr = csv.writer(f)
                wr.writerow(["time", "process", "threads", "memory_usage"])
                f.close()

        elif int(cur_time.split(":")[0][0]) == 4:
            print("40분대")
            train_path = "./core/csvDataSet/TrainSet4.csv"
            if os.path.isfile(train_path):
                try:
                    f = open(train_path, "a+", newline='')
                    wr = csv.writer(f)

                    # 총 프로세스 , 총 쓰레드 갯수
                    tot_process_number = len([x for x in psutil.pids()])
                    tot_thread_number = sum([x.num_threads() for x in psutil.process_iter()])
                    memory_usage = psutil.virtual_memory()
                    print(cur_time, tot_process_number, tot_thread_number, memory_usage.percent)

                    wr.writerow([cur_time, tot_process_number, tot_thread_number, memory_usage.percent])
                    f.close()
                except Exception as e:
                    print(e)
            else:
                f = open(train_path, "a+", newline='')
                wr = csv.writer(f)
                wr.writerow(["time", "process", "threads", "memory_usage"])
                f.close()

        elif int(cur_time.split(":")[0][0]) == 5:
            print("50분대")
            train_path = "./core/csvDataSet/TrainSet5.csv"
            if os.path.isfile(train_path):
                try:
                    f = open(train_path, "a+", newline='')
                    wr = csv.writer(f)

                    # 총 프로세스 , 총 쓰레드 갯수
                    tot_process_number = len([x for x in psutil.pids()])
                    tot_thread_number = sum([x.num_threads() for x in psutil.process_iter()])
                    memory_usage = psutil.virtual_memory()
                    print(cur_time, tot_process_number, tot_thread_number, memory_usage.percent)

                    wr.writerow([cur_time, tot_process_number, tot_thread_number, memory_usage.percent])
                    f.close()
                except Exception as e:
                    print(e)
            else:
                f = open(train_path, "a+", newline='')
                wr = csv.writer(f)
                wr.writerow(["time", "process", "threads", "memory_usage"])
                f.close()

def warning_memory_singal():
    data_list = list()
    dataTopName = list()

    for x in psutil.process_iter(attrs=['name', 'username', 'memory_percent']):
        if (x.info['name'] in "pycharm64.exe") or (x.info['name'] in "python.exe"):
            pass
        else:
            data_list.append([x.info['memory_percent'], x.info['name']])

    tempList = [[str(data_list[y][0]), data_list[y][1]] for y in range(0, len(data_list))]
    floatList = [[float(tempList[z][0]), tempList[z][1]] for z in range(0, len(tempList))]

    dataTop = sorted(floatList, reverse=True)

    for _ in range(0, 5):
        dataTopName.append(dataTop[_][1])

    returnStringValue = ", ".join(dataTopName)

    return returnStringValue


if __name__ == '__main__':
    dataCollecting("true")