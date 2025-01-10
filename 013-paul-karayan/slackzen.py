import marimo

__generated_with = "0.9.14"
app = marimo.App(width="medium")


@app.cell
def __():
    import marimo as mo
    return (mo,)


@app.cell
def __(mo):
    mo.md(
        """
        # SlackZen: just leave™

        ---

        ### 「片手の音を聞いたことがあるか？」
        *「山の頂上に達したら、登り続けよ。」  
        「折れない竹は、風に逆らうオークよりも強い。」  
        「PKファイヤー！私は世界の大破壊者、時です」  
        「空の指 | あなたを愛する | 風そよぐ」*

        ---

        "処理には最大5分かかることがあります。ウィンドウを閉じないでください。 "
        "(The process may take up to 5 minutes. Please do not close the window.)"
        """
    )
    return


@app.cell
def __(HTTPException, TSLACK_BOT_TOKEN, whitelist):
    import os

    from pydantic import BaseModel
    from retrying import retry
    from slack_sdk import WebClient
    from slack_sdk.errors import SlackApiError


    SLACK_BOT_TOKEN = os.getenv("SLACK_BOT_TOKEN")
    client = WebClient(token=TSLACK_BOT_TOKEN)

    WHITELIST = [
        "eng",
        "general",
        "it-requests"
        # etc... etc
    ]



    class SlackAction(BaseModel):
        identifier: str
        categories: list[str]

    class ChannelRequest(BaseModel):
        channel_id: str

    @retry(
        stop_max_attempt_number=5,
        wait_exponential_multiplier=1000,
        wait_exponential_max=10000,
        retry_on_exception=lambda e: isinstance(e, SlackApiError)
        and e.response["error"] == "ratelimited",
    )
    def get_user_id(identifier: str):
        try:
            response = client.users_list()
            print(response)
            for user in response["members"]:
                if (
                    user["id"] == identifier
                    or user["profile"].get("email") == identifier
                    or user["profile"].get("display_name") == identifier
                ):
                    return user["id"]
        except SlackApiError as e:
            print(f"Error fetching users: {e.response['error']}")
        return None


    def fetch_all_channels():
        channels = []
        cursor = None
        try:
            while True:
                response = client.conversations_list(cursor=cursor, limit=1000)
                if response["ok"]:
                    channels.extend(
                        [
                            channel
                            for channel in response["channels"]
                            if not channel["is_archived"]
                        ]
                    )
                    cursor = response.get("response_metadata", {}).get("next_cursor")
                    if not cursor:
                        break
                else:
                    print(f"Error fetching channels: {response['error']}")
                    break
        except SlackApiError as e:
            print(f"Error fetching channels: {e.response['error']}")
        return channels


    @retry(
        stop_max_attempt_number=5,
        wait_exponential_multiplier=1000,
        wait_exponential_max=10000,
        retry_on_exception=lambda e: isinstance(e, SlackApiError)
        and e.response["error"] == "ratelimited",
    )
    def remove_user_from_channel(channel_id, user_id):
        client.conversations_kick(channel=channel_id, user=user_id)


    def leave_channels(user_id, whitelist):
        channels = fetch_all_channels()
        removed_channels = []
        for channel in channels:
            if channel["name"] not in whitelist:
                try:
                    remove_user_from_channel(channel["id"], user_id)
                    removed_channels.append(channel["name"])
                except SlackApiError as e:
                    if e.response["error"] == "not_in_channel":
                        pass
                    else:
                        print(
                            f"Error removing user {user_id} from channel {channel['name']}: {e.response['error']}"
                        )
        return removed_channels


    def manage_channels(username):
        user_id = get_user_id(username.value)
        if not user_id:
            raise HTTPException(status_code=404, detail="User not found")



        ## if you want to have multiple groups of whitelists, you can do this... and pass in those values natch
        # whitelist = []
        # if eng.value:
        #     whitelist.extend(ENG_WHITELIST)
        # if biz.value:
        #     whitelist.extend(BIZ_WHITELIST)

        print(whitelist. user_id)

    def remove_all_from_channel(request: ChannelRequest):
        try:
            channel_id = request.channel_id
            if not request.channel_id:
                raise HTTPException(status_code=404, detail="Channel not found")

            members_response = client.conversations_members(channel=request.channel_id)
            members = members_response["members"]

            removed_members = []
            failed_members = []
            for member in members:
                try:
                    remove_user_from_channel(request.channel_id, member)
                    removed_members.append(member)
                except SlackApiError as e:
                    if e.response["error"] in ["not_in_channel", "not_supported", "cant_kick_self"]:
                        failed_members.append(member)
                        continue
                    else:
                        raise HTTPException(status_code=500, detail=f"Error removing user {member}: {e.response['error']}")

            return {
                "message": f"All removable members removed from channel {request.channel_id}",
                "removed_members": removed_members,
                "failed_members": failed_members
            }

        except SlackApiError as e:
            raise HTTPException(status_code=500, detail=f"Error: {e.response['error']}")
    return (
        BaseModel,
        ChannelRequest,
        SLACK_BOT_TOKEN,
        SlackAction,
        SlackApiError,
        WHITELIST,
        WebClient,
        client,
        fetch_all_channels,
        get_user_id,
        leave_channels,
        manage_channels,
        os,
        remove_all_from_channel,
        remove_user_from_channel,
        retry,
    )


@app.cell
def __(get_user_id):
    ## show that i'm working, please
    user = get_user_id("pk")
    print(user)
    return (user,)


@app.cell
def __(mo):
    # create the gui
    form = (
            mo.md('''
            **Slack Zen**

            {username}

        ''')
        .batch(
            username=mo.ui.text(label="Username to remove", placeholder="@pk"),
        )
        .form()
    )
    return (form,)


@app.cell
def __(form, mo):
    mo.vstack([form, mo.md(f"Has value: {form.value}")])
    return


@app.cell
def __(form, manage_channels, mo):
    if mo.cli_args():
        output = ""
        manage_channels(
            mo.cli_args().get("username")
        )

    elif form.value:
        form_value = form.value
        output = manage_channels(
            mo.cli_args().get("username")
        )

    else:
        output = ""

    output
    return form_value, output


@app.cell
def __(mo):
    mo.md(
        r"""
        ---

        ### 「あるものを得たいなら、まずそれを与えよ。」
        *「春の景色に、良いも悪いもない。花が自然に咲き、枝が伸びたり、縮んだり。」  
        「野生のガチョウは、その跡を残さない。」  
        「歩くときは歩く、食べるときは食べる。」  
        「PKファイヤー！私は世界の大破壊者、時です」*
        """
    )
    return


if __name__ == "__main__":
    app.run()
