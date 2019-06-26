# team_go_backend

## 环境说明

    + Python 3.6.2
    + Django 2.0

## 项目启动

    + `git clone https://github.com/jin-hao-chen/team_go_backend.git`
    + `cd team_go_backend`
    + `pip install -r requirements.txt` 安装 Python 的第三方依赖
    + `python manage.py runserver 127.0.0.1:8080` 启动服务


## 注释要求
    
    + 目前现已以 apps/models.py 文件中的 AdminInfo 中的注释为参考
    ```py
        class AdminInfo(AbstractUser):
        """后台管理员表
        
        Notes
        -----
        AdminInfo 和 学生表是分开来的, AdminInfo 是提供给后台内部使用的
        一般用于后台统计数据, 导出统计数据文件等, 因此 AdminInfo 只包含了
        少数的字段
        """
        username = models.CharField(max_length=10, validators=[validate_username], verbose_name='学号', unique=True)
        password = models.CharField(max_length=128, verbose_name='密码')
        nickname = models.CharField(max_length=30, verbose_name='昵称', blank=True, null=True)
        mobile = models.CharField(max_length=11, verbose_name='手机号', blank=True, null=True)
        email = models.EmailField(_('邮箱'), blank=True)

    ```
    + 在 """ 之后紧接着此类, 此方法或者此函数的简单说明, 要求见名知意
    + Notes 用于描述此类, 此方法或者此函数的说明
    + AdminInfo 中没有参数, 如果有参数的方法或者函数则按照如下案例注释
    ```py
    
    def add(num1, num2):
        """计算两个数的和

        Parameters
        ----------
        num1 : int 类型
            换行, 如果对该参数有额外的说明则在此换行处说明, 如果没有则跳过
        
        num2 : int 类型

        Returns
        -------
        sum : int 类型
            sum 变量名不是任意去的, 应该是此函数或者方法 `return` 的变量名

        Notes
        -----
        如果函数比较简单, 不需要写 Notes

        Examples
        --------
            如果觉得上面表达的不清楚, 可以添加 Examples 项, 通过代码的方式进行举例说明
        """
    ```
   
## 响应数据格式
    
    + json
    
    ```py
    
    In Headers
        status_code = restful_code.CODE_SUCCESS
    
    ret_data = {
        "detail": "Put your detail here",
        "Other options": "Value"
    }
    ```

## git commit 说明

    + 每一次 git 提交指明自己的拼音错写, 如 `cjh`, 这样可以方便定位代码是谁修改了
    + 例如 `git commit -m "cjh: 在 README.md 中添加了 git commit 的要求"`
    + 如果有 BUG, 也需要指出

## 项目说明
    
    + 此项目也可以当做 xadmin 和 DjangoUeditor 的模板, 因为已经配置好了 xadmin 和 DjangoUeditor

