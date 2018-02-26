#!/usr/bin/env python

import pprint
import argparse
from os.path import join, realpath, sep
from os import rename
from glob import glob


def parse_args():
    parser = argparse.ArgumentParser()
    parser.add_argument('series', help='TV Series name. e.g. Futuramar')
    parser.add_argument('directory', help='Directory containing titles to fix.', default='.')
    parser.add_argument('start', help='Episode number to start on. e.g. 49')
    parser.add_argument('-s','--season', help='Season these extras are attached to', default='0')

    return parser.parse_args()


def get_files_to_process(args):
    glob_path = join(args.directory, "title*.mkv")
    return glob(glob_path)


def main():
    args = parse_args()
    pprint.pprint(args)

    files = get_files_to_process(args)
    pprint.pprint(files)

    season = args.season
    start = int(args.start)

    for index, file in enumerate(files):        
        episode_number = str(start + index)
        print("episode_number: {}".format(episode_number))
        print("season: {}".format(season))
        new_filename = "{}-s{}-e{}.mkv".format(args.series, season.zfill(2), episode_number.zfill(2))
        print("new filename: {}".format(new_filename))
        # Path needs to be expanded.
        new_path = join(args.directory + sep + new_filename)
        print("new pathname: {}".format(new_path))
        rename(file, new_path)



main()