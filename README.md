# PCDM
[![PyPI version](https://badge.fury.io/py/pcdm.svg)](https://badge.fury.io/py/pcdm)

Property Casualty Data Model

SQLAlchemy implementation of [OMG Property Casualty Data Model](https://www.omg.org/spec/PC/About-PC/)

![](docs/pcdmcdm.png)

## Distribution

According to the [Object Management Group](https://www.omg.org/gettingstarted/overview.htm#Free):

>Anyone can download specifications from the OMG website for free, write software implementations that conform to the specifications, and use them, give them away, or sell them. Neither OMG membership nor license is required for this.


## Installation and Deployment

This repository requires sqlalchemy, so install it if you don't have it:

```
pip3 install sqlalchemy
```

or
```
pip3 install -r requirements.txt
```

The file deploy_sqlite contains a script that can be used to deploy a SQLite database:

```
git clone https://github.com/genedan/PCDM
cd PCDM
python3 deploy_sqlite.py
```

## PyPI

This packages is also avaiable on PyPI:

```
pip3 install pcdm
```