import pandas as pd
from auth import client
import requests

def bskyFollowing(handle):
      
  # DID finder
  def did_finder(handle):
    did = requests.get(f"https://bsky.social/xrpc/com.atproto.identity.resolveHandle?handle={handle}")
    return did.json()["did"]

  # collect all following of a user
  def get_all_following(actor_did):
    cursor = None
    following = []

    while True:
        response = client.app.bsky.graph.get_follows(
            params={'actor': actor_did, 'cursor': cursor}
        )
        following.extend(response.follows)

        cursor = response.cursor
        if not cursor:
            break

    return following

  # apply functions
  actor_did = did_finder(handle)
  all_following = get_all_following(actor_did)
  actor_profile = client.app.bsky.actor.get_profile(params={"actor": actor_did})

  # extract metadata for Vertex1 and Vertex2
  vertex1_handle = actor_profile.handle
  vertex1_did = actor_profile.did
  vertex1_avatar = actor_profile.avatar
  vertex1_created_at = actor_profile.created_at
  vertex1_description = actor_profile.description
  vertex1_display_name = actor_profile.display_name
  vertex1_indexed_at = actor_profile.indexed_at
  vertex1_py_type = actor_profile.py_type

  vertex2_handles = [f.handle for f in all_following]
  vertex2_did = [f.did for f in all_following]
  vertex2_avatar = [f.avatar for f in all_following]
  vertex2_created_at = [f.created_at for f in all_following]
  vertex2_description = [f.description for f in all_following]
  vertex2_display_name = [f.display_name for f in all_following]
  vertex2_indexed_at = [f.indexed_at for f in all_following]
  vertex2_py_type = [f.py_type for f in all_following]

  bsky_following_network = pd.DataFrame(
      {
          "Vertex1": vertex1_handle,
          "Vertex2": vertex2_handles,
          "Vertex1_did": vertex1_did,
          "Vertex1_avatar": vertex1_avatar,
          "Vertex1_display_name": vertex1_display_name,
          "Vertex1_description": vertex1_description,
          "Vertex1_created_at": vertex1_created_at,
          "Vertex1_indexed_at": vertex1_indexed_at,
          "Vertex1_py_type": vertex1_py_type,
          "Vertex2_did": vertex2_did,
          "Vertex2_avatar": vertex2_avatar,
          "Vertex2_display_name": vertex2_display_name,
          "Vertex2_description": vertex2_description,
          "Vertex2_created_at": vertex2_created_at,
          "Vertex2_indexed_at": vertex2_indexed_at,
          "Vertex2_py_type": vertex2_py_type
      }
  )

  return bsky_following_network



if __name__ == "__main__":
    following = bskyFollowing(handle = "samuel.bsky.team")
    print(following)



