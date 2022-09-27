import time
import facebook as fb
import requests
import json
# Get Access token - Follow the video on how to get access token for your fb account
access_token = "EAAF3FXOcnrQBAPvmXb0PBRRI4bOj3L0ATfW4TPcGZA5Kcp6ULrjO1s0EynS1qYp4yGPhDrVgNQZA4AwmMkqEAaadyNT8HiTt9QGhZBd006KfvUD0dcADde8kmsd9v995IDhoZBkkipIz0rqT4mwA1IP9NMLjwDf3kcwGLrD5PaiH0W1nukprM1FR0dUTZC055wbRsRLR1m8mewZBmQRqhg"

# The Graph API allows you to read and write data to and from the Facebook social graph
asafb = fb.GraphAPI(access_token)

commentID=[]
comments = []
readCommentsUrl = 'https://graph.facebook.com/v2.1/105132792352632_105564952309416/comments' 

url = readCommentsUrl +"?access_token="+ access_token

def get_comment():

    req = requests.get(url)

    content = req.json()

    for r in content['data']:
        if (r['message'] == "ddd"): # and checkCommentEligibility(r, pageAccessToken):		#deciding for which content comment auto reply is to be done.
         comments.append(r)


def coment_after_cheak():
    with open('sample.json', 'r') as openfile:
        # Reading from json file
        old_list_comment = json.load(openfile)
    
    for cID in comments:
        if cID['id'] in old_list_comment:
            pass
        else:
            commentID.append(cID['id'])

    reply = 'verified'
    for cID in commentID:
        posturl = 'https://graph.facebook.com/%s/comments?access_token=%s' % (cID, access_token)
        print ("Posting for the id : %s with url %s" % (cID, posturl))
        req = requests.post(posturl, data={'message': reply})
    # print(comments) 
    with open("sample.json", "w") as outfile:
        json.dump(old_list_comment+commentID, outfile) 



# while (1==1):
#     # print(url)
#     get_comment(url)
#     commentID=[]
#     coment_after_cheak()
#     time.sleep(3)

  


    # print(readComments("105132792352632_105564952309416",access_token,"s"))
