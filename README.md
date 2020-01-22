# Rets Reader

Designed to read any RETS database with a query as a parameter.

## Getting Started

These instructions will get you a copy of the project up and running on your local machine for development and testing purposes. See deployment for notes on how to deploy the project on a live system.

### Prerequisites

What things you need to install the software and how to install them

```
python3
pip
virtualenv
```

### Installing

A step by step series of examples that tell you how to get a development env running

set up virtual environment

```bash
$ virtualenv ./env 
```

enter virtual environment and install requirements

```bash
$ source ./env/bin/activate
$ pip install -r requirements.txt
```

Create a `settings.cfg` file to specify the url and credentials to the rets database you would like to access

See [settings.cfg.example](settings.cfg.example)


## Usage

This tool is designed to be a command line application, you can use it to query whichever rets database you have specified by invoking it as such

In this example, we run in the residential table, looking for 100 entries where there are 3 bedrooms
```bash
$ python run.py RE_1 "(Beds=3)" 100
```

without the limit argument, run.py will default to 1 for safety
```bash
$ python run.py RE_1 "(Beds=3)"
```

Help
```bash
$ python run.py help
python run.py PROPERTY_TYPE DMQP_QUERY [LIMIT]
```


## Authors

* **Johnathen Chilcher** - *Initial work* - [jchilcher](https://github.com/jchilcher)

See also the list of [contributors](https://github.com/jchilcher/RETS_Reader/contributors) who participated in this project.

## License

This project is licensed under the MIT License - see the [LICENSE.md](LICENSE.md) file for details
