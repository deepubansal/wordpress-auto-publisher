import os
from postman import Postman
import time
import shutil


class PostMaster:

    def __init__(self, url, username, password, base_dir):
        assert os.path.exists(base_dir) and os.path.isdir(base_dir)
        self.base_dir = base_dir
        self.postman = Postman(url=url, username=username, password=password)
        self.progress_file = os.path.join(base_dir, "progress")
        if not os.path.exists(self.progress_file):
            open(self.progress_file, 'w').close()
        self.done_folder_name = "done"
        self.done_folder = os.path.join(base_dir, self.done_folder_name)
        if not os.path.exists(self.done_folder) or not os.path.isdir(self.done_folder):
            os.mkdir(self.done_folder)

    def process_next(self):
        posts = filter(lambda x: os.path.isdir(os.path.join(self.base_dir, x)) and x != self.done_folder_name, os.listdir(self.base_dir))
        if posts:
            post_dir = os.path.join(self.base_dir, posts[0])
            self.postman.create_post(post_dir, "publish")
            post_dir_name = os.path.basename(post_dir)
            with open(self.progress_file, "a") as f:
                f.write("{0}:{1}\n".format(post_dir_name, time.strftime("%c")))
            shutil.copytree(post_dir, os.path.join(self.done_folder, post_dir_name))
            shutil.rmtree(post_dir)





