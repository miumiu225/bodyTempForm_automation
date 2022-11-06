#実行権限を付与
chmod u+x test_open.command
＃commandfileのあるディレクトリをメインディレクトリに設定
cd `dirname $0`


(crontab -l; echo "0 20 * * * /path/to/cmd > /dev/null 2>&1") | crontab -