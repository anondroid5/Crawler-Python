#coding: UTF-8
import os
import time
import urllib2
from twython import Twython
 
u"""
ツイッターで投稿された画像を一括でダウンロードする
"""
 
# 画像を保存するディレクトリ(予め作成しておく)
# 各ユーザの画像は、./images/screen_name/ 内に保存される
IMAGES_DIR = './images/'
 
# Twitter 認証関係 https://dev.twitter.com/apps
# Consumer key
CK='dh8kDj98CtO7lZNPA5xRLw'
# Consumer secret
CS='qiUhfh5kwJrE8EWqjHFbG8EKwio1d8KPX4gE9yeGY'
# Access token
ATK='1598997848-EyVYgiPfpp9YUA0bUUXzTCUpsZyuSYIMpzfrFnG'
# Access token secret
ATS='rHbEFVcRJp31QcvkzOjbEaOrYZrKfqSNt644X2b8kVd4V'
 
# 取得するツイート数の最大値の設定(以下の2つの値の積)
NUM_PAGES       = 10         # 取得するページ数
TWEET_PER_PAGE  = 200       # 1ページあたりのツイート数(最大200)
 
# 画像をダウンロードするユーザのスクリーン名を1行に1人ずつ記入する(@の有無は問わない)
SCREEN_NAMES ="""
@reali_ze
"""
class TwitterImageDownloader(object):
    u"""Twitterから画像をダウンロードする"""
    def __init__(self):
        super(TwitterImageDownloader, self).__init__()
        self.twitter =Twython(app_key=CK, app_secret=CS, oauth_token=ATK, oauth_token_secret=ATS)
 
    def read_ids(self):
        ids_all = [line.replace('@', '') for line in SCREEN_NAMES.splitlines() if line]
        ids = sorted(list(set(ids_all)))
        return ids
     
    def get_timeline(self, screen_name):
        max_id = ''
        url_list = []
        for i in xrange(NUM_PAGES):
            try:
                print 'getting timeline : @', screen_name, (i+1), 'page'
                tw_result = (self.twitter.get_user_timeline(screen_name=screen_name, count=TWEET_PER_PAGE, max_id=max_id)
                    if max_id else self.twitter.get_user_timeline(screen_name=screen_name, count=TWEET_PER_PAGE))
                time.sleep(5)
            except Exception as e:
                print "timeline get error ", e
                break
            else:
                for result in tw_result:
                    if 'media' in result['entities']:
                        media = result['entities']['media']
                        for url in media:
                            url_list.append(url['media_url'])
                    max_id = result['id']
            if len(tw_result) < TWEET_PER_PAGE:
                break
        return url_list
 
    def create_folder(self, save_dir):
        try:
            os.mkdir(save_dir)
        except Exception as e:
            print 'cannot make dir', e
        file_list = os.listdir(save_dir)
        return file_list
 
    def get_file(self, url, file_list, save_dir):
        file_name = url[url.rfind('/')+1:]
        url_large = '%s:large'%(url)
        if not file_name in file_list:
            save_path = os.path.join(save_dir, file_name)
            try:
                print "download", url_large
                url_req = urllib2.urlopen(url_large)
            except Exception as e:
                print "url open error", url_large, e
            else:
                print "saving", save_path
                img_read = url_req.read()
                img = open(save_path, 'wb')
                img.write(img_read)
                img.close()
                time.sleep(1)
        else:
            print "file already exists", file_name
 
    def download(self):
        screen_name_list = self.read_ids()
        num_users = len(screen_name_list)
        for i, screen_name in enumerate(screen_name_list):
            save_dir  = os.path.join(IMAGES_DIR, screen_name)
            file_list = self.create_folder(save_dir)
 
            url_list = self.get_timeline(screen_name)
            num_urls = len(url_list)
            for j, url in enumerate(url_list):
                self.get_file(url, file_list, save_dir)
                print "%d / %d users, %d / %d pictures"%((i+1), num_users, (j+1), num_urls)
 
def main():
    tw = TwitterImageDownloader()
    tw.download()
 
if __name__ == '__main__':
    main()