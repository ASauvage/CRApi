QAutoframework
==============

This project aim to provide a toolbox solution to develop API tests.

## Features

- Comprehensive API testing framework
- Easy-to-use test automation tools
- Built-in assertions and validations
- Detailed reporting and logging

## Installation

```bash
pip install --extra-index-url="http://pypi.mappy.priv/simple" --trusted-host=pypi.mappy.priv qautoframework
```

## Quick Start

```python
from qautoframework.data import SSGServices
from qautoframework.models import TestCase

testcases: list[TestCase] = []
pois = (
    {"name": "Aéroport Cdg - Terminal 2 (tgv)", "alias": ["cdg tgv", "cdg gare"]},
    {"name": "Charles De Gaulle Etoile", "alias": ["cge", "etoile"]}
)

for poi in pois:
    for alias in poi["alias"]:
        testcases.append(TestCase(
            title="Checking POI TC by aliases",
            tags=["suggest", "alias_poi_tc"],
            description="Find and return POI TC by using POI TC aliases",
            params={
                "q": alias,
                "strict_bbox": "48.124656,1.430992,49.239716,3.546065",
                "filter": "addresses,pois"
            },
            process={
                "pois.0.name": [f"EQUAL::{poi['name']}"]
            }
        ))

SSGServices.SEARCH.delete_from_tags('suggest', 'alias_poi_tc')
SSGServices.SEARCH.generate(testcases)
SSGServices.SEARCH.run_from_tags('suggest', 'alias_poi_tc', env="snapshot", limit=1000)
```

## Documentation

For detailed documentation, visit our [wiki](../../wiki) or check the [examples](./examples) directory.

