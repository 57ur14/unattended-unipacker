# Unattended unipacker #

This is a fork of [unipacker](https://github.com/unipacker/unipacker) made to allow unattended unpacking (for automated unpacking without the need for user input).

## Installing ##
* ``git clone https://github.com/ntnu-rgb/unattended-unipacker.git``
* ``cd unattended-unipacker``
* ``python3 setup.py install``

## Usage (from shell) ##
``unipacker -d <destination directory> <path to file to analyse>``

## Uninstalling ##
``pip3 uninstall unattended-unipacker``

## Changes from the original ##
The functions _get_tail_jump_ and _get_entrypoint_ in ``unpackers.py``no longer ask for input from the user.
