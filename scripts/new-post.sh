#!/bin/sh

echo $PWD

stardate="$(echo $(./scripts/stardate $(date -u '+%Y-%m-%d')) | tr \[\]. -)"
base_path="./_posts/captains-log/$(date -u +%Y)/$(date -u +%m)/"
file_name="$base_path$(date -u '+%Y-%m-%d')-captain-s-log-stardate$stardate.md"

mkdir -p $base_path

echo "---" | tee -a $file_name
echo "layout: post" | tee -a $file_name
echo "title: Captain's log, stardate $(./scripts/stardate $(date -u '+%Y-%m-%d'))" | tee -a $file_name
echo "date: $(date -u '+%Y-%m-%d %T %z')" | tee -a $file_name
echo "last_modified_at: $(date -u '+%Y-%m-%d %T %z')" | tee -a $file_name
echo "tags: [Captain's log, weekly]" | tee -a $file_name
echo "---" | tee -a $file_name

echo "" | tee -a $file_name
echo "This week in review:" | tee -a $file_name
echo "" | tee -a $file_name

echo "<!-- more -->" | tee -a $file_name

for idx in 0 1 2 3 4 5 6
do
  echo "" | tee -a $file_name
  echo "### $(date -u '+%a, %d %b %Y' --date="+$idx day")" | tee -a $file_name
  echo "" | tee -a $file_name
  echo "▣" | tee -a $file_name
done

echo $file_name

ls -lah $base_path
