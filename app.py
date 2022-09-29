from flask import Flask
import pandas as pd
import dropbox
import os
app = Flask(__name__)

@app.route('/')
def hello_world():
#     dropbox_access_token= "NVwGrPvFLxgAAAAAAAAAAVUBiyewqJ5KTDlXkSBRNBBsH2-aZ9iKQvRkP1bIDy_G"    #Enter your own access token
#     client = dropbox.Dropbox(dropbox_access_token)
#     print("[SUCCESS] dropbox account linked")

#     client.files_delete("/TEST/Sep-24-2022.csv")
#     dropbox_path= "/TEST/output/sample1.csv"
#     # initialize list of lists
#     data = [['tom', 10], ['nick', 15], ['juli', 14]]

#     # Create the pandas DataFrame
#     df = pd.DataFrame(data, columns=['Name', 'Age'])

#     # print dataframe.
#     df.to_csv('/output/sample.csv')
#     dropbox_access_token= "NVwGrPvFLxgAAAAAAAAAAVUBiyewqJ5KTDlXkSBRNBBsH2-aZ9iKQvRkP1bIDy_G"    #Enter your own access token
#     client = dropbox.Dropbox(dropbox_access_token)
#     client.files_upload(open('/output/sample.csv', "rb").read(), dropbox_path)
    arr = os.listdir()
    return arr
#     return 'Hello, World!'

if __name__ == "__main__":
    app.run(debug=True, port=10000)
