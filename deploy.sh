#!/bin/bash

# 날짜와 시간 가져오기
current_time=$(date "+%Y-%m-%d %H:%M:%S")

# 사용자에게 커밋 메시지 입력 받기
read -p "커밋 메시지를 입력하세요: " commit_message

# 커밋 메시지가 비어 있으면 기본 메시지 설정
if [ -z "$commit_message" ]; then
  commit_message="Update on $current_time"
else
  commit_message="$commit_message ($current_time)"
fi

# Git 명령어 실행
git add .
git commit -m "$commit_message"
git push

