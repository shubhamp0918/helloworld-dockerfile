
import  re, subprocess, paramiko

cmd='aws ec2 --region ap-northeast-1 describe-instances --query "Reservations[].Instances[][PublicIpAddress][]"'
push=subprocess.Popen(cmd, shell=True, stdout = subprocess.PIPE, text=True)
std_out, err = push.communicate()
ip = re.findall( r'[0-9]+(?:\.[0-9]+){3}', std_out)
print(ip[0])

# Connection to EC2 instance
k = paramiko.RSAKey.from_private_key_file("C:/Users/91738/Downloads/ec2-keypair.pem")
c = paramiko.SSHClient()
c.set_missing_host_key_policy(paramiko.AutoAddPolicy())
print("connecting")
c.connect( hostname = ip[0], username = "ec2-user", pkey = k )
print("connected to {}".format(ip[0]))

# Excuting command on instance
command = "df"
print("Executing {}".format( command ))
stdin , stdout, stderr = c.exec_command(command)
print(stdout.read())
# if stderr:
#     print( "Errors")
#     print(stderr.read())
c.close()