#!/bin/bash
# send a POST request displays the body of the response
curl -sX POST --data "email=hr@holbertonschool.com&subject=I will always be here for PLD" "$1"
