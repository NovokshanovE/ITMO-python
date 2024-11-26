# Домашнее задание 1

Код который попал в пакет находится в директории `src`


Для установки пакета пропишите:

```
pip install -r requirements.txt 
```
## Задание 1

Были написаны 2 скрипта Python: `latex_generation.py`, `latex_example.py`

Для формирования файла latex необходимо запустить `latex_example.py` из директории `src`.

```
python3 latex_example.py
```

Выходной файл `example_table.tex` лежит в директории `artifacts`.




## Задание 2

```bash
(venv) novokshanov-e@i109893575:~/ITMO/ITMO-python/hw_2/src$ python setup.py sdist bdist_wheel
running sdist
running egg_info
writing novokshanovLatexGen.egg-info/PKG-INFO
writing dependency_links to novokshanovLatexGen.egg-info/dependency_links.txt
writing top-level names to novokshanovLatexGen.egg-info/top_level.txt
reading manifest file 'novokshanovLatexGen.egg-info/SOURCES.txt'
writing manifest file 'novokshanovLatexGen.egg-info/SOURCES.txt'
warning: sdist: standard file not found: should have one of README, README.rst, README.txt, README.md

running check
warning: check: missing required meta-data: url

creating novokshanovLatexGen-0.4.0
creating novokshanovLatexGen-0.4.0/latex_gen
creating novokshanovLatexGen-0.4.0/novokshanovLatexGen.egg-info
copying files to novokshanovLatexGen-0.4.0...
copying setup.py -> novokshanovLatexGen-0.4.0
copying latex_gen/__init__.py -> novokshanovLatexGen-0.4.0/latex_gen
copying latex_gen/example_latex.py -> novokshanovLatexGen-0.4.0/latex_gen
copying latex_gen/latex_gen.py -> novokshanovLatexGen-0.4.0/latex_gen
copying novokshanovLatexGen.egg-info/PKG-INFO -> novokshanovLatexGen-0.4.0/novokshanovLatexGen.egg-info
copying novokshanovLatexGen.egg-info/SOURCES.txt -> novokshanovLatexGen-0.4.0/novokshanovLatexGen.egg-info
copying novokshanovLatexGen.egg-info/dependency_links.txt -> novokshanovLatexGen-0.4.0/novokshanovLatexGen.egg-info
copying novokshanovLatexGen.egg-info/top_level.txt -> novokshanovLatexGen-0.4.0/novokshanovLatexGen.egg-info
Writing novokshanovLatexGen-0.4.0/setup.cfg
Creating tar archive
removing 'novokshanovLatexGen-0.4.0' (and everything under it)
running bdist_wheel
running build
running build_py
copying latex_gen/latex_gen.py -> build/lib/latex_gen
/home/novokshanov-e/ITMO/ITMO-python/hw_2/src/venv/lib/python3.10/site-packages/setuptools/command/install.py:34: SetuptoolsDeprecationWarning: setup.py install is deprecated. Use build and pip and other standards-based tools.
  warnings.warn(
installing to build/bdist.linux-x86_64/wheel
running install
running install_lib
creating build/bdist.linux-x86_64/wheel
creating build/bdist.linux-x86_64/wheel/latex_gen
copying build/lib/latex_gen/latex_gen.py -> build/bdist.linux-x86_64/wheel/latex_gen
copying build/lib/latex_gen/__init__.py -> build/bdist.linux-x86_64/wheel/latex_gen
copying build/lib/latex_gen/example_latex.py -> build/bdist.linux-x86_64/wheel/latex_gen
running install_egg_info
Copying novokshanovLatexGen.egg-info to build/bdist.linux-x86_64/wheel/novokshanovLatexGen-0.4.0.egg-info
running install_scripts
creating build/bdist.linux-x86_64/wheel/novokshanovLatexGen-0.4.0.dist-info/WHEEL
creating 'dist/novokshanovLatexGen-0.4.0-py3-none-any.whl' and adding 'build/bdist.linux-x86_64/wheel' to it
adding 'latex_gen/__init__.py'
adding 'latex_gen/example_latex.py'
adding 'latex_gen/latex_gen.py'
adding 'novokshanovLatexGen-0.4.0.dist-info/METADATA'
adding 'novokshanovLatexGen-0.4.0.dist-info/WHEEL'
adding 'novokshanovLatexGen-0.4.0.dist-info/top_level.txt'
adding 'novokshanovLatexGen-0.4.0.dist-info/RECORD'
removing build/bdist.linux-x86_64/wheel
(venv) novokshanov-e@i109893575:~/ITMO/ITMO-python/hw_2/src$ twine upload dist/*
Uploading distributions to https://upload.pypi.org/legacy/
Uploading novokshanovLatexGen-0.4.0-py3-none-any.whl
100% ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 5.5/5.5 kB • 00:00 • ?
Uploading novokshanovLatexGen-0.4.0.tar.gz
100% ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 4.8/4.8 kB • 00:00 • ?

View at:
https://pypi.org/project/novokshanovLatexGen/0.4.0/
(venv) novokshanov-e@i109893575:~/ITMO/ITMO-python/hw_2/src$ 
(venv) novokshanov-e@i109893575:~/ITMO/ITMO-python/hw_2$ pip install novokshanovLatexGen
Collecting novokshanovLatexGen
  Downloading novokshanovLatexGen-0.4.0-py3-none-any.whl (2.8 kB)
Installing collected packages: novokshanovLatexGen
Successfully installed novokshanovLatexGen-0.4.0
(venv) novokshanov-e@i109893575:~/ITMO/ITMO-python/hw_2$ 
```

Как видим, пакет успешно опубдикован и успешно установлен в локальном окружении.

https://pypi.org/project/novokshanovLatexGen/0.2.0/

