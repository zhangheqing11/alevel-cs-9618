# 9618_s23_42 第 3 题 · Employee / Manager：工资与奖金

标识符及文件名照 QP；数组建成真实 list，并用英文注释注明类型与大小（D10）。从空文件完成，主程序放在 `if __name__ == "__main__":` 下，提示写在 `input("…")` 中。按 `make try EX=practice/p4/9618_s23_42_q3 K=3b` 可分问测试。QP 要求私有属性时使用 `self.__Name`；未要求时可按 MS 使用公有属性；测试允许正确的循环实现，不靠指定变量名或固定提示语判分。
来源：QP pp.8–12；MS pp.23–37。已看 QP 全题原页、MS Python 范例原页；证据格与官方 evidence.doc 逐格核对。

## 英文原题（对照 QP 原页转写）

```text
8

3   A company needs a computer program to store data about its employees.

    Part of the program is being written using object‑oriented programming.

    The class Employee stores data about the employees. Each employee has an employee number,
    a job title and hourly pay rate. The class will also store the amount they are paid each week over a
    52‑week year in a 1D array.

                                               Employee
 HourlyPay : REAL                                 stores the amount each employee gets paid each
                                                  hour

 EmployeeNumber : STRING                          stores the employee’s unique number

 JobTitle : STRING                                stores the employee’s job title

 PayYear2022 : ARRAY[0:51] OF REAL                stores the amount the employee has been paid each
                                                  week
 Constructor()                                    initialises HourlyPay, EmployeeNumber and
                                                  JobTitle from the values passed as parameters
                                                  initialises all 52 elements in PayYear2022 to 0.0

 GetEmployeeNumber()                              returns the employee number

 SetPay()                                         takes the week number and number of hours worked
                                                  that week as parameters
                                                  calculates and stores the pay for that week in
                                                  PayYear2022

 GetTotalPay()                                    returns the total of all the values in PayYear2022


    (a) (i)     Write program code to declare the class Employee.

                You only need to declare the class and its constructor. Do not declare any other methods.

                Use your programming language appropriate constructor.

                If you are writing program code in Python, include attribute declarations using comments.

 Save your program as Question3_J2023.

 Copy and paste the program code into part 3(a)(i) in the evidence document.
                                                                                                       [5]

         (ii)   The method GetEmployeeNumber() returns the employee number.

                Write program code for the method GetEmployeeNumber().

 Save your program.

 Copy and paste the program code into part 3(a)(ii) in the evidence document.
                                                                                                       [2]



        (iii)   The method SetPay():

                •   takes a week number and the number of hours worked that week as parameters
                •   calculates the pay for that week by multiplying the hourly pay by the number of
                    hours worked that week
                •   stores the calculated pay in the appropriate index for that week in PayYear2022.

                Write program code for the method SetPay().

 Save your program.

 Copy and paste the program code into part 3(a)(iii) in the evidence document.
                                                                                                 [3]

        (iv)    The method GetTotalPay() returns the total of all the values in PayYear2022.

                Write program code for the method GetTotalPay().

 Save your program.

 Copy and paste the program code into part 3(a)(iv) in the evidence document.
                                                                                                 [2]






    (b) The child class Manager inherits from the parent class Employee.

         A manager gets a bonus. This bonus value is a percentage, for example 10.0%.
         When calculating the pay, the number of hours the manager worked that week is increased
         by the bonus value.

                                                 Manager
                                    stores the bonus value, for example 10.0 represents a
      BonusValue : REAL
                                    10.0% increase
      Constructor()                 takes bonus value, hourly pay, employee number and job title
                                    as parameters
                                    initialises BonusValue to its parameter value

      SetPay()                      takes the week number and number of hours worked as
                                    parameters
                                    increases the number of hours worked by the bonus value
                                    calls the SetPay() method from the parent class


          (i)   Write program code to declare the class Manager.

                You only need to declare the class and its constructor. Do not declare any other methods.

                Use your programming language appropriate constructor.

                If you are writing in Python, include attribute declarations using comments.

 Save your program.

 Copy and paste the program code into part 3(b)(i) in the evidence document.
                                                                                                      [4]

         (ii)   The Manager method SetPay() overrides the method from the parent class and:

                •   takes the week number and number of hours worked as parameters
                •   increases the number of hours worked by the bonus value
                •   calls SetPay() from the parent class.

                Write program code for the method SetPay().

 Save your program.

 Copy and paste the program code into part 3(b)(ii) in the evidence document.
                                                                                                      [3]






    (c) The main program has a global 1D array, EmployeeArray, to store data about
        eight employees. Each employee is stored as an object of type Employee.

         The file Employees.txt stores data about the employees, in the order:

         •     hourly pay
         •     employee number
         •     bonus value (where included)
         •     job title.

         Only employees who are managers have a bonus value saved. For example:

         •     The first employee is a Junior Developer, with employee number 12452 and an hourly
               pay of $15.22. This employee does not have a bonus value.
         •     The third employee is an Interface Manager, with employee number 02586 and an hourly
               pay of $22.50. This employee has a bonus value of 5.25%.

         Write the main program to:

         •     declare the array to store data about 8 employees
         •     read in the data from the file for each employee
         •     instantiate each employee as either Employee (if the employee does not have a bonus
               value) or Manager (if the employee has a bonus value).

 Save your program.

 Copy and paste the program code into part 3(c) in the evidence document.
                                                                                                [7]

    (d) The file HoursWeek1.txt stores the number of hours each employee has worked in week 1,
        in the order:

         •     employee number
         •     number of hours worked.

         For example, the first set of data is for employee 21548 who has worked 50.0 hours.

         The procedure EnterHours():

         •     reads in the values from the file
         •     finds the location of each employee in EmployeeArray
         •     calls the method SetPay() for each employee.

         Write program code for EnterHours().

 Save your program.

 Copy and paste the program code into part 3(d) in the evidence document.
                                                                                                [4]






       (e) (i)       The main program needs to call EnterHours() and use the method GetTotalPay()
                     to output the employee number and total pay for each of the eight employees.

                     Amend the main program to perform these tasks.

 Save your program.

 Copy and paste the program code into part 3(e)(i) in the evidence document.
                                                                                                                                                         [2]

             (ii)    Test your program.

                     Take a screenshot of the output.

 Save your program.

 Copy and paste the screenshot into part 3(e)(ii) in the evidence document.
                                                                                                                                                         [1]
```

