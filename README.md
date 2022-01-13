# tuyabacklight
## A Python application that creates ambient lighting from pixel value on screen

## Dependencies
**Mac-OS:**
```pipenv```
**Linux/Unix-Based OS:**
```pipenv```

**Windows:**
Currently, no plans exist for developing this software for windows systems. Sorry not sorry :P
## Installation instructions

clone the repository: ```git clone https://github.com/devbrones/tuyabacklight```\
modify the config file to your liking and change config file name: ```cd tuyabacklight/src && mv config_blank.yml config.yml && vim config.yml```\
run the application: ```pipenv run python main.py```

## Configuration options
default config:\
```yml
# logger path (default is .)
log_path: ./log.log

device_1:
  # device config defaults
  ip: '' # internal ip address
  dev_id: '' # device uuid
  ver: '' # protocol version (3.1 or 3.3)
  loc_key: '' # local encryption key
  screen_rel: 'DP-0' # what screen this light represents
  name: 'LEFT_REL_LIGHT'

device_2:
  # device config defaults
  ip: '' # internal ip address
  dev_id: '' # device uuid
  ver: '' # protocol version (3.1 or 3.3)
  loc_key: '' # local encryption key
  screen_rel: 'DP-1' # what screen this light represents
  name: 'CNTR_REL_LIGHT'

device_2:
  # device config defaults
  ip: '' # internal ip address
  dev_id: '' # device uuid
  ver: '' # protocol version (3.1 or 3.3)
  loc_key: '' # local encryption key
  screen_rel: 'DP-2' # what screen this light represents
  name: 'RGHT_REL_LIGHT'

debug: false
verbose: false
log: true
cloud: false
default_rgb_val: '123,123,123'
```
