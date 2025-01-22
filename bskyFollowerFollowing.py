from followerFollowing import FollowerFollowing
import gradio as gr
import pandas as pd
import time

def bskyFollowerFollowing(handle):
  # gr.Info(message="Do not include the '@' symbol in the Bsky handle")
  # handle = [h.strip() for h in handle.split(",")]
  # handle = list(handle)
  if isinstance(handle,list) and len(handle) > 1:
    bsky_follower_following_df = []
    for handles in handle:
      bsky_follower_following_df.append(FollowerFollowing(handles))
      time.sleep(2)

    bsky_follower_following_combined = pd.concat([bsky_follower_following_df])

    return bsky_follower_following_combined
  else:
    bsky_follower_following = FollowerFollowing(handle)
    return bsky_follower_following

# def bskyFollowerFollowing(handle):
#     handle = [h.strip() for h in handle.split(",")]
#     if isinstance(handle, list) and len(handle) > 1:
#         bsky_follower_following_df = []
#         for handles in handle:
#             result = FollowerFollowing(handles)
#             if isinstance(result, tuple):
#                 bsky_follower_following_df.append(result[0])  # Append only the DataFrame
#             else:
#                 bsky_follower_following_df.append(result)
#             time.sleep(2)
#
#         bsky_follower_following_combined = pd.concat(bsky_follower_following_df)
#
#         return bsky_follower_following_combined
#     else:
#         result = FollowerFollowing(handle)
#         if isinstance(result, tuple):
#             return result[0]  # Return only the DataFrame
#         return result
