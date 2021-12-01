# CSV and File Handing Homework
### Dairui Zhang

## ABOUT
In this assignment, in order to consolidate the knowledge I have learned so far and learn how to read CSV, I created a new repository and wrote a simple calculator myself.
The main.py did the following:

- Prepare the test method. My test method is just an ordinary function with return.
I know that we should use "test_" to name the function and assert to test. Finally, run pylint. But I didn't do it because:
  1. I have trouble generating reports with pylint. I need to output some specified log contents. I didn't figure out how to output the report with pylint.
  2. I can achieve the same function with return, and it is convenient to output the specified log content, because we can write some branches according to the different results of return.
  3. Of course, I will continue to study the correct practice of pylint.


- Prepare the watchdog to monitor the output folder, which can detect the creation and modification of files.


- Prepare the CSV file of test file. I put the results of addition, subtraction, multiplication and division in a CSV table, which I think is more convenient when writing code.
  But I later learned that this approach may not be very good. Because once it makes an error, it will affect the global test. But in this assignment, please allow me to do so. I also learned how to get data anywhere in CSV.

- Read the CSV file with pandas and test it line by line. Whether the test results are successful or not, they will be written to the log file in the output folder.

## SCREENSHOT

1. csv file
![OxqWY48DltuwFe5](https://i.loli.net/2021/12/01/OxqWY48DltuwFe5.png)

2. Log

![WTufUEhGV8AYqi4](https://i.loli.net/2021/12/01/WTufUEhGV8AYqi4.png)
![2youjavV49ztfXE](https://i.loli.net/2021/12/01/2youjavV49ztfXE.png)

3. pylint main.py
![JsMlP32ACHoR6eF](https://i.loli.net/2021/12/01/JsMlP32ACHoR6eF.png)