python3 -m pip install --upgrade pip
python3 -m pip install -U selenium
python3 -m pip install -U requests
PY_PATH=`which python3`
echo $PY_PATH
cd `dirname $0`
DIR=`pwd`
F="/gf_club_bt002.py"
FILE_PATH=$DIR$F
echo $FILE_PATH
TIME=`python3 $DIR/my_info.py`
echo $TIME
(crontab -l; echo "$TIME * * * $PY_PATH $FILE_PATH > $DIR/cron_log/\`date '+\%Y_\%m_\%d'\`.log 2>&1" ) | crontab -


