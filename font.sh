#!/bin/bash
mkdir -p ~/.local/share/fonts
cp "/workspaces/i/CMU Serif.ttf" ~/.local/share/fonts/
fc-cache -fv
fc-list | grep -i "CMU"
echo "Lol."