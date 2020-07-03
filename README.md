# PCDM
[![PyPI version](https://badge.fury.io/py/pcdm.svg)](https://badge.fury.io/py/pcdm)

Property Casualty Data Model

SQLAlchemy implementation of [OMG Property Casualty Data Model](https://www.omg.org/spec/PC/About-PC/)

![](docs/pcdmcdm.png)

## Distribution

According to the [Object Management Group](https://www.omg.org/gettingstarted/overview.htm#Free):

>Anyone can download specifications from the OMG website for free, write software implementations that conform to the specifications, and use them, give them away, or sell them. Neither OMG membership nor license is required for this.

## Installation

Run pip install:

```
pip install pcdm
```

## Deployment

The file deploy_sqlite contains a script that can be used to deploy a SQLite database:

```
import sqlalchemy as sa

from sqlalchemy.orm import sessionmaker

from base import Base
import party, account, policy, claim, assessment, agreementrole, claimrole, staffing, partyst, insurable, money

engine = sa.create_engine(
            'sqlite:///pcdm.db',
            echo=True
        )
session = sessionmaker(bind=engine)
Base.metadata.create_all(engine)
```
