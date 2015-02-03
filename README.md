# YNAB Downloader

A tool that uses selenium to traverse your bank website and download exports of account activity to import into YNAB budgeting tool.

# Downloading Chase Activity

**NOTE:** Currently this is operational on Mac OSX only because the selenium driver in this repo is for OSX. There are plans to expand this to allow linux distros such as Ubuntu as well.

* First open your chrome browser and login to your bank. The login is automated on the script, but we do this to ensure that we have the cookie required from entering in the text message access code.

* Have your account username/password and checking/cc/savings account ids ready

* Now run the ynab downloader and follow the instructions on the command line:

For a credit card:
```bash
$ ynab-downloader chase --account_type cc
```
For a checking account:
```bash
$ ynab-downloader chase --account_type checking
```

# Caveats

Currently only chase credit card and checking/savings accounts are supported. Other banks will have to be implemented by contributions.

# Contribute

Fork the project, clone it,  and `pip install -e ynab_downloader`
