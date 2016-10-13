#!/bin/bash
cd /etc/openvpn/
echo "qwe123" | sudo -S openvpn --config bfd_data.ovpn
