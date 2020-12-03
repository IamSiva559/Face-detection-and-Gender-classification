from flask import Flask
from App import ui

app = Flask(__name__)

# url
app.add_url_rule('/','index',ui.index,methods=['GET','POST'])
# 
if __name__ == "__main__":
    app.run()