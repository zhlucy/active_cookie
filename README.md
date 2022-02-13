# Most Active Cookie

The CLI program takes in a csv file and output the most active cookie on a given date.

## Installing
Follow the commands below to install the program.
```
> git clone https://github.com/zhlucy/active_cookie
> cd active_cookie
```

## Configurating
Before running the program, write the csv file in the following format and move it into src.
```
> vim src/cookie_log.csv
---------csv file---------
cookie,timestamp
AtY0laUfhglK3lC7,2018-12-09T14:19:00+00:00
SAZuXPGUrfbcn5UA,2018-12-09T10:13:00+00:00
```

## Executing program
After completed the steps above, run the program with the following commands.
If the current directory is not active_cookie/src,
```
> cd src
```
And then execute the program.
```
> ./most_active_cookie [csv file] -d [date]
```
See an example below.
```
> ./most_active_cookie cookie_log.csv -d 2018-12-09
```

## Usage Instruction
If there is no active cookie on the given date, the program will print "No active cookie."
If more than one cookie are equally and most active, the program will print all cookies that meet the criteria. 

## Authors

Lucy Lu

## Testing
To run the unit tests for this program, use the commands below.
```
> cd active_cookie
> python3 -m unittest
```
