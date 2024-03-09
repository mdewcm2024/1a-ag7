import os
if not os.path.exists("/home/runner/.ssh"):
       os.makedirs("/home/runner/.ssh")
os.system("mv ./dowmloads/id_rsa.txt /home/runner/.ssh/id_rsa")
os.system("mv ./dowmloads/config.txt /home/runner/.ssh/config")
os.system("chomd og-rwx /home/runner/.ssh/id_rsa")