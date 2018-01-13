#!/bin/bash

mysql -u clisson -p -e 'drop database if exists clisson_library;' 
cat clisson_library.sql | mysql -u clisson -p
cat insert.sql | mysql -u clisson -p clisson_library
