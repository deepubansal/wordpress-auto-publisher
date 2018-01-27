# Wordpress-auto-publisher

This is an auto-publisher written using `wp-api-python` module for Wordpress REST API. 
The main idea behind this publisher is to auto-publish a set of posts organized in a certain format, as depicted in `sample-posts` directory, one by one. Each execution of `main.py` as below chooses one of the posts from base directory and uploads it. It also moves the `post` directory to `done` sub-directory(which gets created on first run) and adds an entry in `progress` file (which gets created on first run).

## Requirements:
* Structure of POSTS directory as mentioned in next section.
* Either of these plugins on target wordpress installation
  * https://github.com/WP-API/Basic-Auth
  * https://github.com/georgestephanis/application-passwords/
  

## Usage
`python main.py 'url' 'username' 'password' 'path-to-posts-dir'`

## Structure of POSTS directory:

```
sample-posts\
  - post2
    - files\
      - jpg (referred in metadata.json)
      - html (referred in metadata.json)
    - metadata.json
  - post3
  .
  .
  .
  - done\
    -post1\
      -files
      ....
      ....
  - progress
```



## Why does it upload only one post:
  
Because, it is intended to be run using a scheduler or cron job which can periodically upload posts one by one without any manual intervention. Once `posts` folder is setup correctly with multiple posts, then it can just silently create posts every day or every week.

