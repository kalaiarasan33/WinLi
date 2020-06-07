from winrm.protocol import Protocol
import paramiko
from flask import *  
import boto3
from collections import defaultdict

app = Flask(__name__) 
app.secret_key = "abc"  
  

@app.route('/')  
def login():  
      return render_template('login.html')

@app.route('/adhoc',methods = ['POST'])  
def adhoc(): 
      session['uname']=request.form['uname']
      session['upass']=request.form['upass']
      return render_template('adhoc.html')

@app.route('/server',methods = ['POST'])           

def server():
      os=request.form['os']
      host_s=request.form['host']
      host_l=list(host_s.split(","))  
      cmd=request.form['cmd']
      usern=session['uname']
      userp=session['upass']
      if os =="linux":
            li_output={}
            for host in host_l:
                  #o="***** hostname : {}*****,{}".format(host,)
                  error=["Not able to connect please check "]
                  try:
                        li_output[host]= li(host,cmd,usern,userp)
                  except:
                        li_output[host]= error
                      
            return  render_template("message.html",output=li_output)    
      elif os =="windows":
            wi_output={}
            for host in host_l:
                  #o="***** hostname : {}*****,{}".format(host,win(host,cmd))
                  error=["Not able to connect please check "]
                  try:
                        wi_output[host]= win(host,cmd,usern,userp)
                  except:
                        wi_output[host]=error
                  
            return  render_template("message.html",output=wi_output)  
      



###################################################################################################################   
          
def li(host,cmd,usern,userp):
      username = usern
      passw=userp
      ssh = paramiko.SSHClient()
      ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
      ssh.connect(hostname=host, username=username , password=passw)
      stdin, stdout, stderr = ssh.exec_command(cmd)
      outlines = stdout.readlines()
      res ="".join(outlines)
      resp=[x.strip() for x in res.split('\n')]
      return resp

def win(host,cmd,usern,userp):
      p = Protocol(
      endpoint="https://{}:5986/wsman".format(host),
      transport='ntlm',
      username=usern,
      password=userp,
      server_cert_validation='ignore')
      shell_id = p.open_shell()
      command_id = p.run_command(shell_id, cmd)
      std_out, std_err, status_code = p.get_command_output(shell_id, command_id)
      outlines = std_out.decode("utf-8")
      res ="".join(outlines)
      resp=[x.strip() for x in res.split('\n')]
      p.cleanup_command(shell_id, command_id)
      p.close_shell(shell_id)
      return resp





if __name__ == '__main__':  
   app.run(debug = True)