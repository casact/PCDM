# PCDM
[![PyPI version](https://badge.fury.io/py/pcdm.svg)](https://badge.fury.io/py/pcdm)

Property Casualty Data Model

SQLAlchemy implementation of [OMG Property Casualty Data Model](https://www.omg.org/spec/PC/About-PC/)

![](docs/pcdmcdm.png)

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

from party import Base

engine = sa.create_engine(
            'sqlite:///pcdm.db',
            echo=True
        )
session = sessionmaker(bind=engine)
Base.metadata.create_all(engine)
```