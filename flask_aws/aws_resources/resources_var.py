import boto3
import botocore
import argparse
import configparser
import os
import re
import logging


def init():
    config_path = os.environ.get('HOME') + "/.aws/credentials"
    parser = configparser.ConfigParser()
    parser.read(config_path)
    if parser.sections():
        return parser.sections()
    return []