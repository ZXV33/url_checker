■OS
CentOS Linux release 7.3.1611 (Core)

■ソフトウェア(その他）
geckodriver-v0.18.0-linux64.tar.gz

■ソフトウェア(RPM）
python34-3.4.5-4.el7.x86_64
python34-pip-8.1.2-5.el7.noarch
firefox-52.4.0-1.el7.centos.x86_64

■ソフトウェア(PIP）
selenium (3.5.0)
※いらないかも。
　→PyVirtualDisplay (0.2.1)


■インストール方法
yum install epel-release
yum install python34-3.4.5-4.el7.x86_64 python34-pip-8.1.2-5.el7.noarch
yum install firefox-52.4.0-1.el7.centos.x86_64

pip3 install selenium==3.5.0
curl -O https://github.com/mozilla/geckodriver/releases/download/v0.18.0/geckodriver-v0.18.0-linux64.tar.gz

最後にファイルを展開


■利用方法
cd url_checker
./url_checker.py ${csvfile}


■CSVファイルフォーマット
2列。
URL,スクリーンショットのファイル名

例：
"https://www.google.co.jp/",google.png

