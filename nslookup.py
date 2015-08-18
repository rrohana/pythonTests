#!/usr/bin/python

from subprocess import Popen, PIPE


class Nslookup():
    def __init__(self, host=None):
        self.host = host

    def dns_client(self):
        nsl = 'nslookup %s' % self.host
        try:
            dns_cmd = Popen(nsl, shell=True, stdout=PIPE, stderr=PIPE)
            stdout, stderr = dns_cmd.communicate()
            print (stdout, stderr)
            result = stdout.rstrip().split("\t")
            return result[-1].replace('Address:', '').split("\n")[-1].replace("name = ", '').lstrip()

        except Exception as error:
            print "ERORR -- There was an exception in %s while running %s" % (error, nsl)
            dns_cmd = None

        return dns_cmd


"""Test it"""
bla = Nslookup("www.google.com")

print bla.dns_client()
