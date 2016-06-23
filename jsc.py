import click
import requests
import json
import pprint
from click import pass_context
from io import BytesIO
import ctx
import os
import sys
import getopt
from cmd import Cmd
import argparse
from click import ClickException, UsageError, BadParameter, Abort, MissingParameter     
from utils import make_str, make_default_short_help, echo
from configparser import SafeConfigParser
 
class Interface(Cmd):
     
    @click.command('groups', short_help='Shows groups.')
    @pass_context
     
    def do_groups(self): 
        """Shows groups changes in the current working directory. \n Format: groups"""
         
        headers = {'content-type': 'application/json'}
        url =  "http://10.5.4.87:11880/rest/management/groups/ftp.ivydb.com"
        r = requests.get(url, cookies=ctx.cookies,headers=headers)
        dictionary = r.json()
        for entry in dictionary:
            print(entry['name'])
             
             
    def do_useradd(self, username): 
        """Allows you to insert a new user. \n Format: useradd userName"""
         
        body = {
            "username": str(username),
            "login": "",
            "password": "",
        }
        body["login"] = input("Enter login:")
        body["password"] = input("Enter password")
         
        headers = {'content-type': 'application/json'}
        url =  "http://10.5.4.87:11880/rest/management/accounts/ftp.ivydb.com"
        r = requests.get(url, body, cookies=ctx.cookies,headers=headers)
        print("User successfully added")
     
     
    def do_userdel(self, account): 
        """Allows the deletion of a user. \n Format: userdel accountName"""
         
        headers = {'content-type': 'application/json'}
        url =  "http://10.5.4.87:11880/rest/management/groups/ftp.ivydb.com/" + account
        r = requests.get(url, account, cookies=ctx.cookies,headers=headers)
        print("User successfully deleted")
     
     
    def do_groupadd(self, groupName): 
        """Allows the addition of a group. \n Format: groupadd groupName"""
         
        body = {
            "name": str(groupName)
        }
        headers = {'content-type': 'application/json'}
        url =  "http://10.5.4.87:11880/rest/management/groups/ftp.ivydb.com"
        r = requests.get(url, body, cookies=ctx.cookies,headers=headers)
        print("Group successfully added")
         
         
    def do_cat(self): 
        """Allows you to view all accounts. \n Format: cat"""
         
        headers = {'content-type': 'application/json'}
        url =  "http://10.5.4.87:11880/rest/management/account-infos/ftp.ivydb.com"
        r = requests.get(url, cookies=ctx.cookies,headers=headers)
        dictionary = r.json()
        for key, value in dictionary:
            print(key, value)
            
                  
    def do_getaccount(self, account): 
        """Allows access to account information. \n Format: getaccount accountName"""
         
        headers = {'content-type': 'application/json'}
        url =  "http://10.5.4.87:11880/rest/management/accounts/ftp.ivydb.com/" + account
        r = requests.get(url, account, cookies=ctx.cookies,headers=headers)
        print(r.json())
         
         
    def do_passwd(self, userName):
        """Allows you to change the password of a new user. \n Format: passwd userName"""
         
        headers = {'content-type': 'application/json'}
        url =  "http://10.5.4.87:11880/rest/management/accounts/ftp.ivydb.com/" + userName
        r = requests.get(url, userName, cookies=ctx.cookies,headers=headers)
        body = r.json()
        body["password"] = input("Enter new password:")
         
        headers = {'content-type': 'application/json'}
        url =  "http://10.5.4.87:11880/rest/management/accounts/ftp.ivydb.com"
        r = requests.get(url, body, cookies=ctx.cookies,headers=headers)
        print("User password successfully changed.")
 
 
 
 
