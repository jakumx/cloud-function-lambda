# cloud-function-lambda

## requirements

* `mysql`

## env variables

* MYSQL_HOST
* MYSQL_USER
* MYSQL_PASSWORD

## Test

```sh
 $ python -m unittest tests/*_tests.py
 ```

 ## populate db

 ```sh
  $ mysql -u <user> -h <host> -p -s < seed.sql
 ```
