from getReplies import getRepliesNetwork
import pandas as pd

def bskyRepliesNetwork(uri):
    if isinstance(uri,list) and len(uri) > 1:
        bsky_replies_net = [r for r in map(getRepliesNetwork, uri)]
        bsky_replies_net_df = pd.concat(bsky_replies_net)
        return bsky_replies_net_df
    else:
        bsky_replies = getRepliesNetwork(uri)
        return bsky_replies
    
    
