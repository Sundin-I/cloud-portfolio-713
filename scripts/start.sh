#!/bin/bash
echo "Starting deployment..."
systemctl restart httpd || service httpd restart
