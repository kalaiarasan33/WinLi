# WinLi
Python flask app for windows and linux to execute command in remote

# Windows setup
# Execute below command to enable winrm protocal and open port 5986
# Reference https://pypi.org/project/pywinrm/0.2.2/

  * Enabling WinRM on remote host
  * Enable WinRM over HTTP and HTTPS with self-signed certificate (includes firewall rules):

# from powershell:
  I.  Invoke-Expression ((New-Object System.Net.Webclient).DownloadString('https://raw.githubusercontent.com/ansible/ansible/devel/examples/scripts/ConfigureRemotingForAnsible.ps1'))
  Enable WinRM over HTTP for test usage (includes firewall rules):

  II.  winrm quickconfig
  Enable WinRM basic authentication. For domain users, it is necessary to use NTLM, Kerberos or CredSSP authentication (Kerberos and NTLM authentication are enabled by default CredSSP isn’t).

# from cmd:
    III. winrm set winrm/config/service/auth @{Basic="true"}
    Enable WinRM CredSSP authentication. This allows double hop support so you can authenticate with a network service when running command son the remote host. This command is run in Powershell.

# No setup required for linux, ssh with password

## Setup config for deployment ##
# copy code in environment 

pip install -r requirements.txt

# start application

Python main.py

## Steps: ##
# 1. Give username and password od machine in landing page --> login
# 2. * Select os - windows or linux
      * Give ip -  ex. 192.168.0.0
         * If multiple ip list use comman seperator  -  ex. 192.168.0.0,192.168.0.1
     * Give Command to Execute
   
  



