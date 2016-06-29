# sitedown
A diagnostic program that should tell you why your web site has suffered a catastrophic outage

Instructions for use:

```
python sitedown.py -f CONFIGURATION_FILE -c
```
Assuming everything is working normally, create or update *CONFIGURATION_FILE*.  Some of the things in
the configuration file, such as the SNMP community name, have to be added manually.

```
python sitedown.py -f configuration_file -t
```

Test the configuration file *CONFIGURATION_FILE* is correct.

```
python sitedown.py -f CONFIGURATION_FILE
```

Actually run the program and diagnose why the site has failed.

Note that *CONFIGURATION_FILE* is optional.  If ommitted, the file ~/sitedown.json will be used.




