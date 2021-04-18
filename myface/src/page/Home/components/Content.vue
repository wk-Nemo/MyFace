<template>
  <div>
    <Nav id="nav" :class="{fixedNavbar: isfixTab}" :activeList="activeList"></Nav>
    <div id="section" class="section">
      <div class="section-title">应用场景</div>
      <div class="section-container">
        <div
          class="section-list"
          v-for="(item, index) in list"
          :key=index
        >
          <div
            class="section-item"
            v-for="(block,index) in item"
            :key=index
          >
            <img class="section-item-img" :src="block.url">
            <div class="section-item-info">
              <div class="section-item-info-title">{{ block.title }}</div>
              <div class="section-item-info-content">{{ block.content }}</div>
            </div>
          </div>
        </div>
      </div>
    </div>
    <div id="news" class="news">
      <div class="news-title">相关新闻</div>
      <div class="news-container">
        <div class="news-nav">
          <div class="news-nav-item"
            v-for="(item, index) in news"
            :key="index"
            :class="{'news-nav-item-active': isActiveIndex === index}"
            @click="changeStyle(index)"
          >
            {{ item.title }}
          </div>
        </div>
        <div class="news-content">
          <div class="news-content-left">
            <a :href="news[isActiveIndex].url" class="news-content-title">{{ news[isActiveIndex].title }}</a>
            <div class="content">{{ news[isActiveIndex].content }}</div>
          </div>
          <div class="news-content-right">
            <img :src="news[isActiveIndex].photo">
          </div>
        </div>
      </div>
    </div>
    <div id="superiority" class="superiority">
      <div class="superiority-title">特色优势</div>
      <div class="superiority-container">
        不同于传统人脸识别方案,我们在最重要的数据处理环节选择将用户数据不可逆加密后存储,即使暴露也不必担心安全问题
        <div class="encrypt">
          <div class="ndb">
            <div class="ndb-title">
              <div class="ndb-title-img"></div>
              <div class="ndb-title-msg">负数据库加密</div>
            </div>
            <img src="@/assets/ndb.png" style="width: 100%; margin-top:38px"/>
            <div class="ndb-content">
              目前很多算法被证明是不安全的，无法同时满足不可逆性、可撤销性和不可连接性。而本算法的创新之处在于将负数据库和聚合函数相结合，在不同的应用程序中引入不同的个性化参数，并采用p-hidden算法生成负数据库，使得不同应用中的认证数据之间不可进行交叉匹配，同时满足上述三种特性。
此外，一些已有的方案并未考虑用户提交的人脸凭证数据安全的问题。本算法在用户提交的人脸信息生成负数据库后删除原始人脸信息，仅将转化的负数据库传递给后端，利用负数据库的相似度估算方法和储存的负数据库信息进行比对，达到验证的效果。由于传递的是负数据库并且在传递给后端前时就已经删除了原始信息，因此即使在传递的过程中泄露也无法得到人脸生物信息，从而保证了人脸数据的安全。
            </div>
          </div>
          <div class="line"></div>
          <div class="part">
            <div class="part-title">
              <div class="part-title-img"></div>
              <div class="part-title-msg">局部排序</div>
            </div>
            <img src="@/assets/part.png" style="width: 100%; margin-top:38px"/>
            <div class="part-content">
              我们提出了一种使用局部排序的人脸特征保护方法，可以同时满足国际标准ISO/IEC 24745对生物识别模板提出的不可逆性、可撤销性和不相关性，并且该方法可以获得良好的识别性能。
本方法首先将人脸数据与应用程序特定的字符串按位执行异或运算；然后将执行的结果划分为块，将块划分为组，每个组中的块根据其十进制值进行排序；最后将原始块转换成排序值进行存储，删除原始数据和中间数据。
            </div>
          </div>
        </div>
      </div>
    </div>
  </div>
</template>``

