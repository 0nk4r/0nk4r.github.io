---
layout: post
title: Trigger Github Pages build
date: 2019-06-29 10:14 -0700
tags: [Tools]
---

I recently moved the `_layouts` and `_sass` folders into their own theme repo.
This resulted in me having trouble updating my website automatically when the
theme is updated. I tried pushing empty commits to the Github pages repo but
that started to get annoying after sometime. I did a little digging and found
that github has an [Pages Api](https://developer.github.com/v3/repos/pages/)
for exactly this.
<!-- more -->
## Get Authorization token
First go to [https://github.com/settings/tokens](https://github.com/settings/tokens)
and under personal access tokens, click on **Generate new token**. Give the
token a name and select `public_repo` scope and click **Generate token**
button at the bottom. Copy the token value and store it in a safe place.

![Personal access tokens]({{"/assets/images/20190629/gh-pages-token.png"|absolute_url}})

## API Request

```bash
curl -H "Authorization: token $AUTH_TOKEN" -H "Accept: application/vnd.github.mister-fantastic-preview+json" -X POST https://api.github.com/repos/:user/:repo/pages/builds
```
{: .code-wrap}

In the above bash snippet replace `$AUTH_TOKEN` with your Personal access
token. Then replace the `:user` with your username and `:repo` with your
*gh-pages* repository name.

When you run the above command in bash, you should get something like this.

```
{
  "status": "queued",
  "url": "https://api.github.com/repositories/12667135/pages/builds/latest"
}
```
