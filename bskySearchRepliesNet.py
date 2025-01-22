from bskyRepliesNet import bskyRepliesNetwork
from getallposts import bskySearch
import pandas as pd
import gradio as gr
import time

def bskyAllRepliesNet(query):
 
  bskySearch_df = bskySearch(query)
  bskyURIs = bskySearch_df["URI"]

  allRepliesNetData = []
  for u in bskyURIs:
    try:
      r = bskyRepliesNetwork(u)
      if not r.empty:
        allRepliesNetData.append(r)
    except Exception as e:
      pass
    # time.sleep(2)
  allRepliesNetData_df = pd.concat(allRepliesNetData)

  # clean dataset of blank cells
  allRepliesNetData_df_clean = allRepliesNetData_df[(allRepliesNetData_df['Vertex1'] != "") & (allRepliesNetData_df['Vertex2'] != "")]

  return allRepliesNetData_df_clean
