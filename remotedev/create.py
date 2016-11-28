# Creates a Droplet on Digital Ocean for remote Zulip development.
# Particularly useful for sprints/hackathons, interns, and other
# situation where one wants to quickly onboard new contributors.
#
# This script takes one argument: the name of the GitHub user for whom you want
# to create a Zulip developer environment. Requires Python 3.
#
# Requires python-digitalocean library:
# https://github.com/koalalorenzo/python-digitalocean
#
# Also requires Digital Ocean team membership for Zulip and api token:
# https://cloud.digitalocean.com/settings/api/tokens
#
# Copy conf.ini-template to conf.ini and populate with your api token.
#
# usage: python3 create.py <username>

import sys
import configparser
import urllib.request
import json
import digitalocean
import time
import argparse
import os

# initiation argument parser
parser = argparse.ArgumentParser(description='Create a Zulip devopment VM Digital Ocean droplet.')
parser.add_argument("username", help="Github username for whom you want to create a Zulip dev droplet")

def get_config():
    config = configparser.ConfigParser()
    config.read(os.path.join(os.path.dirname(os.path.abspath(__file__)), 'conf.ini'))
    return config

def user_exists(username):
    print("Checking to see if GitHub user {0} exists...".format(username))
    user_api_url = "https://api.github.com/users/{0}".format(username)
    try:
        response = urllib.request.urlopen(user_api_url)
        userdata = json.loads(response.read().decode())
        print("...user exists!")
        return True
    except urllib.error.HTTPError as err:
        print(err)
        print("Does the github user {0} exist?".format(username))
        sys.exit(1)

def get_keys(username):
    print("Checking to see that GitHub user has available public keys...")
    apiurl_keys = "https://api.github.com/users/{0}/keys".format(username)
    try:
        response = urllib.request.urlopen(apiurl_keys)
        userkeys = json.loads(response.read().decode())
        print("...public keys found!")
        return userkeys
    except urllib.error.HTTPError as err:
        print(err)
        print("Has user {0} added ssh keys to their github account?".format(username))
        sys.exit(1)

def fork_exists(username):
    print("Checking to see GitHub user has forked zulip/zulip...")
    apiurl_fork = "https://api.github.com/repos/{0}/zulip".format(username)
    try:
        response = urllib.request.urlopen(apiurl_fork)
        userfork = json.loads(response.read().decode())
        print("...fork found!")
        return True
    except urllib.error.HTTPError as err:
        print(err)
        print("Has user {0} forked zulip/zulip?".format(username))
        sys.exit(1)

def exit_if_droplet_exists(my_token, username):
    print("Checking to see if droplet for {0} already exists...".format(username))
    manager = digitalocean.Manager(token=my_token)
    my_droplets = manager.get_all_droplets()
    for droplet in my_droplets:
        if droplet.name == "{0}.zulipdev.org".format(username):
            print("Droplet for user {0} already exists.".format(username))
            print("Delete droplet AND dns entry via Digital Ocean control panel if you need to re-create.")
            sys.exit(1)
    print("...No droplet found...proceeding.")

def set_user_data(username, userkeys):
    print("Setting cloud-config data, populated with GitHub user's public keys...")
    ssh_authorized_keys = ""

    # spaces here are important here - these need to be properly indented under
    # ssh_authorized_keys:
    for key in userkeys:
        ssh_authorized_keys += "\n          - {0}".format(key['key'])

    #print(ssh_authorized_keys)
    cloudconf = """
    #cloud-config
    users:
      - name: zulipdev
        ssh_authorized_keys:{1}
    runcmd:
      - su -c 'cd /home/zulipdev/zulip && git remote add origin https://github.com/{0}/zulip.git && git fetch origin' zulipdev
    power_state:
     mode: reboot
     condition: True
    """.format(username, ssh_authorized_keys)

    print("...returning cloud-config data.")
    return cloudconf

def create_droplet(my_token, template_id, username, user_data):
    droplet = digitalocean.Droplet(token=my_token,
                                name='{0}.zulipdev.org'.format(username),
                                region='nyc3',
                                image=template_id,
                                size_slug='2gb',
                                user_data=user_data,
                                tags=username,
                                backups=False)

    print("Initiating droplet creation...")
    droplet.create()

    incomplete = True
    while incomplete:
        actions = droplet.get_actions()
        for action in actions:
            action.load()
            print("...[{0}]: {1}".format(action.type, action.status))
            if action.type == 'create' and action.status == 'completed':
                incomplete = False
                break
        if incomplete:
            time.sleep(15)
    print("...droplet created!")
    droplet.load()
    print("...ip address for new droplet is: {0}.".format(droplet.ip_address))
    return droplet.ip_address

def create_dns_record(my_token, username, ip_address):
    print("Creating A record for {0}.zulipdev.org that points to {1}.".format(username,ip_address))
    domain = digitalocean.Domain(token=my_token, name='zulipdev.org')
    domain.load()
    domain.create_new_domain_record(type='A', name=username, data=ip_address)

if __name__ == '__main__':
    # define id of image to create new droplets from
    template_id = "20997685"

    # get command line arguments
    args = parser.parse_args()
    print("Creating Zulip developer environemnt for GitHub user {0}...".format(args.username))

    # get config details
    config = get_config()

    # see if droplet already exists for this user
    user_exists(username=args.username)

    # grab user's public keys
    public_keys = get_keys(username=args.username)

    # now make sure the user has forked zulip/zulip
    fork_exists(username=args.username)

    api_token = config['digitalocean']['api_token']
    # does the droplet already exist?
    exit_if_droplet_exists(my_token=api_token, username=args.username)

    # set user_data
    user_data = set_user_data(username=args.username, userkeys=public_keys)

    # create droplet
    ip_address = create_droplet(my_token=api_token,
                                template_id=template_id,
                                username=args.username,
                                user_data=user_data)

    # create dns entry
    create_dns_record(my_token=api_token, username=args.username, ip_address=ip_address)

    print("COMPLETE! GitHub user {0} can connect to droplet with:".format(args.username))
    print("   ssh zulipdev@{0}.zulipdev.org".format(args.username))
    sys.exit(1)
