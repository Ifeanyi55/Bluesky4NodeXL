import numpy as np
import pandas as pd
from auth import client
import os

def getRepliesNetwork(uri):

  # def postUri(url):
  #   post_split = url.split("/")
  #   return "at://" + post_split[4] + "/" + "app.bsky.feed.post/" + post_split[6]

  # uri = postUri(url)
  response = client.app.bsky.feed.get_post_thread(params={"uri":uri})

  # extract thread metadata
  handles = [r.post.author.handle for r in response.thread.replies]
  did = [r.post.author.did for r in response.thread.replies]
  associated = [r.post.author.associated for r in response.thread.replies]
  avatar = [r.post.author.avatar for r in response.thread.replies]
  created_at = [r.post.author.created_at for r in response.thread.replies]
  reply_at = [r.post.indexed_at for r in response.thread.replies]
  display_name = [r.post.author.display_name for r in response.thread.replies]
  text = [r.post.record.text for r in response.thread.replies]
  uri = [r.post.uri for r in response.thread.replies]
  like_count = [r.post.like_count for r in response.thread.replies]
  reply_count = [r.post.reply_count for r in response.thread.replies]
  repost_count = [r.post.repost_count for r in response.thread.replies]
  quote_count = [r.post.quote_count for r in response.thread.replies]
  py_type = [r.post.viewer.py_type for r in response.thread.replies]
  profile_url = ["https://bsky.app/profile/" + r.post.author.handle for r in response.thread.replies]

  # parse dates
  created_at_parse = [" ".join(created_at[i].split("T")) for i in range(len(created_at))]
  created_at_parse2 = ["".join(created_at_parse[i].split("Z")) for i in range(len(created_at_parse))]

  reply_at_parse = [" ".join(reply_at[i].split("T")) for i in range(len(reply_at))]
  reply_at_parse2 = ["".join(reply_at_parse[i].split("Z")) for i in range(len(reply_at_parse))]

  # get parent post metatdata
  v2_handle = np.repeat(response.thread.post.author.handle,len(handles))
  v2_did = np.repeat(response.thread.post.author.did,len(did))
  v2_associated = np.repeat(response.thread.post.author.associated,len(did))
  v2_avatar = np.repeat(response.thread.post.author.avatar,len(avatar))
  v2_created_at = response.thread.post.author.created_at
  v2_post_at = response.thread.post.indexed_at
  v2_name = np.repeat(response.thread.post.author.display_name,len(display_name))
  v2_text = np.repeat(response.thread.post.record.text,len(text))
  v2_profile_url = np.repeat("https://bsky.app/profile/" + response.thread.post.author.handle,len(profile_url))
  v2_uri = np.repeat(response.thread.post.uri,len(uri))

  # parse dates
  v2_created_at_parse = " ".join(v2_created_at.split("T"))
  v2_created_at_parse2 = "".join(v2_created_at_parse.split("Z"))

  v2_post_at_parse = " ".join(v2_post_at.split("T"))
  v2_post_at_parse2 = "".join(v2_post_at_parse.split("Z"))

  # convert into data frame
  replies_net = pd.DataFrame(
    {
        "Vertex1":display_name,
        "Vertex2": v2_name,
        "Vertex1_Text": text,
        "Vertex1_CreatedAt": created_at_parse2,
        "Vertex1_ReplyAt": reply_at_parse2,
        "Vertex1_Handle": handles,
        "Vertex1_ProfileURL": profile_url,
        "Vertex1_Avatar": avatar,
        "Vertex1_LikeCount": like_count,
        "Vertex1_ReplyCount": reply_count,
        "Vertex1_RepostCount": repost_count,
        "Vertex1_QuoteCount": quote_count,
        "Vertex1_DID": did,
        "Vertex1_Associated": associated,
        "Vertex1_URI": uri,
        "Vertex1_PyType": py_type,
        "Vertex2_Handle": v2_handle,
        "Vertex2_ProfileURL": v2_profile_url,
        "Vertex2_Avatar": v2_avatar,
        "Vertex2_Text": v2_text,
        "Vertex2_Associated": v2_associated,
        "Vertex2_DID": v2_did,
        "Vertex2_CreatedAt": np.repeat(v2_created_at_parse2,len(created_at)),
        "Vertex2_PostAt": np.repeat(v2_post_at_parse2,len(reply_at)),
        "Vertex2_URI": v2_uri
    }
  )

  # save DataFrame to csv
  # output_dir = "output"
  # file_name = "Replies.csv"
  # file_path = os.path.join(output_dir, file_name)
  #
  # # check if output director exists; if not, create it.
  # if not os.path.exists(output_dir):
  #     os.makedirs(output_dir)
  #
  # replies_net.to_csv(file_path,index=False)

  return replies_net


if __name__ == "__main__":
    # test code
    replies_net = getRepliesNetwork("at://anniefortruth1.bsky.social/app.bsky.feed.post/3ldqbzif2j22l")
    print(replies_net)
