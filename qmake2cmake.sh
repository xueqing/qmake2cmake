python3 -m venv env --prompt mpp
source env/bin/activate
pip install -r requirements.txt
# python3.7 -m pip install -r requirements.txt
qmake2cmake_all /home/kiki/github/qt/qmake2cmake/tests/SubdirsDemo --min-qt-version 6.0
# mkdir cbuild && cd cbuild
# cmake -DCMAKE_PREFIX_PATH=/home/kiki/Qt/6.4.0/gcc_64 ../