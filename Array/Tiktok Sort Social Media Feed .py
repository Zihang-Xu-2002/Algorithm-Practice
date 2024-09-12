# https://www.fastprep.io/problems/tiktok-sort-social-media-feed
from typing import List

class Solution:
  def sortSocialMediaFeed(self, feed: List[str]) -> List[str]:

    grouped_feed = {}

    for entry in feed:
      timeStamp, userID, post = entry.split(',')

      if userID not in grouped_feed:
        grouped_feed[userID] = []

      grouped_feed[userID].append(entry)
    result = []
    for userID in sorted(grouped_feed.keys()):
      sorted_posts = sorted(grouped_feed[userID], key=lambda x:x[0])
      for item in sorted_posts:
        result.append(item)
    return result