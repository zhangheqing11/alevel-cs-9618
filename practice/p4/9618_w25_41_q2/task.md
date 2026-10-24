# 9618_w25_41 第 2 题 · Train 与 Station：对象容器与容量

## 导读与 Python 接口

从空白程序完成整道题。标识符与文件名照抄 QP；数组须建立真实 list 并以英文注释类型与大小；QP 要求私有的属性使用双下划线。主程序写在 `if __name__ == "__main__":` 下，提示语放在 `input()` 中。指定的算法自行实现，不用内置 sort / index / max 等代劳（D10）。

构造方法、getter 按 QP / MS Python 顺序。无数据文件。QP `Trains[0:9]` 与 D10 要求真实 10 格 list；MS p.19 Python 用空 list 后 append，参考解改为 `[None] * 10`，AddTrain 按 NumberTrains 下标存。这里 empty array 指尚未存列车，不是容量为零。GetTrains 返回字符串（不是 print），QP 明确了行格式和空站消息，测试核对格式；允许末尾空行或行末空格。MS p.25 截图：Station is full 一次，STH 两列车 12ADV/134、33ART/20，NTH 为21VBC/24。

## 英文原题（已对照 QP 原页）

### QP p.4

```text
4

2      A program stores data about trains and train stations using Object-Oriented Programming (OOP).

       The class Train stores the data about the trains:

                                                           Train

        TrainIDNumber : String                        stores the train ID number

        Route : Integer                               stores the route number the train is travelling
        Constructor()                                 initialises TrainIDNumber and Route to the parameter
                                                      values

        GetTrainIDNumber()                            returns the train ID number

        GetRoute()                                    returns the route number the train is travelling


       (a) (i)    Write program code to declare the class Train and its constructor.

                  Do not declare the other methods.

                  All attributes should be private.

                  Use your programming language appropriate constructor.

                  If you are writing in Python, include attribute declarations using comments.

    Save your program as Question2_N25.

    Copy and paste the program code into part 2(a)(i) in the evidence document.
                                                                                                         [4]

           (ii)   The methods GetTrainIDNumber() and GetRoute() return the appropriate attribute.

                  Write program code for GetTrainIDNumber() and GetRoute()

    Save your program.

    Copy and paste the program code into part 2(a)(ii) in the evidence document.
                                                                                                         [3]




© UCLES 2025                                          9618/41/O/N/25
```

### QP p.5

```text
5

    (b) The program is tested with four trains:

               train ID number   route

           12ADV                 134

           33ART                 20

           9FKF                  3

           21VBC                 24


         Write program code to declare an instance of Train for each of the four trains.

 Save your program.

 Copy and paste the program code into part 2(b) in the evidence document.
                                                                                                  [2]




© UCLES 2025                                9618/41/O/N/25                                 [Turn over
```

### QP p.6

```text
6

    (c) The class Station stores the data about the stations:

                                                        Station

      StationID : String                                stores the station ID

      NumberPlatforms : Integer                         stores the number of platforms at the station

      Trains[0:9] : Train                               stores the trains currently at the station platforms

      NumberTrains : Integer                            stores the number of trains currently at the station
                                                        platforms
      Constructor()                                     initialises StationID and NumberPlatforms
                                                        to the parameter values, initialises Trains to an
                                                        empty array and NumberTrains to 0

      GetTrains()                                       returns a string containing data about the trains
                                                        currently at the station platforms

      AddTrain()                                        takes a Train parameter and stores it if there is a
                                                        platform available; each platform can only have one
                                                        train


          (i)   Write program code to declare the class Station and its constructor.

                Do not declare the other methods.

                All attributes should be private.

                Use your programming language appropriate constructor.

                If you are writing in Python, include attribute declarations using comments.

 Save your program.

 Copy and paste the program code into part 2(c)(i) in the evidence document.
                                                                                                               [3]




© UCLES 2025                                        9618/41/O/N/25
```

### QP p.7

```text
7

         (ii)   The method AddTrain() takes a Train parameter. The method compares the
                attributes NumberTrains and NumberPlatforms to identify if there is a platform
                available (a platform currently with no train).

                The method returns FALSE if there are no platforms available.

                If there is a platform available, the method:

                •   stores the Train parameter in the array Trains
                •   updates the appropriate attribute(s)
                •   returns TRUE

                Write program code for AddTrain()

 Save your program.

 Copy and paste the program code into part 2(c)(ii) in the evidence document.
                                                                                                           [4]

        (iii)   The method GetTrains() returns the string "There are no trains" if there are no
                trains at the station platforms.

                If there are trains at the station platforms, the method returns a string in the format:
                    The trains at station <StationID> are:
                    <TrainIDNumber> on route number <Route>

                The line <TrainIDNumber> on route number <Route> is repeated for each train
                at the station platforms.

                For example: If the station with the station ID "NT1" has two trains with the train ID
                numbers "48RTG", "6UFH", the method will produce this output:
                    The trains at station NT1 are:
                    48RTG on route number 43
                    6UFH on route number 12

                Write program code for GetTrains()

 Save your program.

 Copy and paste the program code into part 2(c)(iii) in the evidence document.
                                                                                                           [6]




© UCLES 2025                                     9618/41/O/N/25                                  [Turn over
```

