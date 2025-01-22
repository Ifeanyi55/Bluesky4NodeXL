import pandas as pd
from auth import client

def bskySearch(query):
  # define function to collect all posts containing the search query term
  def get_all_posts(query):
    cursor = None
    posts = []

    while True:
        response = client.app.bsky.feed.search_posts(
            params={'q': query, 'cursor': cursor}
        )
        posts.extend(response.posts)

        cursor = response.cursor
        if not cursor:
            break

    return posts

  # apply function
  all_posts = get_all_posts(query)

  # extract metadata
  handles = [p.author.handle for p in all_posts]
  did = [p.author.did for p in all_posts]
  associated = [p.author.associated for p in all_posts]
  avatar = [p.author.avatar for p in all_posts]
  created_at = [p.author.created_at for p in all_posts]
  display_name = [p.author.display_name for p in all_posts]
  text = [p.record.text for p in all_posts]
  uri = [p.uri for p in all_posts]
  like_count = [p.like_count for p in all_posts]
  reply_count = [p.reply_count for p in all_posts]
  repost_count = [p.repost_count for p in all_posts]
  quote_count = [p.quote_count for p in all_posts]
  py_type = [p.viewer.py_type for p in all_posts]

  # convert into a data frame
  bsky_posts_df = pd.DataFrame(
      {
          "Handles": handles,
          "DID": did,
          "Associated": associated,
          "Avatars": avatar,
          "Created_at": created_at,
          "Display_name": display_name,
          "Text": text,
          "URI": uri,
          "Like_count": like_count,
          "Reply_count": reply_count,
          "Repost_count": repost_count,
          "Quote_count": quote_count,
          "Py_type": py_type
      }
  )

  return bsky_posts_df.head(500)


if __name__=="__main__":
    bskySearch(query = "bluesky")
