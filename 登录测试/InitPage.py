

class InitPage:

    login_success_date = [
        {"username": "jason", "pwd": "1234567", "expect": "Student Login"},
        {"username": "admin", "pwd": "root", "expect": "Student Login12345"}
    ]


    login_error_data = [
        #  id:msg_uname
        {"username": "jason1", "pwd": "1234567", "expect": "账户名错误或密码错误!别瞎弄!"},
        {"username": "admin", "pwd": "root1", "expect": "账户名错误或密码错误!别瞎弄!"}
    ]










