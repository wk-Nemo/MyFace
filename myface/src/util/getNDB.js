class MyNDB {
  constructor (descriptor) {
    this.originalData = this.getOriginal(descriptor) 
    this.before_s = this.originalData.before_s // 原始串s
    this.lens = this.originalData.lens         // 隐藏串s的每个128维向量二进制串的长度
    this.flag = this.originalData.flag         // 原始数据的正负号
    this.m = this.before_s.length              // 字符串s位数
    this.r = 10
    this.cn = this.m * this.r                  // NDB长度
    this.specific = this.getSpecific()         // 异或串
    this.s = this.xor(this.before_s)           // 异或后的隐藏串s
    this.p = [0, 0.95, 0.03, 0.02]             // 概率参数p，表示取第几种类型的概率
    this.q = [0.55, 0.05, 0.05, 0.05, 0.05, 0.05, 0.05, 0.05, 0.05, 0.05] // 概率参数q，表示第几位取反的概率
    this.posbility = this.getPosibility()      // 概率，[i][0]是取反的概率（Pdiff），[i][1]是取正的概率（Psame）
    this.cc = this.getCC()                     // 0-1023的01串
    this.NDB = this.f(this.s)                  // 转换后的负数据库
    this.Pos = this.num_01()                   // 位置
    this.Gen = this.getAttr()                  // 期望值
    this.trueGen = this.getOriginalGen()       // 真实期望值
  }

  // 原始数据结构体
  OriginalData (before_s, lens, flag) {
    this.before_s = before_s
    this.lens = lens
    this.flag = flag
  }

  // 获取原始串
  getOriginal (descriptor) {
    let before_s = ''
    let lens = []
    let flag = []
    // 生成s
    for (let i=0; i<128; i++) {
      var n = this.floatTo2(descriptor[i])
      lens[i] = n.len
      before_s = before_s.concat(n.s)
      flag[i] = n.flag
    }
    return new this.OriginalData(before_s, lens, flag)
  }

  // 存储单个数据的结构体
  MyNumber(s, len, flag) {
    this.s = s       // 每个数字的二进制
    this.len = len   // 每个数字的二进制长度
    this.flag = flag // 每个数字的正负号
  }

  // 将128个数据转换成二进制并且连接在一起
  floatTo2(num) {
    // 判断正负号
    var a = []
    if(num > 0) {
        var flag = 1
    } else {
        var flag = -1
        num = -num
    }

    // 将数字主体部分转换成整数并二进制化
    var b = num*Math.pow(10, 3)
    b = Math.round(b)
    b = b.toString(2)
    
    // 将不足部分的0填进去
    for (let i=0; i<10-b.length; i++) {
        a.push('0')
    }

    //将主体部分二进制串和头部符号合在一起
    var front = a.join('')
    var result = front.concat(b)
    
    // 将二进制串和长度一起传递给MyNumber
    var myNum = new this.MyNumber(result, result.length, flag)
    return myNum
  }

  // 生成异或串
  getSpecific() {
    var specific_res = []
    for (let i=0; i<1280; i++) {
        let x = Math.random()
        if (x < 0.5) {
            specific_res.push('0')
        } else {
            specific_res.push('1')
        }
    }
    var res = specific_res.join('')
    return res
  }

  // 异或操作
  xor(s) {
    let res = []
    for (let i=0; i<1280; i++) {
        if (s[i] === this.specific[i]) {
            res.push('0')
        } else {
            res.push('1')
        }
    }
    let result = res.join('')
    return result
  }

  // 获取posibility
  getPosibility () {
    let posbility = []
    for (let i = 0; i < 10; i++) {   
      posbility[i] = []
      posbility[i][0] = this.diff(i)   //每一个属性与隐藏串不同的概率  即属性取反
      posbility[i][1] = 1 - posbility[i][0]   //每一个属性与隐藏串想同的概率
    } 
    return posbility
  }

  // 辅助获取posility
  diff (i) {
    var Ndiff = 0
    var Nsame = 0
    for (let j = 1; j <= 3; j++) {
      Ndiff += j * this.p[j] * this.q[i]    //求和  公式6
    }
    for (let j = 1; j <= 3; j++) {
      Nsame += ((3 - j) * this.p[j]) / 10  //属性中长度最大的为10   //公式7
    }

    var Pdiff = 0
    Pdiff = Ndiff / (Ndiff + Nsame)  //控制一个属性中第i位不同于隐藏串s   公式5
    return Pdiff
  }

  myTo2 (num) {
    // 判断正负号
    var a = []
    // 将数字主体部分转换成整数并二进制化
    var b = num.toString(2)   
    // 将不足部分的0填进去
    for (let i  =0; i < 10 - b.length; i++) {
        a.push('0')
    }
    //将主体部分二进制串和头部符号合在一起
    var front = a.join('')
    var result = front.concat(b) 
    return result
  }

  getCC () {
    let cc = []
    for (let i = 0; i <= 1023; i++) {
      cc.push(this.myTo2(i))
    }
    return cc
  }

  // 反位生成
  generateRandomNumbers(l) { 
    var count = 0
    for (let i=9; i>=0; i--) {
      count += this.q[i]
      if (l < count) {
        return i
      }
    }
  }

  //判断0，1
  judge(s) {
    if(s === '1') {
      return '0'
    } else {
      return '1'
    }
  }

  // 存储单个生成的负数据库信息的数据结构
  Ent(p, c) {
    this.p = p  // 三个位
    this.c = c  //记录此位是'0'还是'1’
  }

  //生成负数据库
  f (s) {
    let NDB = []
    var n = 0
    do {
      var v_p =[]
      var v_c = []
      var v = new this.Ent(v_p, v_c)
      //生成0-1的随机数，用于选择属性
      var t = Math.random()
      //生成类型一
      if(t < this.p[1]) {
        // console.log("1")
        var diff1 = 0
        var same1 = 0
        var same2 = 0
        var attr = 0
        // 随机生成属性的号数，即选择哪个属性
        attr = Math.floor(Math.random()*128)

        // 通过属性q决定属性的哪一位与原始位不同  得到不同类型的位
			  diff1 = this.generateRandomNumbers(Math.random())
        // 生成的反转的位数
			  v.p[0] = diff1 + attr * 10 
        // 反转后的字符，与s相反
			  v.c[0] = this.judge(s[v.p[0]]) 

        same1 = Math.floor(Math.random()*10)
        while (same1 === diff1) {   //如果与反转位的位号相同，则重新生成
          same1 = Math.floor(Math.random()*10)
        }
        v.p[1] = same1 + attr * 10;    //相同位
        v.c[1] = s[v.p[1]];

        same2 = Math.floor(Math.random()*10)
        while (same2 === diff1 || same2 === same1) {
          same2 = Math.floor(Math.random()*10)
        }
        v.p[2] = same2 + attr * 10;
        v.c[2] = s[v.p[2]];
      }
      //生成类型二
      else if(t < this.p[1] + this.p[2]) {
        var diff1 = 0
        var diff2 = 0
        var same1 = 0
        var attr = 0
  			attr = Math.floor(Math.random()*128)
        // 通过属性q决定属性的哪一位与原始位不同  得到不同类型的位
  			diff1 = this.generateRandomNumbers(Math.random())
        // 生成的反转的位数
	  		v.p[0] = diff1 + attr * 10;    
        // 反转后的字符，与s相反
		  	v.c[0] = this.judge(s[v.p[0]])  
        diff2 = this.generateRandomNumbers(Math.random())
        while (diff2 === diff1) {
  				diff2 = this.generateRandomNumbers(Math.random());
	  		}
        v.p[1] = diff2 + attr * 10;
		  	v.c[1] = this.judge(s[v.p[1]]) 

        same1 = Math.floor(Math.random()*10)
			  while (same1 === diff1 || same1 === diff2) {
				  same1 = Math.floor(Math.random()*10)
			  }
			  v.p[2] = same1 + attr * 10;
			  v.c[2] = s[v.p[2]];
      }
      //生成类型三
      else {
        var diff1 = 0
        var diff2 = 0
        var diff3 = 0
        var attr = 0
        // 随机生成属性的号数，即选择哪个属性
			  attr = Math.floor(Math.random()*128)
        // 通过属性q决定属性的哪一位与原始位不同  得到不同类型的位
			  diff1 = this.generateRandomNumbers(Math.random())
        // 生成的反转的位数
			  v.p[0] = diff1 + attr * 10    
        // 反转后的字符，与s相反
			  v.c[0] = this.judge(s[v.p[0]])   
        diff2 = this.generateRandomNumbers(Math.random())
        while (diff2 === diff1) {
			  	diff2 = this.generateRandomNumbers(Math.random());
			  }
        v.p[1] = diff2 + attr * 10
		  	v.c[1] = this.judge(s[v.p[1]]) 

        diff3 = this.generateRandomNumbers(Math.random())
        while (diff3 === diff1 || diff3 === diff2) {
				  diff3 = this.generateRandomNumbers(Math.random());
			  }
        v.p[2] = diff3 + attr * 10;
			  v.c[2] = this.judge(s[v.p[2]]) 
      }
      //负数据库确定位赋值 
      NDB[n] = v
      n++
    }while(n < this.cn)
    return NDB
  }

  /*计算期望，得到一个串*/ 
  // 统计负数据库中0和1的个数
  num_01 () {
    let Pos = []
    for (let i = 0; i < this.m; i++) {
      Pos[i] = []
      Pos[i][0] = 0
      Pos[i][1] = 0
	  }
    for (let i = 0; i < this.cn; i++) {
      for (let j = 0; j < 3; j++) {
        if (this.NDB[i].c[j] === '0') {
          Pos[this.NDB[i].p[j]][0]++
        }
        else {
          Pos[this.NDB[i].p[j]][1]++
        }
      }
    }
    return Pos
  }

  /*进行欧氏距离计算*/
  //传入的值为原始串中第i位的索引值(可以认为第i个属性值的第一位索引值    num为原串在该位的值为0或者1)
  Pr (index, num) {
    var pr1 = 0
    var pr0 = 0
    var tmp = index % 10
    var pdiff = this.posbility[tmp][0]
    var psame = this.posbility[tmp][1]
    pr0 = (Math.pow(pdiff, this.Pos[index][1])*Math.pow(psame, this.Pos[index][0])) / (Math.pow(pdiff, this.Pos[index][1])*Math.pow(psame, this.Pos[index][0]) + Math.pow(pdiff, this.Pos[index][0])*Math.pow(psame, this.Pos[index][1]))
    if (num === '1') {
      pr1 = 1 - pr0
      return pr1
    }
    else {
      return pr0
    }
  }

  // 计算每个属性为-999-999的概率
  // index分别是0， 11， 22 ...等一系列128个数据
  // real是-999-999等所有可能会出现的值
  calculate(index, real) {
    // sum是概率
    var sum = 1
    // 分别计算每一位的概率，然后相乘得到sum的概率
    for (let i=0; i<10; i++) {
      // index表示的是位置；cc表示的是-999到999的每个数的二进制
      var tmp = this.Pr(index + i, this.cc[real][i])
      sum = sum*tmp
    }
    // 概率和值相乘，满足定理3中的一项
    // sum *= Math.pow(real, 2)
    sum *= real
    return sum
  }

  // 计算每个属性的期望值，采用定理三的公式
  // index分别是0， 10， 20 ... 1270等一系列128个数据
  E (index) {
    // tmp是总和，欧氏距离
    var tmp = 0
    for (let i=0; i<=1023; i++) {
      tmp += this.calculate(index, i) 
    }
    // tmp = Math.pow(tmp, 0.5)
    return tmp
  }

  // 计算128个属性数据的期望
  getAttr () {
    var count = 0
    let Gen = []
    for (let i=0; i<this.m; i++) {
      if (i % 10 === 0) {
        Gen[count] = this.E(i) * 0.001
        count++
      }
    }
    return Gen
  }

  // 合并的二进制串s转换成128向量
  to128Float (s, lens) {
    var res = []
    var count = 0
    // 使用一个简单的slice将128个数据连接在一起
    for (let i=0; i<128; i++) {
      res[i] = s.slice(count, count+lens[i])
      count = count + lens[i] 
    }
    return res
  }

  // 二进制小数转换成十进制数的方法
  // 该方法主要将128个数据的二进制转换成十进制
  toFloat(s, flag) {
    var num = 0
    var count = 9
    for (let i=0; i<10; i++) {
      if (s[i] === '1') {
        num += Math.pow(2, count)
      }
      count--
    }
    num = num*flag
    return num
  }

  getOriginalGen () {
    // 验证正确性
    // 将Gen转换成二进制串得到新的s再异或回去
    var after_s = ''
    for (let i=0; i<128; i++) {
      var n = this.floatTo2(this.Gen[i])
      after_s = after_s.concat(n.s)
    }
    // 期望串s
    var result_s = this.xor(after_s)
    var result_128s = this.to128Float(result_s, this.lens)
    var result_nums = []
    for (let i=0; i<128; i++) {
      var result_num = this.toFloat(result_128s[i], this.flag[i])
      result_nums.push(result_num)
    }
    return result_nums
  }
}

export  { MyNDB }