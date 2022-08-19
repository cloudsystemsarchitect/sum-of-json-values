# Get the sum of JSON values
This script finds the total of `seqlen` values in all files matching `*.data.json` pattern found in a given folder. 

* It handles the invalid `seqlen` by recording it in a log file using the `logging` module. 
* It supports the search in the subdirectory using the `glob` module to find all the filenames matching a `*.data.json` in the directory and sub-directory. 
* It uses the `cysimdjson` module to speed up reading the `seqlen` value from the JSON file

# Installation in Linux 
```
git clone https://github.com/patrickgwl1/seqlen.git

cd seqlen

python3 -m venv env

source env/bin/activate

pip3 install -r requirements.txt

```

# How to run

```
python3 seqlen.py --input_dir='<input directory>'

```

# How to run the unit tests

```

cd seqlen

pip install pytest

pip install coverage

coverage run -m pytest

coverage report -m

```


