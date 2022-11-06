python3 -m pip install --upgrade pip
python3 -m pip install -U selenium
python3 -m pip install -U requests
PY_PATH=`which python3`
echo $PY_PATH
DIR=`pwd`
F="/gf_club_bt002.py"
FILE_PATH=$DIR$F
echo $FILE_PATH
DATE="date "+\%Y_\%m_\%d""
(crontab -l; echo "0 20 * * * $PY_PATH $FILE_PATH > $DIR/cron_log/`$DATE`.log 2>&1") | crontab -

