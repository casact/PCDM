# PCDM
[![PyPI version](https://badge.fury.io/py/pcdm.svg)](https://badge.fury.io/py/pcdm)

Property Casualty Data Model

PCDM is a [SQLAlchemy](https://www.sqlalchemy.org/) implementation of [Object Management Group's Property Casualty Data Model](https://www.omg.org/spec/PC/About-PC/). The Property Casualty Data Model is a relational database schema that closely resembles the backend of an insurance company. This package allows you to deploy a SQLite database within seconds for testing, and can be tweaked to support Postgres and other relational database systems.

PCDM contains 256 tables from 13 subject area models (SAMs):

1. Party - all persons, organizations, and groups involved in the insurance agreement
2. Account and Agreement - customer, insurer, and vendor agreements
3. Policy - policy information
4. Claim - claim information
5. Assessment - information pertaining to assesment (credit scoring, appraisals)
6. Agreement Role - roles involved in agreements (providers, producers, suppliers)
7. Claim Role - roles involved in claims (claimaints, adjusters)
8. Staffing Role - roles involved in staffing (employees and contractors)
9. Party Subtype - groupings and subgroupings of parties
10. Insurable Object - things that can be insured (vehicles, structures)
11. Money - transaction information
12. Event - event information
13. Product - product information (line of business, limits, coverage)

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

This package is also available on PyPI:

```
pip3 install pcdm
```
