# Website Blocker built using Python

## Objective

### Built a Python script that will run in the background during a given timeframe (for example, the working day) and block access to specific websites

## Modules

### datetime, time

## Usage

### This script has been written to be used with a scheduling service (cron, windows scheduler, etc).
### If using cron on MacOS or Linux, add the following to run this script in the background on boot:
```
@reboot python3 path/to/script
```

## Future improvements

### - Add GUI to allow the user to specify time window and websites to block