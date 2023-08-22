for i in *; do if [ ! -s "$i" ]; then echo "$(stat --printf "$i %s" "$i")"; fi; done