<script>
import Nav from './Nav'
export default {
  name: 'Content',
  components: {
    Nav
  },
  data () {
    return {
      isfixTab: false,
      list: [
        [
          {
            url: 'https://ai.bdstatic.com/file/4EDA347A5D294A9E89E20C2ABEB9DD46',
            title: '人脸实名认证',
            content: '结合身份证识别、人脸对比、活体检测等多项组合能力，连接权威数据源，确保用户是「真人」且为「本人」，快速完成用户身份核验，可应用于金融服务、物流货运等行业，有效控制业务风险，抵御作弊行为'
          },
          {
            url: 'https://ai.bdstatic.com/file/D3023F42158C45C0BF1A284D351ECFA4',
            title: '刷脸闸机通行',
            content: '将人脸识别功能集成到闸机中，快速录入人脸信息，用户刷脸通行，可以解决用户忘带工卡、被盗卡等问题，实现企业、商业、住宅等多场景门禁通行'
          },
          {
            url: 'https://ai.bdstatic.com/file/071B48C3C6B046BD9E51E4B59723543C',
            title: '智慧人脸考勤',
            content: '提供移动考勤、摄像头无感知考勤、一体机考勤三种方案，确保签到人员身份识别准确性，实现1秒内快速认证，有效防止代打卡等作弊行为，增强企业信息化员工管理'
          }
        ],
        [
          {
            url: 'https://ai.bdstatic.com/file/A43BC7BC5B9146F29E6086F77A01B7A6',
            title: '智能视频监控',
            content: '结合人脸识别技术，在工厂、学校、商场、餐厅等人流密集的场所进行监控，对人流进行自动统计、识别和追踪，同时标记存在安全隐患的行为及区域，并发出告警提醒，加强信息化安全管理，降低人工监督成本'
          },
          {
            url: 'https://ai.bdstatic.com/file/81AD4C04B671484E9F1D429021A2DEF1',
            title: '刷脸移动支付',
            content: '应用前端人脸采集方案，搭配百万级人脸库1：N检索功能，将人脸与银行卡、手机等支付工具绑定，解决支付场景对安全、效率、精度的严苛要求，实现「无现金」刷脸支付代替传统密码，提高支付效率与体验'
          },
          {
            url: 'https://ai.bdstatic.com/file/581DF3747DB84CAB865B614226D7CCE7',
            title: '智能相册分类',
            content: '通过人脸检测、人脸搜索、人脸聚类等组合能力，对相册中的图片进行智能分类，将同一个人的照片归为一组，减少人工分类成本，提升产品用户体验'
          }
        ],
        [
          {
            url: 'https://ai.bdstatic.com/file/240D0A7FFA324DD48F68BE8D01A2EE07',
            title: '互动娱乐美颜',
            content: '基于150关键点识别，对人脸五官及轮廓自动精准定位，可自定义对人脸特定位置进行修饰美颜；同时获取表情、情绪等人脸属性信息，实现特效相机、动态贴纸等互动娱乐功能'
          },
          {
            url: 'https://ai.bdstatic.com/file/9E2AD43BD58848F596F4FBAFD2B30FCF',
            title: '人脸注册登录',
            content: '用户注册阶段录入人脸图片，确保用户身份真实性，在安全性要求高的场景中启动人脸登录验证，保障高质量、高效率、低风险的身份核验'
          }
        ]
      ],
      news: [
        {
          url: 'https://medium.com/datavisor/the-face-of-privacy-facial-recognition-privacy-and-security-483ede676267',
          photo: 'https://miro.medium.com/max/2400/1*NizGOvrl6B0js8KnX468ww.png',
          title: 'The “Face” of Privacy: Facial Recognition, Privacy, and Security ',
          content: 'Digital privacy is one side of a two-sided policy coin. Virtually all attention to date has been focused on developing legal and regulatory remedies to address this pervasive public concern'
        },
        {
          url: 'http://news.cctv.com/2021/04/13/ARTI0kVrMdpRcLr8To68corc210413.shtml',
          photo: 'http://p3.img.cctvpic.com/photoworkspace/contentimg/2021/04/13/2021041310522129267.jpg',
          title: '“人脸识别第一案”终审判决：向滥用公民个人信息说“不” ',
          content: '备受关注的“人脸识别第一案”迎来了终审判决。被告杭州野生动物世界被判删除原告郭兵办理指纹年卡时提交的包括照片在内的面部特征信息和指纹识别信息，并于判决生效之日起十日内履行完毕。'
        },
        {
          url: 'https://news.cctv.com/2021/03/18/ARTIojM4XIMEhmT19TdjEyE3210318.shtml',
          photo: 'https://p5.img.cctvpic.com/photoworkspace/2020/10/22/2020102208065374726.jpg',
          title: '不法分子“换脸”骗过人脸识别 如何更好保障个人信息？',
          content: '近来，人脸识别频频引发公众对个人信息泄露的担忧。各大互联网社交平台为保障个人信息安全，维护平台用户权益，引入“刷脸识别”技术。但在利益驱使下，不法分子不断设法利用技术手段突破社交平台的安全设防，这给用户个人信息安全带来威胁，也让社交平台成为受害对象。'
        },
        {
          url: 'https://www.scmp.com/tech/policy/article/3129226/chinas-first-facial-recognition-lawsuit-comes-end-new-ruling-and-new',
          photo: 'https://i.loli.net/2021/04/13/mk1jqUHLwbztXBi.png',
          title: 'China’s first facial-recognition lawsuit comes to an end with new ruling and new questions about the fate of individuals’ data',
          content: 'A court in Hangzhou made its final judgment in China’s first-ever lawsuit over the use of facial recognition after both parties filed for appeal, upholding its original judgment and ordering additional data to be deleted.\nIn late 2019, Hangzhou Safari Park replaced its fingerprint-based admission system with one that uses facial recognition, telling customers that they would be refused entry if they did not use the new system.'
        },
        {
          url: 'https://www.163.com/dy/article/G7EUSJU40512D3VJ.html',
          photo: 'https://gimg2.baidu.com/image_search/src=http%3A%2F%2Fask.qcloudimg.com%2Fhttp-save%2Fyehe-1008345%2Fssbp9yj4v9.jpeg&refer=http%3A%2F%2Fask.qcloudimg.com&app=2002&size=f9999,10000&q=a80&n=0&g=0n&fmt=jpeg?sec=1620909276&t=9b000de8658c4916d59f5f3f8a4a13b3',
          title: '谁“动”了你的脸——人脸识别技术背后的隐私保护',
          content: '如今，从案件侦破、交通安检、课堂监控到金融支付、社区门禁、手机解锁，人脸识别技术不断拓展应用场景，但这项给人类带来便捷的技术背后，也蕴藏着巨大的风险。人脸面部特征的重要性不言而喻。2020年10月1日开始实施的新版推荐性国家标准《信息安全技术个人信息安全规范》已经明确了“人脸信息属于生物识别信息，也属于个人敏感信息，收集个人信息时应获得个人信息主体的授权同意”，并进一步指出，越来越多的组织收集、使用个人信息，给生活带来便利的同时，也出现了对个人信息的非法收集、滥用、泄露等问题，个人信息安全面临严重威胁。'
        },
        {
          url: 'https://news.cctv.com/2021/03/18/ARTIojM4XIMEhmT19TdjEyE3210318.shtml',
          photo: 'https://p1.ivideo.sina.com.cn/video/363/004/778/363004778_400_300.jpg',
          title: '多商家被曝“偷脸” 人脸识别监控错在哪？',
          content: '“为保护个人信息，戴着头盔去看房”，去年这则新闻曾引发一阵热议。在今年3·15晚会上，人脸识别技术的滥用成为曝光重点。商家进行人脸识别，需要消费者的同意。授权法律不断完善，侵犯个人信息后果严重。“人脸等敏感数据的保护需要明确、权威、高效公共监管机关，保持全流程的外部监管，平衡具体场景当中的利益冲突，及时纠正处置各类主体的侵害行为。”吴沈括表示，消费者保护组织、新闻媒体等在内的各类社会主体也应持续强化社会监督，培育用户的维权意识，促进各类数据业务主体的合规意识，为社会打造保护个人信息的良性氛围。'
        },
        {
          url: 'https://news.cctv.com/2020/12/17/ARTI7q9Po75PwiKg1zPGtRl2201217.shtml',
          photo: 'https://tse3-mm.cn.bing.net/th/id/OIP.x5VXdKlaX_Ktq_2WcqUp4gAAAA?pid=ImgDet&rs=1',
          title: '人脸识别日益普及 你的脸刷明白了吗',
          content: '最近，随着“94岁老人被抱起做人脸识别”“为躲人脸识别戴头盔看房”等事件的发生，让人脸识别频上热搜，技术滥用问题引发广泛关注。“人脸识别技术目前已达到工业化、大规模应用标准，简单整形、化妆等常见的识别难题早已被攻克，机器系统的识别能力已超过人类。因此，能否实现整容后识别，要看整容后面部特征的改变程度。如果只是进行美容式整容，如垫高鼻梁、收缩下巴或割双眼皮等，当前技术完全可以做到精准识别；但如果是因为事故导致大面积毁容，人脸识别就无能为力了。”闫怀志表示。'
        },
        {
          url: 'https://news.cctv.com/2020/11/11/ARTIIpurzjsVV0uifuMy76Rt201111.shtml',
          photo: 'https://p1.img.cctvpic.com//photoworkspace/imageLocalized/2020/11/11/2020111106252996099.jpg',
          title: '担忧人脸识别技术有照片泄露风险 如何应对？',
          content: '不少人对于人脸识别技术的应用表示担忧，主要认为其有照片泄露的风险。照片泄露就是人脸识别技术的“锅”吗？面对泄露风险，我们要如何应对？　　伴随着人脸识别技术的发展，其争议始终存在。先是有因不接受动物园将入园方式改成“刷脸”，浙江理工大学副教授郭兵将杭州野生动物世界告上了法庭。而后又发生了清华大学法学院教授劳东燕遇到“不刷脸不让进小区”的情况，对此，劳东燕认为在小区安装人脸识别装置并无必要，并且不经同意收集人脸数据也违反了现行的法律规定，经协商，街道最终同意业主出入小区可以自愿选择门禁卡、手机或人脸识别的方式。目前，不少人对于人脸识别技术的应用表示担忧，主要认为其有照片泄露的风险。人脸照片泄露就是人脸识别技术的“锅”吗？面对泄露风险，我们要如何应对？'
        },
        {
          url: 'http://www.xinhuanet.com/techpro/2021-01/26/c_1127024502.htm',
          photo: 'http://n.sinaimg.cn/tech/crawl/59/w550h309/20201127/2e8b-kentcvx8652740.jpg',
          title: '人脸信息是敏感信息和核心隐私 应该强化保护',
          content: '人脸识别技术正在不断地改变我们的生活，现在已经被大规模地应用于安防、支付等重要场景中。但这项改变生活的技术，如今却处于前所未有的争议之中。针对人脸识别技术被滥用的原因、如何保护好个人隐私等问题，中国人民大学一级教授、中国法学会副会长、民法学会会长王利明表示，在平衡“利用与保护”关系时，人脸信息等敏感信息要更注重保护，其他非敏感信息则更多地强调“利用”。'
        }
      ],
      isActiveIndex: 0,
      activeList: 0
    }
  },
  methods: {
    changeStyle: function (index) {
      this.isActiveIndex = index
    },
    handleTabFix () {
      var scrollTop = window.pageYOffset || document.documentElement.scrollTop || document.body.scrollTop
      // var sectionTop = document.querySelector('#section').offsetTop
      var newsTop = document.querySelector('#news').offsetTop
      var superiorityTop = document.querySelector('#superiority').offsetTop
      scrollTop > 340 ? this.isfixTab = true : this.isfixTab = false
      if (scrollTop < newsTop) {
        this.activeList = 0
      } else if (scrollTop > newsTop && scrollTop < superiorityTop) {
        this.activeList = 1
      } else {
        this.activeList = 2
      }
    }
  },
  mounted () {
    // document.querySelector('.home').addEventListener('scroll', this.handleTabFix, true)
    window.addEventListener('scroll', this.handleTabFix, true)
  }
}
</script>

