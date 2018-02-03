from wordpress import API
import os
import json


class Postman:

    DEFAULT_FEATURED_MEDIA = 151
    DEFAULT_CATEGORY = 13

    def __init__(self, url, username, password):
        self.__wp_api = API( url=url, api="wp-json", version='wp/v2',
                             wp_user=username, wp_pass=password,
                             basic_auth=True, user_auth=True,
                             consumer_key="", consumer_secret="")
        assert self.__wp_api.get("categories").status_code == 200

    def upload_media(self, file_path):
        assert os.path.exists(file_path), "img should exist at {}".format(file_path)
        data = open(file_path, 'rb').read()
        filename = os.path.basename(file_path)
        _, extension = os.path.splitext(filename)
        headers = {
            'cache-control': 'no-cache',
            'content-disposition': 'attachment; filename=%s' % filename,
            'content-type': 'image/%s' % extension
        }
        response = self.__wp_api.post("media", data, headers=headers)
        print "Media upload response status:{}".format(response.status_code)
        return response.json()

    def create_post(self, post_dir, status):
        assert os.path.exists(post_dir), "Post Directory should exist at {}".format(post_dir)
        with open(os.path.join(post_dir, "metadata.json"), 'r') as f:
            metadata = json.loads(f.read())
            post = {'slug': metadata['information']['slug'], 'title': metadata['information']['title']}
            if 'title-img' in metadata['information'] and metadata['information']['title-img']:
                media = self.upload_media(os.path.join(post_dir, metadata['information']['title-img']))
                post['featured_media'] = media['id']
            else:
                post['featured_media'] = Postman.DEFAULT_FEATURED_MEDIA
            post['status'] = status
            post['categories'] = [Postman.DEFAULT_CATEGORY]
            assert metadata['information']['content-file']
            with open(os.path.join(post_dir, metadata['information']['content-file'])) as c:
                post['content'] = c.read().decode('utf-8')
            headers = {
                'content-type': 'application/json'
            }
            response = self.__wp_api.post("posts", data=post, headers=headers)
            print "Create Post response status:{}".format(response.status_code)
            return response

if __name__ == "__main__":
    Postman('http://localhost:8000','admin', 'bEnM sw5m wM8f nRZr YJvX nNTi')\
        .create_post('/Users/dbansal/Work/MyCode/wp-auto-poster/posts/posts0016', 'publish')
