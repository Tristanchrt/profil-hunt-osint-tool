import json
from auth import *


def dump(profile):

    followers = []
    following = []
    medias = []
    followerskeys = profile.followers.keys()
    for key in followerskeys:
        followers.append(
            {
                "username": profile.followers[key].username,
                "full_name": profile.followers[key].full_name,
                "pic_url": profile.followers[key].profile_pic_url,
            },
        )

    followingskeys = profile.following.keys()
    for key in followingskeys:
        following.append(
            {
                "username": profile.following[key].username,
                "full_name": profile.following[key].full_name,
                "pic_url": profile.following[key].profile_pic_url,
            },
        )

    for items in profile.medias:
        for tags in items.usertags:
            medias.append(
                {
                    "img_url": items.thumbnail_url,
                    "comment_count": items.comment_count,
                    "like_count": items.like_count,
                    "caption_text": items.caption_text,
                    "user_taged": tags.user.username,
                },
            )

    data = {
        profile.username: {
            "description": profile.description.biography,
            "followers": followers,
            "following": following,
            "media": medias,
        }
    }

    with open("data.json", "w") as fp:
        json.dump(dict(data), fp)

    return data
