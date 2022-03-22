import click
import os
import json
import sys

from python_installer.build_module import build as m_build
from python_installer.install_module import install as m_install
from python_installer.json_module import create_json as m_json



@click.group()
def cli():
    pass

@cli.command(name='install', help='Install added modules')
def install():
    m_install()

@cli.command(name='build', help='Create a pacakage installer')
def build():
    m_json()
    m_build()