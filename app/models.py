# -*-coding:utf-8 -*-
from werkzeug.security import generate_password_hash, check_password_hash
from app import connection
import math


class Kjhm(object):
    def __init__(self, num1, num2, num3, num4, num5, num6, num7, id=None, qh=0, kjrq="", sales=0, first=0, secend=0):
        self.num1 = num1
        self.num2 = num2
        self.num3 = num3
        self.num4 = num4
        self.num5 = num5
        self.num6 = num6
        self.num7 = num7
        self.id = id
        self.qh = qh
        self.kjrq = kjrq
        self.sales = sales
        self.first = first
        self.secend = secend

    @staticmethod
    def pagenum():
        sql = "SELECT COUNT(`id`) FROM `duan`.`kjhm`;"
        with connection.cursor() as cursor:
            cursor.execute(sql)
            count = cursor.fetchone()[0]
            connection.commit()
            cursor.close()
        return math.ceil(int(count)/30)

    @staticmethod
    def getkjhmbyrq(kjrq):
        sql = '''SELECT `id`, `qh`, `kjrq`, `num1`, `num2`, `num3`, `num4`, `num5`, `num6`, `num7`, `sales`, `first`,
        `secend` FROM `duan`.`kjhm` WHERE `kjrq` = %s;'''
        with connection.cursor() as cursor:
            cursor.execute(sql, kjrq)
            row = cursor.fetchone()
            connection.commit()
            cursor.close()
        if row is not None:
            kjhm = Kjhm(row[3], row[4], row[5], row[6], row[7], row[8], row[9], row[0], row[1], row[2], row[10],
                        row[11], row[12])
            return kjhm
        return None

    @staticmethod
    def getkjhmbycount(start=0, end=30):
        kjxx = []
        sql = '''SELECT `id`, `qh`, `kjrq`, `num1`, `num2`, `num3`, `num4`, `num5`, `num6`, `num7`, `sales`, `first`,
            `secend` FROM `duan`.`kjhm` LIMIT %s, %s;'''
        with connection.cursor() as cursor:
            cursor.execute(sql, (start, end))
            rows = cursor.fetchall()
            connection.commit()
            cursor.close()
        for row in rows:
            kjhm = Kjhm(row[3], row[4], row[5], row[6], row[7], row[8], row[9], row[0], row[1], row[2], row[10],
                        row[11], row[12])
            kjxx.append(kjhm)
        return kjxx

    # @staticmethod
    # def select_with_condition(kjxx, ball_color, select_condition, ball):
    #     results = []
    #     if ball_color == 'red' and select_condition == 'equal':
    #         for info in kjxx:
    #             if ball in [info.num1, info.num2, info.num3, info.num4, info.num5, info.num6]:
    #                 if select_condition

    @staticmethod
    def get_count_by_col(col, ball):
        sql = '''SELECT COUNT(`id`) FROM `duan`.`kjhm` WHERE %s=%s;'''
        with connection.cursor() as cursor:
            cursor.execute(sql, (col, ball))
            count = cursor.fetchone()[0]
            connection.commit()
            cursor.close()
        return int(count)

    @staticmethod
    def get_kjhm_and_weather_by_count(start=0, end=30):
        sql = '''SELECT `weathar`.`id`, `qh`, `kjrq`, `num1`, `num2`, `num3`, `num4`, `num5`, `num6`, `num7`, `sales`, `first`,
            `secend`, `desc`, `wd` FROM `kjhm`, `weathar` WHERE `weathar`.`rq` = `kjhm`.`kjrq` LIMIT %s, %s;'''
        with connection.cursor() as cursor:
            cursor.execute(sql, (start, end))
            results = cursor.fetchall()
            connection.commit()
            cursor.close()
            return results

    @staticmethod
    def get_kjhm_and_weather_by_col(col, ball, desc):
        sql = '''SELECT count(`weathar`.`id`) FROM `kjhm`, `weathar` WHERE `kjhm`.%s = %s and \
         `weathar`.`desc` = %s and `weathar`.`rq` = `kjhm`.`kjrq`;'''
        with connection.cursor() as cursor:
            cursor.execute(sql, (col, ball, desc))
            count = cursor.fetchone()[0]
            connection.commit()
            cursor.close()
        return int(count)


class User(object):

    def __init__(self, username, password_hash, role_id, address, email, id=None):
        self.id = id
        self.username = username
        self.roleid = role_id
        self.password_hash = password_hash
        self.address = address
        self.email = email

    def __repr__(self):
        if self.id is None:
            return "<User: name:%s,role:%d,email:%s,address:%s>" % (
                self.username, self.roleid, self.email, self.address)
        else:
            return "<User: id:%d, name:%s,role:%d,email:%s,address:%s>" % (
                self.id, self.username, self.roleid, self.email, self.address)

    @property
    def password(self):
        raise AttributeError('password is not a readable attribute')

    @password.setter
    def password(self, password):
        self.password_hash = generate_password_hash(password)

    def verify_password(self, password):
        return check_password_hash(self.password_hash, password)

    @staticmethod
    def getuserbyname(name):
        sql = '''SELECT `id`, `username`, `password_hash`, `role_id`, `address`, `email` FROM `duan`.`users`
        WHERE `username` = %s;'''
        print(sql)
        with connection.cursor() as cursor:
            cursor.execute(sql, name)
            row = cursor.fetchone()
            connection.commit()
            cursor.close()
        if row is not None:
            user = User(row[1], row[2], row[3], row[4], row[5], row[0],)
            return user
        return None

    @staticmethod
    def insertuser(user):
        sql = '''INSERT INTO `duan`.`users` (`username`, `password_hash`, `role_id`, `address`, `email`) VALUES
         (%s, %s, %s, %s, %s);'''
        with connection.cursor() as cursor:
            cursor.execute(sql, (user.username, user.password_hash, user.roleid, user.address, user.email))
            connection.commit()
            cursor.close()


class Role(object):
    def __init__(self, rolename, level=None, id=None):
        self.rolename = rolename
        self.level = level
        self.id = id

    @staticmethod
    def getrolebyid(role_id):
        sql = '''SELECT `id`, `rolename`, `level` FROM `duan`.`role` WHERE `id` = %s'''
        with connection.cursor() as cursor:
            cursor.execute(sql, role_id)
            row = cursor.fetchone()
            connection.commit()
            cursor.close()
        role = Role(id=row[0], rolename=row[1], level=row[2])
        return role

    @staticmethod
    def getallrole():
        sql = '''SELECT `id`, `rolename`, `level` FROM `duan`.`role`;'''
        with connection.cursor() as cursor:
            cursor.execute(sql)
            rows = cursor.fetchall()
            connection.commit()
            cursor.close()
        roles = []
        for row in rows:
            role = Role(id=row[0], rolename=row[1], level=row[2])
            roles.append(role)
        return roles


class Weather(object):
    @staticmethod
    def get_desc_count():
        sql = '''select count(`desc`) from `weathar`;'''
        with connection.cursor() as cursor:
            cursor.execute(sql)
            count = cursor.fetchone()
            connection.commit()
            cursor.close()
        return int(count)

    @staticmethod
    def get_desc_count_by_desc(desc):
        sql = '''select count(`id`) from `weathar` where `desc` = %s;'''
        with connection.cursor() as cursor:
            cursor.execute(sql, desc)
            count = cursor.fetchone()[0]
            connection.commit()
            cursor.close()
        return int(count)





