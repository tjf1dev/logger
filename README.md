# tjf1's logger setup

simple python logger setup i use in most of my projects
<img width="760" height="181" alt="showcase" src="https://github.com/user-attachments/assets/8d8b615b-061e-4bda-9408-1c3a58d71205" />

## features

- easy to install and use
- clean, simple logs
- new "OK" level to indicate successful actions
- file logging

## install

make sure the cwd is the root of your project

### as submodule (recommended)

```bash
git submodule add https://github.com/tjf1dev/logger logger
git commit -m "add logger submodule"
```

#### updating

```bash
git submodule update --remote logger
```

### without submodule

```bash
git clone https://github.com/tjf1dev/logger
```

## usage

```py
import logger
logger.info("hello world!")
# > DD/MM/YYYY HH:MM:SS [ INFO ] hello world! (<module>)
```

## settings

to change the default behavior, open `logger/logger.py`

- `FILE_LOGGING`: is file logging enabled
- `LOG_PATH`: the name of the directory to save logs to
- `FILENAME_DATE_STR`: the name of the log files ([available codes](https://docs.python.org/3/library/datetime.html#strftime-and-strptime-format-codes))
  - <details>
    <summary>available codes</summary>

    | Directive | Meaning                                                                                                                                                                          | Example                                                                      |
    | --------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------- |
    | %a        | Weekday as locale’s abbreviated name.                                                                                                                                            | Sun, Mon, …, Sat (en_US); So, Mo, …, Sa (de_DE)                              |
    | %A        | Weekday as locale’s full name.                                                                                                                                                   | Sunday, Monday, …, Saturday (en_US); Sonntag, Montag, …, Samstag (de_DE)     |
    | %w        | Weekday as a decimal number, where 0 is Sunday and 6 is Saturday.                                                                                                                | 0, 1, …, 6                                                                   |
    | %d        | Day of the month as a zero-padded decimal number.                                                                                                                                | 01, 02, …, 31                                                                |
    | %b        | Month as locale’s abbreviated name.                                                                                                                                              | Jan, Feb, …, Dec (en_US); Jan, Feb, …, Dez (de_DE)                           |
    | %B        | Month as locale’s full name.                                                                                                                                                     | January, February, …, December (en_US); Januar, Februar, …, Dezember (de_DE) |
    | %m        | Month as a zero-padded decimal number.                                                                                                                                           | 01, 02, …, 12                                                                |
    | %y        | Year without century as a zero-padded decimal number.                                                                                                                            | 00, 01, …, 99                                                                |
    | %Y        | Year with century as a decimal number.                                                                                                                                           | 0001, 0002, …, 2013, 2014, …, 9998, 9999                                     |
    | %H        | Hour (24-hour clock) as a zero-padded decimal number.                                                                                                                            | 00, 01, …, 23                                                                |
    | %I        | Hour (12-hour clock) as a zero-padded decimal number.                                                                                                                            | 01, 02, …, 12                                                                |
    | %p        | Locale’s equivalent of either AM or PM.                                                                                                                                          | AM, PM (en_US); am, pm (de_DE)                                               |
    | %M        | Minute as a zero-padded decimal number.                                                                                                                                          | 00, 01, …, 59                                                                |
    | %S        | Second as a zero-padded decimal number.                                                                                                                                          | 00, 01, …, 59                                                                |
    | %f        | Microsecond as a decimal number, zero-padded to 6 digits.                                                                                                                        | 000000, 000001, …, 999999                                                    |
    | %z        | UTC offset in the form ±HHMM[SS[.ffffff]] (empty string if the object is naive).                                                                                                 | (empty), +0000, -0400, +1030, +063415, -030712.345216                        |
    | %Z        | Time zone name (empty string if the object is naive).                                                                                                                            | (empty), UTC, GMT                                                            |
    | %j        | Day of the year as a zero-padded decimal number.                                                                                                                                 | 001, 002, …, 366                                                             |
    | %U        | Week number of the year (Sunday as the first day of the week) as a zero-padded decimal number. All days in a new year preceding the first Sunday are considered to be in week 0. | 00, 01, …, 53                                                                |
    | %W        | Week number of the year (Monday as the first day of the week) as a zero-padded decimal number. All days in a new year preceding the first Monday are considered to be in week 0. | 00, 01, …, 53                                                                |
    | %c        | Locale’s appropriate date and time representation.                                                                                                                               | Tue Aug 16 21:30:00 1988 (en_US); Di 16 Aug 21:30:00 1988 (de_DE)            |
    | %x        | Locale’s appropriate date representation.                                                                                                                                        | 08/16/88 (None); 08/16/1988 (en_US); 16.08.1988 (de_DE)                      |
    | %X        | Locale’s appropriate time representation.                                                                                                                                        | 21:30:00 (en_US); 21:30:00 (de_DE)                                           |
    | %%        | A literal '%' character.                                                                                                                                                         | %                                                                            |

    </details>

  - ([from python's docs](https://docs.python.org/3/library/datetime.html#strftime-and-strptime-format-codes))

- `LEVEL`: default logger level

<img width="487" height="252" alt="config setup" src="https://github.com/user-attachments/assets/faa711b0-a6a3-489b-8e82-fab14f63f060" />

## file logging

> [!WARNING]
> file logging is disabled by default! enable it in [settings](#settings)

the logger setup has file logging built in.  
it creates them to a folder names `logs` by default
with a `latest.log` and a log file for every session
