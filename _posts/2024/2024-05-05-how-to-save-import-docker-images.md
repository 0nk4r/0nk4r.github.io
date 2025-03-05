---
layout: post
title: How to save/import docker images
date: 2024-05-05 19:32 +0000
last_modified_at: 2024-05-18 02:04:45 +0000
tags: [docker, linux]
published: false
---


```
while read image container_id; do
    image=$(echo $image | sed -e 's/[^A-Za-z0-9._-]/_/g')
    docker export $container_id > "${image//\//_}-${container_id}.tar"  
  done < <(docker ps -a -f status=exited | tail -n +2 | awk '{ print $2 " " $1 }')
```

```
while read image version image_id; do
    image=$(echo $image | sed -e 's/[^A-Za-z0-9._-]/_/g')
    docker save $image_id > "${image//\//_}-${version}-${image_id}.tar"
  done < <(docker images| tail -n +2 | grep -v '<none>' | awk '{ print $1 " " $2 " " $3 }')
```