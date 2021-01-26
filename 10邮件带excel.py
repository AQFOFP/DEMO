# 发邮件的库
import smtplib
# 邮件文本
from email.mime.text import MIMEText


SMTPServer = "smtp.qq.com"  # SMTP服务器
sender = "aqfofp@qq.com"   # 发邮件的地址
token = "tlouppbbpqaobddi"  # 发送者邮箱的token

# message = "sunck is a good man"  # 设置发送的内容

html = """
        <html>
        <head><meta http-equiv="Content-Type" content="text/html; charset=utf-8" /></head>
            <body>
                <div id="container">
                    <p><strong>测试程序邮件发送:</strong></p>
                    <div id="content">
                         <table border="1" bordercolor="gray" cellspacing="0" cellpadding="0">
                            <tr>
                              <th align="center"><strong>排序</strong></td>
                              <th align="center"><strong>日期</strong></td>
                              <th align="center"><strong>用户价值</strong></td>
                              <th align="center"><strong>uid</strong></td>
                              <th align="center"><strong>rid</strong></td>
                              <th align="center"><strong>流失等级</strong></td>
                              <th align="center"><strong>昵称</strong></td>
                              <th align="center"><strong>性别</strong></td>
                              <th align="center"><strong>国家</strong></td>
                              <th align="center"><strong>平台</strong></td>
                              <th align="center"><strong>用户等级</strong></td>
                              <th align="center"><strong>VIP等级</strong></td>
                              <th align="center"><strong>注册时间</strong></td>
                              <th align="center"><strong>最近登录时间</strong></td>
                              <th align="center"><strong>近15天在房时长</strong></td>
                              <th align="center"><strong>近7天收礼物流水</strong></td>
                              <th align="center"><strong>近7天发礼物流水</strong></td>
                              <th align="center"><strong>最近一次充值时间</strong></td>
                            </tr>
                        </table>
                    </div>
                </div>
            </body>
        </html>
      """

html2 = """
    <!DOCTYPE html>
    <html>
    <head>
        <meta charset="utf-8"> 
        <title>Bootstrap 实例 - 边框表格</title>
        <link rel="stylesheet" href="https://cdn.staticfile.org/twitter-bootstrap/3.3.7/css/bootstrap.min.css">  
        <script src="https://cdn.staticfile.org/jquery/2.1.1/jquery.min.js"></script>
        <script src="https://cdn.staticfile.org/twitter-bootstrap/3.3.7/js/bootstrap.min.js"></script>
    </head>
    <body>
    
    <table class="table table-bordered">
        <caption>边框表格布局</caption>
        <thead>
            <tr>
                <th>名称</th>
                <th>城市</th>
                <th>邮编</th>
            </tr>
        </thead>
        <tbody>
            <tr>
                <td>Tanmay</td>
                <td>Bangalore</td>
                <td>560001</td>
            </tr>
            <tr>
                <td>Sachin</td>
                <td>Mumbai</td>
                <td>400003</td>
            </tr>
            <tr>
                <td>Uma</td>
                <td>Pune</td>
                <td>411027</td>
            </tr>
        </tbody>
    </table>
    
    </body>
    </html>
"""

msg = MIMEText(html2, _subtype='html', _charset='utf-8')  # 转换成邮件文本
msg["From"] = sender  # 设置发送者
msg["Subject"] = "excel表格测试"   # 设置标题


if __name__ == '__main__':

    # mailServer = smtplib.SMTP(SMTPServer, 465)
    mailServer = smtplib.SMTP_SSL(SMTPServer, 465)  # 创建SMTP服务器

    mailServer.login(sender, token)  # 登陆邮箱

    # 发送邮件
    mailServer.sendmail(sender, ['aqfofp@qq.com'], msg.as_string())
    mailServer.quit()  # 退出邮箱