import os as OS
import sys, subprocess as sps, os


# Every browser specific module must define run(), find_path() and name like this

name = 'Firefox'

def run(path, options, start_urls):
    if options['app_mode']:
        for url in start_urls:
            sps.Popen([path, "-no-remote", url] +
                       options['cmdline_args'],
                       stdout=sps.PIPE, stderr=sps.PIPE, stdin=sps.PIPE)
    else:
        return
        args = options['cmdline_args'] + start_urls
        sps.Popen([path, '-new-window'] + args,
                   stdout=sps.PIPE, stderr=sys.stderr, stdin=sps.PIPE)


def find_path():
    if sys.platform in ['win32', 'win64']:
        return _find_firefox_win()

def _find_firefox_win():
    letters = "CDEFG"
    for l in letters:
        path = l + r":\Program Files\Mozilla Firefox\firefox.exe"
        if os.path.exists(path):
            return path