## Python 接口与 QP / MS 差异

构造参数采用 MS：`Employee(EmpNum, Pay, Job)` 与 `Manager(EmpNum, Pay, Job, Bonus)`。全局 `EmployeeArray` 为 8 个对象的 list；`EnterHours()` 无参数。周编号 1–52 映射 0–51，不测试 QP 未定义的无效周。MS p.35 / p.36 将 EmployeeArray 写成 Employees，p.36 `for(Y in range(0,8):` 是语法笔误；统一修正，输入 ID 保持 STRING、去行尾，完整读取工时对并关闭文件。p.29 的百分比公式照原页实现。p.37 截图顺序跟工时文件不同于 EmployeeArray；QP 未规定输出顺序，自动测核对全部 ID/总额映射，接受浮点显示差异，不强制排序。文件开关位置及调用结构人工补核。3(c) 8 个可选点最多 7 分，3(d) 6 个可选点最多 4 分。

## 证据文档对照表

| 证据格 | 行 id | 分 | 内容 | 自动测（测试名 · 语料得分点） | 人工核对 |
|:--|:--|--:|:--|:--|:--|
| Part 3(a)(i) | 9618_s23_42:3(a)(i) | 5 | 代码 | `test_3a_i_ii_employee_initial_state` · MP2, MP4, MP5 | MP1, MP3 |
| Part 3(a)(ii) | 9618_s23_42:3(a)(ii) | 2 | 代码 | `test_3a_i_ii_employee_initial_state` · MP2 | MP1 |
| Part 3(a)(iii) | 9618_s23_42:3(a)(iii) | 3 | 代码 | `test_3a_iii_iv_set_week_and_total` · MP2, MP3 | MP1 |
| Part 3(a)(iv) | 9618_s23_42:3(a)(iv) | 2 | 代码 | `test_3a_iii_iv_set_week_and_total` · MP1, MP2 | — |
| Part 3(b)(i) | 9618_s23_42:3(b)(i) | 4 | 代码 | `test_3main_call_chain` / `test_3b_inherits_and_calls_parent_with_bonus` · MP1, MP3, MP4 | MP2 |
| Part 3(b)(ii) | 9618_s23_42:3(b)(ii) | 3 | 代码 | `test_3b_inherits_and_calls_parent_with_bonus` · MP2, MP3 | MP1 |
| Part 3(c) | 9618_s23_42:3(c) | 7 | 代码 | `test_3c_load_employees` / `test_3c_missing_employees` · MP1, MP2, MP3, MP4, MP5, MP6, MP7, MP8 | — |
| Part 3(d) | 9618_s23_42:3(d) | 4 | 代码 | `test_3d_enterhours_matches_ids` / `test_3d_missing_hours` · MP1, MP2, MP3, MP4, MP5, MP6 | — |
| Part 3(e)(i) | 9618_s23_42:3(e)(i) | 2 | 代码 | `test_3main_call_chain` / `test_3e_ii_screenshot_all_pays` · MP1, MP2 | — |
| Part 3(e)(ii) | 9618_s23_42:3(e)(ii) | 1 | 截图 | `test_3e_ii_screenshot_all_pays` · 整行 | — |

自动覆盖表示行为得到验证；混合点里的函数头、注释、调用结构仍须补核，不能凭测试自动授予考试分数。可选得分点多于该行满分时，按 markpoints[].marks 加权后按该行满分比例折算。

## 人工核对清单

- [ ] 3(a)(i) MP1：Class Employee declaration (and end where appropriate)
- [ ] 3(a)(i) MP3：Constructor header within class (and end where appropriate) taking 3 parameters …
- [ ] 3(a)(ii) MP1：Get method header (and end) with no parameters …
- [ ] 3(a)(iii) MP1：Method header (and close) with two parameters (week number and number of hours)
- [ ] 3(b)(i) MP2：Constructor within class (and end) taking 4 parameters…
- [ ] 3(b)(ii) MP1：Method SetPay header (and end) taking 2 parameters
- [ ] 所有方法头、主程序的调用顺序、返回值接收与题给标识符符合该题 MS；属性注释写明类型，QP 要求私有的属性不改成公有属性。
- [ ] 题目指定算法自行实现，不用 `in`、`sort()`、`sorted()`、`index()`、`max()` 等代劳（D10 ③；本项人工核对）。
- [ ] 截图清晰，输入、输出及要求的文件名可见；appropriate message 的语义与状态一致（措辞不限）。

## 得分点编号（D37 ②）

编号采用语料 markpoints[].n；1 分且未拆分的行记“整行”。本题 MS 圆点顺序与语料一致；若 MS 给可选点上限，按该行上限计分。
