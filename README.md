# python_unittest_interface

（1）run.py主运行文件，运行之后可以生成相应的测试报告，并以邮件形式发送；

（2）report文件夹存放测试结果报告；

（3）unit_test文件夹是存放测试用例（demo.py和test_unittest.py用例用法介绍，实际项目中可以按照不同模块新建python package，来存放不同模块的接口用例）；

（4）util对测试接口相关方法的封装：HTMLTestRunner.py生成测试报告的封装；send_mail.py发送邮件的封装；test_get_post.py接口请求类型的封装。