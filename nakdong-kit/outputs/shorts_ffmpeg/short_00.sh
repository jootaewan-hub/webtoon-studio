#!/usr/bin/env bash
set -e
# 표지
cd "$(dirname "$0")/../.."
mkdir -p outputs/shorts_ffmpeg/seg00
ffmpeg -y -loglevel error -loop 1 -i "thumbs/0-001.svg" -t 8.0 -vf "scale=1080:1920:force_original_aspect_ratio=decrease,pad=1080:1920:(ow-iw)/2:(oh-ih)/2:color=black,zoompan=z='min(zoom+0.0008,1.08)':d=192:s=1080x1920:fps=24,format=yuv420p" -r 24 "outputs/shorts_ffmpeg/seg00/0-001.mp4"
ffmpeg -y -loglevel error -loop 1 -i "thumbs/0-002.svg" -t 2.2 -vf "scale=1080:1920:force_original_aspect_ratio=decrease,pad=1080:1920:(ow-iw)/2:(oh-ih)/2:color=black,zoompan=z='min(zoom+0.0008,1.08)':d=52:s=1080x1920:fps=24,format=yuv420p" -r 24 "outputs/shorts_ffmpeg/seg00/0-002.mp4"
ffmpeg -y -loglevel error -loop 1 -i "thumbs/0-003.svg" -t 2.4 -vf "scale=1080:1920:force_original_aspect_ratio=decrease,pad=1080:1920:(ow-iw)/2:(oh-ih)/2:color=black,zoompan=z='min(zoom+0.0008,1.08)':d=57:s=1080x1920:fps=24,format=yuv420p" -r 24 "outputs/shorts_ffmpeg/seg00/0-003.mp4"
ffmpeg -y -loglevel error -loop 1 -i "thumbs/0-004.svg" -t 4.1 -vf "scale=1080:1920:force_original_aspect_ratio=decrease,pad=1080:1920:(ow-iw)/2:(oh-ih)/2:color=black,zoompan=z='min(zoom+0.0008,1.08)':d=98:s=1080x1920:fps=24,format=yuv420p" -r 24 "outputs/shorts_ffmpeg/seg00/0-004.mp4"
ffmpeg -y -loglevel error -loop 1 -i "thumbs/0-005.svg" -t 4.3 -vf "scale=1080:1920:force_original_aspect_ratio=decrease,pad=1080:1920:(ow-iw)/2:(oh-ih)/2:color=black,zoompan=z='min(zoom+0.0008,1.08)':d=103:s=1080x1920:fps=24,format=yuv420p" -r 24 "outputs/shorts_ffmpeg/seg00/0-005.mp4"
ffmpeg -y -loglevel error -loop 1 -i "thumbs/0-006.svg" -t 2.9 -vf "scale=1080:1920:force_original_aspect_ratio=decrease,pad=1080:1920:(ow-iw)/2:(oh-ih)/2:color=black,zoompan=z='min(zoom+0.0008,1.08)':d=69:s=1080x1920:fps=24,format=yuv420p" -r 24 "outputs/shorts_ffmpeg/seg00/0-006.mp4"
ffmpeg -y -loglevel error -loop 1 -i "thumbs/0-007.svg" -t 4.6 -vf "scale=1080:1920:force_original_aspect_ratio=decrease,pad=1080:1920:(ow-iw)/2:(oh-ih)/2:color=black,zoompan=z='min(zoom+0.0008,1.08)':d=110:s=1080x1920:fps=24,format=yuv420p" -r 24 "outputs/shorts_ffmpeg/seg00/0-007.mp4"
ffmpeg -y -loglevel error -f concat -safe 0 -i outputs/shorts_ffmpeg/seg00/list.txt -c copy "outputs/shorts_ffmpeg/short_00.mp4"
echo "완료: outputs/shorts_ffmpeg/short_00.mp4 (표지)"