### QP p.8

```text
8

    (d) The program is tested with two stations:

                              number of
                station ID
                              platforms
           STH               2

           NTH               1


          (i)    Write program code to amend the main program to declare an instance of Station for
                 each of the two stations.

 Save your program.

 Copy and paste the program code into part 2(d)(i) in the evidence document.
                                                                                                    [2]

         (ii)    The four trains attempt to stop at the following stations in the order given:

                 •    Train 12ADV, station STH
                 •    Train 33ART, station STH
                 •    Train 9FKF, station STH
                 •    Train 21VBC, station NTH

                 Write program code to amend the main program to:

                 •    add each train to the given station using AddTrain()
                 •    output "Station is full" for any train where the return value indicates it cannot
                      be added to the station
                 •    output the trains at each station using GetTrains()

 Save your program.

 Copy and paste the program code into part 2(d)(ii) in the evidence document.
                                                                                                    [4]

        (iii)    Test your program.

                 Take a screenshot of the output(s).

 Save your program.

 Copy and paste the screenshot(s) into part 2(d)(iii) in the evidence document.
                                                                                                    [2]




© UCLES 2025                                     9618/41/O/N/25
```

## 证据文档对照表

| 证据格 | 行 id | 分 | 交什么 | 自动测（测试名 · 得分点） | 人工核对（得分点） |
|:--|:--|--:|:--|:--|:--|
| Part 2(a)(i) | 9618_w25_41:2(a)(i) | 4 | 代码 | `test_2ai_aii_train` · MP2、MP4 | MP1、MP3 |
| Part 2(a)(ii) | 9618_w25_41:2(a)(ii) | 3 | 代码 | `test_2ai_aii_train` · MP2、MP3 | MP1 |
| Part 2(b) | 9618_w25_41:2(b) | 2 | 代码 | `test_2b_di_main_instances` · MP1、MP2 | — |
| Part 2(c)(i) | 9618_w25_41:2(c)(i) | 3 | 代码 | `test_2ci_station_initial_state` · MP1、MP3 | MP2 |
| Part 2(c)(ii) | 9618_w25_41:2(c)(ii) | 4 | 代码 | `test_2cii_capacity_and_storage` · MP2、MP3、MP4 | MP1 |
| Part 2(c)(iii) | 9618_w25_41:2(c)(iii) | 6 | 代码 | `test_2ciii_empty_string`、`test_2ciii_getters_formatted_return` · MP1、MP2、MP3、MP4、MP5、MP6 | — |
| Part 2(d)(i) | 9618_w25_41:2(d)(i) | 2 | 代码 | `test_2b_di_main_instances` · MP1、MP2 | — |
| Part 2(d)(ii) | 9618_w25_41:2(d)(ii) | 4 | 代码 | `test_2main_call_chain` / `test_2diii_screenshot` · MP1、MP2、MP3、MP4 | — |
| Part 2(d)(iii) | 9618_w25_41:2(d)(iii) | 2 | 截图 | `test_2diii_screenshot` · MP1、MP2 | — |

## 人工核对清单

- [ ] 2(c)(i) MP2: Constructor header (and end) within class taking 2 parameters …

- [ ] 2(a)(i) MP3: Constructor header (and end) within class with 2 parameters …

- [ ] 2(a)(i) MP1: Class header (and end)
- [ ] 2(a)(ii) MP1: One get method header (and end) with no parameter …
- [ ] 2(c)(ii) MP1: Method header (and close) taking one Train parameter
- [ ] 类型与大小的英文注释、函数头及参数、类与方法的归属、QP 要求时的私有属性声明符合本题 MS。混合得分点中能测行为的计自动，头部和类型仍须人工复核。
- [ ] 主程序的调用、返回值使用与分支逐项符合 QP；截图清晰并包含题目要求的输入与输出；提示语语义合适。
- [ ] 指定算法的实现没有用内置函数代劳；文件打开 / 关闭位置及异常范围按 MS 检查。

## MS 得分点编号

测试与上表使用语料 `markpoints[].n`。1 分行按全行计；未印 MP 数字的圆点按原页顺序对应。可选点多于行分值时，自动 / 人工分值按点的权重比例折算；结构整体点仅作人工。
