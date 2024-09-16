Archives all files in a specific directory (in this sample, the user's home directory)

tar -czPf /home/devops/backup-home-stas_$(date +%F).tar.gz /home/stas/*
tar -czPf /home/devops/backup-home-stas_$(date +%F).tar.gz "$HOME"/*


-c, --create               create a new archive
-z, --gzip, --gunzip, --ungzip   filter the archive through gzip
-P, --absolute-names       don't strip leading '/'s from file names
-f, --file=ARCHIVE         use archive file or device ARCHIVE)
