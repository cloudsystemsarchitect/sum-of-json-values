# seqlen
This utility finds the total of `seqlen` values in all files matching `*.data.json` pattern found in a given folder. 

# Installation 
```
git clone https://github.com/patrickgwl1/seqlen.git

```

# Running the script

```
cd seqlen

python3

>>> import seqlen

>>> seqlen.get_total_seqlen_from_dir(json_dir='<Replace with directory with all the `*.data.json` files>')

```

# Running the unit test

```
pip install pytest

pip install coverage

coverage run -m pytest -v

coverage report -m

```
