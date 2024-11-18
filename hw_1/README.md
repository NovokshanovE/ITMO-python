# Домашнее задание 1

## Libs

В текущей домашней работе использовалась только стандартная библиотека `sys`

## Структура папок
`artifacts` - папка со всеми артефактами

`artifacts/task1` - папка со всеми ходными файлами ля задания 1

`artifacts/task2` - папка со всеми ходными файлами ля задания 2

`artifacts/task1.txt` - файл с запуском утилиты по заданию 1

`artifacts/task2.txt` - файл с запуском утилиты по заданию 2

## Задача 1

Те же тесты хранятся в файле `artifacts/task1.txt`

### Пример с указанием входного файла

#### Сам файл `task1_input.txt`


```bash
~/ITMO/ITMO-python/hw-1$ cat artifacts/task1_input.txt 
Hello
World
This
Is
A
Tr
frfr

Worlddwd
d
dd

hfjr
```
#### Запуск утилиты

```bash
~/ITMO/ITMO-python/hw-1$ python3 nl.py artifacts/task1_input.txt 
1 Hello
2 World
3 This
4 Is
5 A
6 Tr
7 frfr
8 
9 Worlddwd
10 d
11 dd
12 
13 hfjr
```

### Пример c передачей текста из stdin

```bash
~/ITMO/ITMO-python/hw-1$ echo -e "Hello\nWorld\nThis\nIs\nerwtyte\nywueiw\nertete\tuye\nuheu" | python3 nl.py 
1 Hello
2 World
3 This
4 Is
5 erwtyte
6 ywueiw
7 ertete        uye
8 uheu
```


## Задача 2

### Содержимое входных файлов `artifacts/task2/file1.txt` и `artifacts/task2/file2.txt`

#### `file1.txt`

```bash
~/ITMO/ITMO-python/hw-1$ cat artifacts/task2/file1.txt 
line 1  of file1
line 2  of file1
line 3  of file1
line 4  of file1
line 5  of file1
line 6  of file1
line 7  of file1
line 8  of file1
line 9  of file1
line 10 of file1
line 11 of file1
line 12 of file1
line 13 of file1
line 14 of file1
```

#### `file2.txt`

```bash
~/ITMO/ITMO-python/hw-1$ cat artifacts/task2/file1.txt 
line 1  of file1
line 2  of file1
line 3  of file1
line 4  of file1
line 5  of file1
line 6  of file1
line 7  of file1
line 8  of file1
line 9  of file1
line 10 of file1
line 11 of file1
line 12 of file1
line 13 of file1
line 14 of file1
```

### Тестирование утилиты `tail` на одном файле

#### На файле `artifacts/task2/file1.txt`

```bash
~/ITMO/ITMO-python/hw-1$ python3 tail.py artifacts/task2/file1.txt 
line 5  of file1
line 6  of file1
line 7  of file1
line 8  of file1
line 9  of file1
line 10 of file1
line 11 of file1
line 12 of file1
line 13 of file1
line 14 of file1
```


### На файле `artifacts/task2/file2.txt`

```bash
~/ITMO/ITMO-python/hw-1$ python3 tail.py artifacts/task2/file2.txt 
line 7  of file2
line 8  of file2
line 9  of file2
line 10 of file2
line 11 of file2
line 12 of file2
line 13 of file2
line 14 of file2
line 15 of file2
line 16 of file2
```

### Тестирование утилиты `tail` на двух файлах

```bash
~/ITMO/ITMO-python/hw-1$ python3 tail.py artifacts/task2/file2.txt artifacts/task2/file1.txt 
==> artifacts/task2/file2.txt <==
line 7  of file2
line 8  of file2
line 9  of file2
line 10 of file2
line 11 of file2
line 12 of file2
line 13 of file2
line 14 of file2
line 15 of file2
line 16 of file2
==> artifacts/task2/file1.txt <==
line 5  of file1
line 6  of file1
line 7  of file1
line 8  of file1
line 9  of file1
line 10 of file1
line 11 of file1
line 12 of file1
line 13 of file1
line 14 of file1
```

### Тестирование утилиты `tail` на трех файлах

```bash
~/ITMO/ITMO-python/hw-1$ python3 tail.py artifacts/task2/file2.txt artifacts/task2/file1.txt artifacts/task1/task1_input.txt 
==> artifacts/task2/file2.txt <==
line 7  of file2
line 8  of file2
line 9  of file2
line 10 of file2
line 11 of file2
line 12 of file2
line 13 of file2
line 14 of file2
line 15 of file2
line 16 of file2
==> artifacts/task2/file1.txt <==
line 5  of file1
line 6  of file1
line 7  of file1
line 8  of file1
line 9  of file1
line 10 of file1
line 11 of file1
line 12 of file1
line 13 of file1
line 14 of file1
==> artifacts/task1/task1_input.txt <==
Is
A
Tr
frfr

Worlddwd
d
dd

hfjr
```

### Тестирование утилиты `tail` при чтении из stdin

```bash
~/ITMO/ITMO-python/hw-1$ cat artifacts/task2/file1.txt | python3 tail.py 
line 1  of file1
line 2  of file1
line 3  of file1
line 4  of file1
line 5  of file1
line 6  of file1
line 7  of file1
line 8  of file1
line 9  of file1
line 10 of file1
line 11 of file1
line 12 of file1
line 13 of file1
line 14 of file1
```


## Задача 3

Тестирование провродилось на файлах из директории `./artifacts/task2/`

### Тестирование stdin

```bash
~/ITMO/ITMO-python/hw_1$ python3 wc.py 
de
ded
gt
q

werp ok j r3
6       8       26
```

### Тестирование для одного файла `file1.txt`

```bash
~/ITMO/ITMO-python/hw_1$ python3 wc.py artifacts/task2/file1.txt 
13 56 237 artifacts/task2/file1.txt
```

### Тестирование для нескольних файлов из директории `./artifacts/task2/`

```
~/ITMO/ITMO-python/hw_1$ python3 wc.py artifacts/task2/*.txt 
13 56 237 artifacts/task2/file1.txt
15 64 271 artifacts/task2/file2.txt
28 120 508 total
```





