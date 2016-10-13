#!/usr/bin/expect

spawn  ssh xue.bai@192.168.22.18

expect "password:"
send "1qaz@WSX\n"
expect "Input:"
send "0\n"
expect "Input:"
send "0\n"
expect "Input:"
send "s:3222\n"
interact
