# gscholar-search

### Environment Setup:
```
python 3.9
scholarly 1.7.11
```

### Usage
Search by author name/author ID/publication title
```
python main.py [--name="Author Name"]|
               [--id="Author gscholar ID"]|
               [--title="Publication Title"] [--bib="Generate bibtex"] [--output="Output Path"]
```
Output file in ```.json``` format

### Acknowledging ```scholarly```
```
@software{cholewiak2021scholarly,
  author  = {Cholewiak, Steven A. and Ipeirotis, Panos and Silva, Victor and Kannawadi, Arun},
  title   = {{SCHOLARLY: Simple access to Google Scholar authors and citation using Python}},
  year    = {2021},
  doi     = {10.5281/zenodo.5764801},
  license = {Unlicense},
  url = {https://github.com/scholarly-python-package/scholarly},
  version = {1.5.1}
}
```
