import pandas as pd
from followers import bskyFollowers
from following import bskyFollowing
import os

def FollowerFollowing(handle):

  followers = bskyFollowers(handle)
  following = bskyFollowing(handle)

  # Ensure both are DataFrames
  if not isinstance(followers, pd.DataFrame):
     raise ValueError("The 'followers' data must be a Pandas DataFrame.")
  if not isinstance(following, pd.DataFrame):
     raise ValueError("The 'following' data must be a Pandas DataFrame.")

  bskyCombined = pd.concat([followers,following])

  # save to CSV
  output_dir = "result"
  file_name = "Followers.csv"
  file_path = os.path.join(output_dir, file_name)

  # check if directory exists; if not, create it
  if not os.path.exists(output_dir):
      os.makedirs(output_dir)

  bskyCombined.to_csv(file_path,index=False)

  return bskyCombined, file_path



if __name__ == "__main__":
    follower_following = FollowerFollowing(handle = "samuel.bsky.team")
    print(follower_following)
