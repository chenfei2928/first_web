import requests

res = requests.get(
    '/api/mgr/sq_mgr/?action=list_course&pagenum=1&pagesize=20')

print(res.status_code)