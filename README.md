# How to run the server ?

Download the code in this repository by clicking on the link below.
[Download Code](https://github.com/data-charya/demo-flask/archive/refs/heads/main.zip)

---
After you have downloaded the files you will need to extract the zip file.
- Right click on the zip file and click extract here or you could run the command below to extract it. Replace your_user_name with your ubuntu username.
- If you are unsure about what your username is just run whoami in your terminal. This command will return your username
- ```
  cd /home/your_user_name/Downloads/
  unzip demo-flask-main.zip
  ```
- Navigate within the folder by launching a terminal window and running
- ```
  cd /home/demo-flask-main/Downloads/demo-flask-main/
  ```
- now that you are in the directory of the code, you can run the command below.
---
Just run the command below in your terminal and you should have your application up and running
```sh
sudo apt update && sudo apt install && sudo apt install python3 -y && sudo apt install python3-flask -y && export FLASK_DEBUG=1 && flask run --port=8181
```
