#!/bin/sh

exists()
{
  command -v "$1" >/dev/null 2>&1
}

# https://blog.nerde.pw/2016/08/09/jekyll-last-modified-date.html
echo ""
echo "************************************"
echo "*   updating last_modified_at...   *"
echo "************************************"
git diff --cached --name-status | while read a b; do
  echo "* Processing $b..."
  if exists gsed; then
    gsed -i "/---.*/,/---.*/s/^last_modified_at:.*$/last_modified_at: $(date -u "+%Y-%m-%d %T %z")/" "$b"
  else
    sed -i "/---.*/,/---.*/s/^last_modified_at:.*$/last_modified_at: $(date -u "+%Y-%m-%d %T %z")/" "$b"
  fi
  git add $b
done
echo "************************************"
echo "*            ...DONE...            *"
echo "************************************"
echo ""