CONTEXT_SETTINGS = dict(auto_envvar_prefix='JSC')
class Handle:
     
    @click.command('groups', short_help='Shows groups.')
    @pass_context
    def main(args, ctx):
        argv = args
 
        parser = SafeConfigParser()
        parser.readfp(sys.stdin)
         
        config = dict((section, dict((option, parser.get(section, option))
                                    for option in parser.options(section)))
                    for section in parser.sections())
        p = argparse.ArgumentParser()
        subparsers = p.add_subparsers()
         
        # groups command
        groups_parser = subparsers.add_parser('groups')
        groups_parser.set_defaults(funct = Interface.do_groups)
        for param in argv[1:]:
            groups_parser.add_argument(param)
 
            if args and not ctx.allow_extra_args and not ctx.resilient_parsing:
                ctx.fail('Got unexpected extra argument%s (%s)'
                        % (len(args) != 1 and 's' or '',
                            ' '.join(map(make_str, args))))
         
        # useradd command
        useradd_parser = subparsers.add_parser('useradd')
        useradd_parser.set_defaults(func=Interface.do_useradd)
        for param in argv[1:]:
            useradd_parser.add_argument(param)
 
            if args and not ctx.allow_extra_args and not ctx.resilient_parsing:
                ctx.fail('Got unexpected extra argument%s (%s)'
                        % (len(args) != 1 and 's' or '',
                            ' '.join(map(make_str, args))))
         
        # userdel command
        userdel_parser = subparsers.add_parser('userdel')
        userdel_parser.set_defaults(func=Interface.do_userdel)
        for param in argv[1:]:
            userdel_parser.add_argument(param)
 
            if args and not ctx.allow_extra_args and not ctx.resilient_parsing:
                ctx.fail('Got unexpected extra argument%s (%s)'
                        % (len(args) != 1 and 's' or '',
                            ' '.join(map(make_str, args))))
         
        # groupadd command
        groupadd_parser = subparsers.add_parser('groupadd')
        groupadd_parser.set_defaults(func=Interface.do_groupadd)
        for param in argv[1:]:
            groupadd_parser.add_argument(param)
 
            if args and not ctx.allow_extra_args and not ctx.resilient_parsing:
                ctx.fail('Got unexpected extra argument%s (%s)'
                        % (len(args) != 1 and 's' or '',
                            ' '.join(map(make_str, args))))
         
        # cat command
        cat_parser = subparsers.add_parser('cat')
        cat_parser.set_defaults(func=Interface.do_cat)
        for param in argv[1:]:
            cat_parser.add_argument(param)
 
            if args and not ctx.allow_extra_args and not ctx.resilient_parsing:
                ctx.fail('Got unexpected extra argument%s (%s)'
                        % (len(args) != 1 and 's' or '',
                            ' '.join(map(make_str, args))))
         
        # getaccount command
        getaccount_parser = subparsers.add_parser('getaccount')
        getaccount_parser.set_defaults(func=Interface.do_getaccount)
        for param in argv[1:]:
            getaccount_parser.add_argument(param)
 
            if args and not ctx.allow_extra_args and not ctx.resilient_parsing:
                ctx.fail('Got unexpected extra argument%s (%s)'
                        % (len(args) != 1 and 's' or '',
                            ' '.join(map(make_str, args))))
         
        # passwd command
        passwd_parser = subparsers.add_parser('passwd')
        passwd_parser.set_defaults(func=Interface.do_passwd)
        for param in argv[1:]:
            passwd_parser.add_argument(param)
 
            if args and not ctx.allow_extra_args and not ctx.resilient_parsing:
                ctx.fail('Got unexpected extra argument%s (%s)'
                        % (len(args) != 1 and 's' or '',
                            ' '.join(map(make_str, args))))
         
         
        # begin accepting commands from user
        interface = Interface()
        interface.prompt(">")
        interface.cmdloop("Starting prompt...")
        ctx.login('admin', argv[0])
         
        args = p.parse_args()
        args.func(args)
         
     
    def fail(self, message):
        """Aborts program with a specific error message.
        :param message: the error message to fail with."""
        raise UsageError(message, self)
         
     
 
if __name__ == "__main__":
    Handle.main(sys.argv[1:], ctx)
 
