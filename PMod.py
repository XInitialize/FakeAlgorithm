class PMod:
    """
    ---
    PMod算法
    ---
    对不规整列表进行均匀采样的算法之一，对原表长度a和样本容量b进行取模等操作，
    具体采样方法如下：

    定义方法
    + M(a, b, flag):
    + + a / b = d ... r1
    + + a / d = a’ ... r2
    + + b’ = a’ - b
    + + if r1 == r2 : # 此时 b’恒等于0
    + + +     END
    + + else:
    + + +     M(a’, b’, -flag)

    """

    def __init__(self, a: int, b: int):
        """Define 'a' and 'b'

        Args:
            a (int): length of source
            b (int): samples
        """
        self.a = a
        self.b = b

    @staticmethod
    def _dvd(numerator: int, denominator: int) -> tuple:
        """整数的除法运算

        Args:
            numerator (int): 被除数
            denominator (int): 除数

        Returns:
            tuple: (商, 余数) 
        """
        quotient = int(numerator/denominator)
        remainder = numerator - quotient*denominator
        return quotient, remainder

    @staticmethod
    def _mod(a: int, b: int) -> int:
        """求模

        Args:
            a (int): 被取模数
            b (int): 取模数

        Returns:
            int: 模
        """
        return a-b*int(a/b)

    def _pm(self, a: int, b: int) -> tuple:
        """PMod算法主体

        Args:
            a (int): 母集长度
            b (int): 子集长度

        Returns:
            tuple: distance, a', b', r1, r2
        """
        d, r1 = self._dvd(a, b)
        af, r2 = self._dvd(a, d)
        bf = af-b
        return d, af, bf, r1, r2

    def _iter(self, s: list, flag: int, d: int) -> tuple:
        """迭代方法

        Args:
            s (list): 输入集
            flag (int): flag
            d (int): 距离

        Returns:
            tuple: 输出集, 新flag, 距离
        """
        sret = []
        flag = 1-flag
        for i in range(len(s)):
            if self._mod(i+1, d) == 0:
                sret.append(flag)
            else:
                sret.append(s[i])
        return sret, flag, d

    def get_sample_flags(self) -> list:
        """获取样本标记表

        Returns:
            list: 标记表
        """
        a = self.a
        b = self.b
        d = 1
        flag = 0
        s = [0]*a
        while True:
            dn, af, bf, _, _ = self._pm(a, b)
            d = d*dn
            print("--------")
            print(f"a:{a},b:{b},d:{d},dn:{dn},af:{af},bf:{bf},flag:{flag}")
            # print(f"s:{s}")
            a = af
            b = bf
            s, flag, d = self._iter(s, flag, d)
            # print(f"sn:{s}")
            print("--------")
            if bf == 0:
                break
        return s

    def get_sample_by_list(self, ll: list) -> list:
        """取样方法

        Args:
            ll (list): 样本列表

        Returns:
            list: [description]
        """
        return [li for li, g in zip(ll, self.get_sample_flags()) if g]


if __name__ == "__main__":
    pm = PMod(10235, 2200)
    rst = pm.get_sample_by_list([i for i in range(10235)])
    print(rst)
