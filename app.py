import gradio as gr
from atproto import Client
from bskySearchRepliesNet import bskyAllRepliesNet
from bskyFollowerFollowing import bskyFollowerFollowing
from dotenv import load_dotenv
import os
import pandas as pd  # Required for initializing empty DataFrames

# Load environment variables
load_dotenv()

bsky_username = os.environ.get("BSKY_USERNAME")
bsky_password = os.environ.get("BSKY_PASSWORD")

# Login to Bluesky client
client = Client()
client.login(bsky_username, bsky_password)

# Create the Gradio app
with gr.Blocks() as replies:
    gr.HTML("<div style='text-align:center;overflow:hidden;'><h2>Replies Network</h2></div>")
    with gr.Column():
        modal_btn = gr.Button("Info",size="md",interactive=True,visible=True,min_width=50)
    with gr.Row():
        search_query = gr.Text(label="Search Query", placeholder="Enter your search query here")
        # uri_limit = gr.Slider(minimum=0, maximum=9000, value=0, step=10, label="URI Limit", info="Select Number of URIs to Loop Over")
    with gr.Row():
        btn = gr.Button("Search")
        clear = gr.Button("Clear")
    with gr.Column():
        table = gr.Dataframe(label="Replies Network Data")
        # download_btn = gr.DownloadButton("Download CSV")

    # define button click event
    # def click_replies_network(search_query):
    #     replies_net, file_path = bskyAllRepliesNet(search_query)
    #     return replies_net, file_path

    # create modal function
    def modal():
        gr.Info("Please enter one search query at a time!")

    modal_btn.click(
        fn = modal
    )

    btn.click(
        fn=bskyAllRepliesNet,
        inputs=search_query,
        outputs=table
    )
    clear.click(
        lambda: ("", 0, pd.DataFrame()),
        inputs=None,
        outputs=[search_query, table],
        queue=False
    )


with gr.Blocks() as followers:
    gr.HTML("<div style='text-align:center;overflow:hidden;'><h2>Follower Network</h2></div>")
    with gr.Row():
        handle = gr.Text(label="Bsky Handle", placeholder="Enter Bsky handle without the '@' symbol")
    with gr.Row():
        run = gr.Button("Run")
        clear_btn = gr.Button("Clear")
    with gr.Column():
        df = gr.Dataframe(label="Follower Network Data")
        download = gr.DownloadButton("Download CSV")

    # define button click event
    def click_followers_network(handle):
        bskyCombined, file_path = bskyFollowerFollowing(handle)
        return bskyCombined, file_path

    run.click(
        fn=click_followers_network,
        inputs=[handle],
        outputs=[df, download]
    )
    clear_btn.click(
        lambda: ("", pd.DataFrame()),
        inputs=None,
        outputs=[handle, df],
        queue=False
    )

# Create a tabbed interface
app = gr.TabbedInterface(
    [replies, followers],
    ["Replies Network", "Follower Network"],
    title="Bluesky4NodeXL",
    theme = gr.themes.Soft()
)

if __name__ == "__main__":
    app.launch()
