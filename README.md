# RCEAAS
## Remote code execution as a service

It simply allows you to send a command to a machine and get the output.

By default it runs everything and listens on port 5000 but you can change that

There is no security in this. Don't run it as root

### How to use
curl -X POST http://127.0.0.1:5000/rce -F 'cmd=ls -la'