chdir H:\master_control
timeout 3 > NUL
python main.py
timeout 15 > NUL
start chrome http://127.0.0.1:5257/