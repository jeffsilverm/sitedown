# sitedown
A diagnostic program that should tell you why your web site has suffered a catastrophic outage

Instructions for use:

```
python sitedown.py -f *configuration_file* -c
```
Assuming everything is working normally, create or update *configuration_file*.  Some of the things in
the configuration file, such as the SNMP community name, have to be added manually.

```
python sitedown.py -f *configuration_file* -t
```

Test the configuration file *configuration_file* is correct.

```
python sitedown.py -f *configuration_file*
```

Actually run the program and diagnose why the site has failed.


