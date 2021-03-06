import pexpect
import os
import json
import time


def generate_ssh_keys_pexpect(user_first_name, user_last_name, path):

    """
    Create ssh Keys for the user

    Args:
        user_first_name: The first name of the user which will be included in the URN
        user_last_name: The last name of the user which will be included in the URN
        ch_name: the name of the corresponding clearing house

    """
    print path
    try:
        child = pexpect.spawn('ssh-keygen -t rsa')

        child.expect('Enter file in which to save the key (.*):')
        child.sendline(path + user_first_name[0] + user_last_name)

        child.expect('Enter passphrase (.*):')
        child.sendline('')

        child.expect('Enter same passphrase again:')
        child.sendline('')

    except Exception, e:
        print e #For now


def read_file(path):
    """
    Read a file content

    Args:
        path: The path of the file to read

    Returns:
        The contents of the file
    """
    with file(path) as f:
        s = f.read()
        return s


def read_json_file(path):
    """
    Read content of a JSON file

    Args:
        path: The path of the file to read

    Returns:
        The contents of the JSON file
    """
    with open(path) as json_file:
        json_data = json.load(json_file)
        return json_data


def get_ssh_keys( user_first_name, user_last_name, path):
    """
    Get ssh keys for a user

    Args:
        user_first_name: The first name of the user which will be included in the URN
        user_last_name: The last name of the user which will be included in the URN

    Returns:
        public ssh key

    """
    generate_ssh_keys_pexpect(user_first_name, user_last_name, path)

    private_key = read_file(str(path)+ user_first_name[0] + user_last_name)
    public_key =  read_file(str(path)+ user_first_name[0] + user_last_name +'.pub')
    return (public_key, private_key)