<style lang="scss" scoped>
.fixedNavbar {
  position: fixed !important;
  left: 0;
  right: 0;
  top: 0;
  background: white;
  z-index: 10;
}
.section {
  padding-top: 80px;
  margin: 0 auto;
  color: black;
  width: 75%;
  .section-title {
    font-size: 20px;
    text-align: center;
  }
  .section-container {
    margin-top: 20px;
    .section-list {
      display: flex;
      margin: 20px 0;
      .section-item {
        flex: auto;
        height: 250px;
        margin: 40px 20px;
        width: 400px;
        transition: transform .5s ease;
        .section-item-img {
          width: 100%;
        }
        .section-item-info {
          box-shadow: 0 5px 20px 0 rgb(210, 208, 208);
          border: 1px solid #eee;
          padding: 20px 48px 22px;
          height: 120px;
          .section-item-info-title {
            font-size: 15px;
            margin-bottom: 20px;
          }
          .section-item-info-content{
            color: #999;
            font-size: 8px;
          }
        }
      }
      .section-item:hover {
        cursor: pointer;
        transform: scale(1.10);
      }
    }
  }
}
.news {
  padding-top: 180px;
  margin: 0 auto;
  color: black;
  width: 75%;
  .news-title {
    font-size: 20px;
    text-align: center;
  }
  .news-container {
    margin-top: 20px;
    display: flex;
    .news-nav {
      width: 200px;
      background: rgb(247, 247, 247);
      padding: 20px 0;
      .news-nav-item {
        padding: 0 10px;
        overflow: hidden;
        text-overflow: ellipsis;
        white-space: nowrap;
        height: 20px;
        font-size: 8px;
        line-height: 20px;
        color: #666;
      }
      .news-nav-item-active {
        height: 35px;
        line-height: 35px;
        background: rgb(11,116,233);
        color: white;
      }
      .news-nav-item:hover {
        color:  rgb(11,116,233);
        cursor: pointer;
      }
      .news-nav-item-active:hover {
        color: white;
      }
    }
    .news-content {
      flex: 1;
      padding: 20px;
      display: flex;
      .news-content-left{
        padding-right: 20px;
        flex: 1;
        .news-content-title{
          font-size: 16px;
          font-weight: 600;
        }
        .content {
          margin: 20px 0;
          font-size: 6px;
          line-height: 17px;
        }
      }
      .news-content-right {
        width: 250px;
        img {
          width: 100%;
        }
      }
    }
  }
}
.superiority {
  padding-top: 80px;
  margin: 0 auto;
  color: black;
  width: 75%;
  .superiority-title {
    font-size: 20px;
    text-align: center;
  }
  .superiority-container {
    margin: 20px 0;
    text-align: center;
    .encrypt {
      display: flex;
      height: 500px;
      margin: 20px 0;
      .ndb {
        flex: 1;
        position: relative;
        width: 480px;
        .ndb-title {
          display: flex;
          position: absolute;
          left: 50%;
          transform: translate(-50%);
          .ndb-title-img {
            width: 30px;
            height: 30px;
            background-image: url("https://ai.bdstatic.com/file/D0E2AF8227C24812A26B9AC1FDE8D647");
            background-size: 30px 30px;
          }
          .ndb-title-msg {
            font-size: 18px;
            font-weight: 900;
            line-height: 30px;
            margin-left: 20px;
          }
        }
        .ndb-content {
          padding: 10px;
          margin-top: 50px;
          font-size: 6px;
          line-height: 17px;
          text-align: left;
        }
      }
      .line {
        border-left: 1px solid rgb(247,247,247);
      }
      .part {
        flex: 1;
        position: relative;
        width: 480px;
        .part-title {
          display: flex;
          position: absolute;
          left: 50%;
          transform: translate(-50%);
          .part-title-img {
            background-image: url("https://ai.bdstatic.com/file/A58A8DDBEB6D41698E2E2579B9EB406B");
            width: 30px;
            height: 30px;
            background-size: 30px 30px;
          }
          .part-title-msg {
            font-size: 18px;
            font-weight: 900;
            line-height: 30px;
            margin-left: 20px;
          }
        }
        .part-content {
          padding: 10px;
          margin-top: 50px;
          font-size: 6px;
          line-height: 17px;
          text-align: left;
        }
      }
    }
  }
}
</style>
