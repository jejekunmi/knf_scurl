#!/usr/bin/python

import sys, os
from datetime import datetime, timedelta

# retrieve the server's certificate if you don't already have it

# be sure to examine the certificate to see if it is what you expected
#
# Windows-specific:
# - Use NUL instead of /dev/null.
# - OpenSSL may wait for input instead of disconnecting. Hit enter.
# - If you don't have sed, then just copy the certificate into a file:
#   Lines from -----BEGIN CERTIFICATE----- to -----END CERTIFICATE-----.
#
# openssl s_client -servername www.example.com -connect www.example.com:443 < /dev/null | sed -n "/-----BEGIN/,/-----END/p" > www.example.com.pem
 
# extract public key in pem format from certificate
# openssl x509 -in www.example.com.pem -pubkey -noout > www.example.com.pubkey.pem
 
# convert public key from pem to der
# openssl asn1parse -noout -inform pem -in www.example.com.pubkey.pem -out www.example.com.pubkey.der
 
# sha256 hash and base64 encode der to string for use
# openssl dgst -sha256 -binary www.example.com.pubkey.der | openssl base64

#url = "pinning-test.badssl.com"
# url = "apple.com"
dir_path = os.path.dirname(os.path.realpath(__file__)) + "/pinnedcert/"

def did_command_pass(command):
    return not bool((os.system(command)) >> 8)

def extract_PEM(url):
	command1 = "openssl s_client -servername https://www." + url + " -connect www." + url + ":443 < /dev/null | sed -n \"/-----BEGIN/,/-----END/p\" > " + dir_path + url + ".pem"
	command2 = "openssl x509 -in " + dir_path + url + ".pem -pubkey -noout > " + dir_path + url + ".pubkey.pem"

	print "****************"
	print command1
	passed = did_command_pass(command1)

	if passed:
		print "certificated retrieved"

	print "****************"
	print command2
	passed2 = did_command_pass(command2)
	if passed2:
		print "public key extracted"

extract_PEM(url)
