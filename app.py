from flask import Flask
import dropbox
app = Flask(__name__)

@app.route('/')
def hello_world():
    dropbox_access_token= "NVwGrPvFLxgAAAAAAAAAAVUBiyewqJ5KTDlXkSBRNBBsH2-aZ9iKQvRkP1bIDy_G"    #Enter your own access token
    client = dropbox.Dropbox(dropbox_access_token)
    print("[SUCCESS] dropbox account linked")

    client.files_delete("/TEST/Sep-24-2022.csv")
    return 'Hello, World!'

if __name__ == "__main__":
    app.run(debug=True, port=10000)
